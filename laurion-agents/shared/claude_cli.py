"""Model calls through headless Claude Code (`claude -p`) on a subscription.

Every model call in the project goes through `call()`. It runs the `claude`
CLI with tools, MCP servers, slash commands and settings files disabled, so
the model sees only our system prompt and messages (plus the short
environment block Claude Code always adds: date, working directory). It runs
in an empty temp directory so no CLAUDE.md or git status from this repo leaks
into the context.

Multi-turn conversations use Claude Code sessions: the first call passes
`session_id` with `resume=False`, later calls pass the same id with
`resume=True`.

ANTHROPIC_API_KEY is stripped from the child environment so the CLI always
bills the logged-in subscription, never an API key.
"""

import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Optional

_WORKDIR: Optional[Path] = None


class RefusalError(RuntimeError):
    pass


def _workdir() -> Path:
    global _WORKDIR
    if _WORKDIR is None:
        _WORKDIR = Path(tempfile.mkdtemp(prefix="laurion-claude-"))
    return _WORKDIR


def call(prompt: str, *, system: str, model: str, effort: str,
         schema: Optional[dict] = None, session_id: Optional[str] = None,
         resume: bool = False, max_tokens: Optional[int] = None,
         timeout: int = 3600) -> dict:
    """Run one turn and return Claude Code's JSON result.

    Useful keys: `result` (text), `structured_output` (when `schema` is
    given), `usage`, `total_cost_usd`, `modelUsage`, `session_id`.
    """
    if shutil.which("claude") is None:
        raise RuntimeError("`claude` CLI not found on PATH; install Claude Code and log in.")
    wd = _workdir()
    sys_file = wd / "system.md"
    sys_file.write_text(system, encoding="utf-8")

    cmd = [
        "claude", "-p",
        "--output-format", "json",
        "--model", model,
        "--effort", effort,
        "--system-prompt-file", str(sys_file),
        "--tools", "",
        "--strict-mcp-config",
        "--setting-sources", "",
        "--disable-slash-commands",
        # No --fallback-model: a declined or overloaded request fails loudly.
    ]
    if schema is not None:
        cmd += ["--json-schema", json.dumps(schema)]
    if session_id is None:
        cmd.append("--no-session-persistence")
    elif resume:
        cmd += ["--resume", session_id]
    else:
        cmd += ["--session-id", session_id]

    env = {k: v for k, v in os.environ.items() if k != "ANTHROPIC_API_KEY"}
    if max_tokens:
        env["CLAUDE_CODE_MAX_OUTPUT_TOKENS"] = str(max_tokens)

    proc = subprocess.run(cmd, input=prompt, capture_output=True, text=True,
                          cwd=wd, env=env, timeout=timeout)
    try:
        out = json.loads(proc.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"claude -p failed (exit {proc.returncode}): "
                           f"{(proc.stderr or proc.stdout)[-2000:]}")

    if out.get("stop_reason") == "refusal":
        raise RefusalError(out.get("result", "refused"))
    if out.get("stop_reason") == "max_tokens":
        raise RuntimeError("Hit max_tokens; raise max_tokens for this stage.")
    if out.get("is_error") or out.get("subtype") != "success":
        raise RuntimeError(f"claude -p error ({out.get('subtype')}, "
                           f"api status {out.get('api_error_status')}): {out.get('result')}")

    # Fallback is off: refuse any answer that came from a different model.
    used = {v.get("canonicalModel", k) for k, v in out.get("modelUsage", {}).items()}
    if used - {model}:
        raise RuntimeError(f"Requested {model} but Claude Code used {sorted(used)}.")
    if schema is not None and out.get("structured_output") is None:
        raise RuntimeError("No structured output returned.")
    return out


def usage_record(out: dict, prior_session_cost: float = 0.0) -> dict:
    """What we log per call in meta.json.

    On a resumed session, Claude Code's `total_cost_usd` is the running total
    for the whole session, so pass the previous call's total to get this
    call's own cost. Costs are list-price equivalents; the subscription is
    what's actually billed.
    """
    session_total = out.get("total_cost_usd") or 0.0
    return {
        **out.get("usage", {}),
        "models": sorted(out.get("modelUsage", {})),
        "cost_usd": round(session_total - prior_session_cost, 6),
        "session_total_cost_usd": session_total,
        "duration_ms": out.get("duration_ms"),
        "session_id": out.get("session_id"),
    }
