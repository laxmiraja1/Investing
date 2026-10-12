# Calibration trades

One folder per trade, e.g. `1988-ko-buy/`:

```
1988-ko-buy/
  packet/          # packet.yaml + docs, all published before as_of (see packets/example)
  truth.yaml       # what the investor actually did and why (copy truth.example.yaml)
  runs/            # written by shared.run_agent
  scores.csv       # written by shared.judge
  writeup.md       # your honest assessment: where it matched, where it diverged, why
```

Pick 3-5 trades: a well-known buy, a sell or trim, a pass or obscure position, and ideally an admitted mistake. Hold one or two back until the agent is frozen.
