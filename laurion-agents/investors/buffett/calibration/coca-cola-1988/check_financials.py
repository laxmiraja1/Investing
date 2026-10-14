"""Check that the OCR'd Coca-Cola statements add up.

  python investors/buffett/calibration/coca-cola-1988/check_financials.py

Figures ($ thousands) come from the OCR text layer of the two annual reports
(ocrmypdf --force-ocr, then pdftotext -layout). Every subtotal and total
printed in each statement is recomputed from its line items. A mismatch
means an OCR misread; the fix is checked against the page image and noted
in CORRECTIONS.

Sources:
  ar1988 = ko-annual-report-1988.pdf (ProQuest; chairman's letter signed 1989-02-18,
           auditor's report 1989-01-27): income statement p38, balance sheet
           p36-37. Text layer from ProQuest, no re-OCR. 1987 column restated
           (finance subsidiary consolidated).
  ar1987 = ko-annual-report-1987.pdf (ProQuest, dated 1988-02-18):
           income statement p40, balance sheet p38-39. 1986 column restated.
  ar1986 = ko-10k-1986.pdf (1986 annual report): income statement p46,
           balance sheet p44-45. As originally reported.
"""

CORRECTIONS = {
    ("ar1986", "bs", 1986, "current_maturities_ltd"):
        "OCR read '2212'; page image (PDF p45, printed p43) shows 23,212.",
    ("ar1988", "is", 1988, "revenue"):
        "text layer garbled ('*B Q17 eq-f'); page image (PDF p38, printed p36) shows 8,337,831.",
}

DATA = {
    "ar1988": {
        "is": {
            1988: dict(revenue=8_337_831, cogs=3_701_472, gross=4_636_359, sga=3_038_058, restructuring=0,
                       op_income=1_598_301, int_income=199_333, int_expense=230_513, equity_income=48_259,
                       other=-33_243, gain_subsidiary_stock=0, pretax=1_582_137, taxes=537_434,
                       cont_ops=1_044_703, disc_ops=0, disc_gain=0, net_income=1_044_703,
                       preferred_dividends=6_426, net_to_common=1_038_277, eps=2.85, avg_shares=364_612),
        },
        "bs": {
            1988: dict(cash=1_145_346, securities=85_844, receivables=627_248, fin_sub_receivables=156_728,
                       inventories=778_816, prepaid=451_450, notes_rec_cpe=0, current_assets=3_245_432,
                       inv_cce=733_295, inv_tcc=96_921, inv_cpe=598_059, inv_other=483_698, fin_sub_investments=167_689,
                       rec_other=309_897, investments=2_389_559, land=116_726, buildings=853_252,
                       machinery=1_645_652, containers=293_277, ppe_gross=2_908_907, depreciation=1_149_832,
                       ppe_net=1_759_075, goodwill=56_546, total_assets=7_450_612,
                       payables=1_080_970, loans_fin_sub=253_628, loans=1_000_896, current_maturities_ltd=108_915,
                       dividends_in_kind=0, accrued_taxes=424_488, current_liabilities=2_868_897,
                       ltd_fin_sub=41_584, ltd=719_475, other_liabilities=205_702, deferred_tax=269_652,
                       preferred=300_000, common=417_395, surplus=380_264, reinvested=4_385_142,
                       unearned_restricted=-51_467, fx=-17_010, equity_before_treasury=5_414_324,
                       treasury=2_069_022, equity=3_345_302, total_liabilities_equity=7_450_612),
            1987: dict(cash=1_383_560, securities=105_546, receivables=672_160, fin_sub_receivables=68_619,
                       inventories=776_740, prepaid=680_407, notes_rec_cpe=544_889, current_assets=4_231_921,
                       inv_cce=749_159, inv_tcc=84_493, inv_cpe=989_409, inv_other=395_004, fin_sub_investments=228_290,
                       rec_other=251_587, investments=2_697_942, land=112_741, buildings=763_317,
                       machinery=1_492_583, containers=275_120, ppe_gross=2_643_761, depreciation=1_042_233,
                       ppe_net=1_601_528, goodwill=74_155, total_assets=8_605_546,
                       payables=1_208_754, loans_fin_sub=186_578, loans=1_685_408, current_maturities_ltd=213_609,
                       dividends_in_kind=335_017, accrued_taxes=454_013, current_liabilities=4_083_379,
                       ltd_fin_sub=106_113, ltd=803_352, other_liabilities=208_328, deferred_tax=217_200,
                       preferred=0, common=415_977, surplus=338_594, reinvested=3_783_625,
                       unearned_restricted=-37_414, fx=-4_247, equity_before_treasury=4_496_535,
                       treasury=1_309_361, equity=3_187_174, total_liabilities_equity=8_605_546),
        },
    },
    "ar1987": {
        "is": {
            1987: dict(revenue=7_658_341, cogs=3_633_159, gross=4_025_182, sga=2_665_022, restructuring=36_370,
                       op_income=1_323_790, int_income=207_164, int_expense=279_012, equity_income=118_533,
                       other=34, gain_subsidiary_stock=39_654, pretax=1_410_163, taxes=494_027,
                       cont_ops=916_136, disc_ops=0, disc_gain=0, net_income=916_136, eps=2.43, avg_shares=377_372),
            1986: dict(revenue=6_976_558, cogs=3_453_891, gross=3_522_667, sga=2_445_602, restructuring=180_000,
                       op_income=897_065, int_income=139_348, int_expense=196_778, equity_income=155_804,
                       other=33_014, gain_subsidiary_stock=375_000, pretax=1_403_453, taxes=469_106,
                       cont_ops=934_347, disc_ops=0, disc_gain=0, net_income=934_347, eps=2.42, avg_shares=386_831),
            1985: dict(revenue=5_879_160, cogs=2_909_496, gross=2_969_664, sga=2_162_991, restructuring=0,
                       op_income=806_673, int_income=144_648, int_expense=189_808, equity_income=164_385,
                       other=66_524, gain_subsidiary_stock=0, pretax=992_422, taxes=314_856,
                       cont_ops=677_566, disc_ops=9_000, disc_gain=35_733, net_income=722_299, eps=1.84, avg_shares=393_354),
        },
        "bs": {
            1987: dict(cash=1_017_624, securities=450_640, receivables=672_160, inventories=776_740,
                       prepaid=674_148, notes_rec_cpe=544_889, current_assets=4_136_201,
                       inv_cpe=989_409, inv_cce=749_159, inv_tcc=84_493, inv_other=435_484, rec_other=289_000,
                       investments=2_547_545, land=112_741, buildings=763_317, machinery=1_488_464,
                       containers=275_120, ppe_gross=2_639_642, depreciation=1_041_983, ppe_net=1_597_659,
                       goodwill=74_155, total_assets=8_355_560,
                       payables=1_430_193, loans=1_685_408, current_maturities_ltd=213_609, dividends_in_kind=335_017,
                       accrued_taxes=454_313, current_liabilities=4_118_540, ltd=803_352, deferred_tax=209_880,
                       due_cpe=0, common=415_977, surplus=338_594, reinvested=3_783_625, fx=-5_047,
                       equity_before_treasury=4_533_149, treasury=1_309_361, equity=3_223_788,
                       total_liabilities_equity=8_355_560),
            1986: dict(cash=606_848, securities=261_785, receivables=672_568, inventories=695_437,
                       prepaid=932_630, notes_rec_cpe=0, current_assets=3_169_268,
                       inv_cpe=1_436_707, inv_cce=709_287, inv_tcc=87_696, inv_other=212_194, rec_other=217_046,
                       investments=2_662_930, land=98_842, buildings=695_029, machinery=1_390_689,
                       containers=287_672, ppe_gross=2_472_232, depreciation=934_679, ppe_net=1_537_553,
                       goodwill=114_377, total_assets=7_484_128,
                       payables=1_198_407, loans=697_743, current_maturities_ltd=4_628, dividends_in_kind=0,
                       accrued_taxes=344_141, current_liabilities=2_244_919, ltd=907_676, deferred_tax=239_813,
                       due_cpe=576_741, common=414_492, surplus=299_345, reinvested=3_624_046, fx=-118_087,
                       equity_before_treasury=4_219_796, treasury=704_817, equity=3_514_979,
                       total_liabilities_equity=7_484_128),
        },
    },
    "ar1986": {
        "is": {
            1986: dict(revenue=8_668_556, cogs=4_644_235, gross=4_024_321, sga=2_699_293, restructuring=180_000,
                       op_income=1_145_028, int_income=134_184, int_expense=185_769, equity_income=0,
                       other=42_837, gain_subsidiary_stock=375_000, pretax=1_511_280, taxes=576_933,
                       cont_ops=934_347, disc_ops=0, disc_gain=0, net_income=934_347, eps=2.42, avg_shares=386_831),
            1985: dict(revenue=7_212_093, cogs=3_859_612, gross=3_352_481, sga=2_367_853, restructuring=0,
                       op_income=984_628, int_income=150_683, int_expense=168_462, equity_income=0,
                       other=96_597, gain_subsidiary_stock=0, pretax=1_063_446, taxes=385_880,
                       cont_ops=677_566, disc_ops=9_000, disc_gain=35_733, net_income=722_299, eps=1.84, avg_shares=393_354),
        },
        "bs": {
            1986: dict(cash=625_899, securities=261_785, receivables=1_081_597, inventories=932_619,
                       prepaid=837_512, current_assets=3_739_412,
                       inv_cce=709_287, inv_other=387_155, film_costs=777_590, rec_other=337_213, investments=2_211_245,
                       land=137_233, buildings=765_482, machinery=1_565_305, containers=321_938, ppe_gross=2_789_958,
                       depreciation=1_026_230, ppe_net=1_763_728, goodwill=659_053, total_assets=8_373_438,
                       payables=1_332_714, loans=701_866, current_maturities_ltd=23_212, ent_obligations_current=257_333,
                       accrued_taxes=439_689, current_liabilities=2_754_814, ent_obligations=354_054, ltd=1_011_185,
                       deferred_tax=381_559, deferred_ent_revenue=356_847, common=414_492, surplus=299_345,
                       reinvested=3_624_046, fx=-118_087, equity_before_treasury=4_219_796, treasury=704_817,
                       equity=3_514_979, total_liabilities_equity=8_373_438),
            1985: dict(cash=499_624, securities=369_491, receivables=827_451, inventories=884_445,
                       prepaid=221_006, current_assets=2_802_017,
                       inv_cce=402_678, inv_other=384_898, film_costs=536_112, rec_other=444_436, investments=1_768_124,
                       land=127_565, buildings=674_131, machinery=1_405_835, containers=317_752, ppe_gross=2_525_283,
                       depreciation=893_846, ppe_net=1_631_437, goodwill=570_032, total_assets=6_771_610,
                       payables=1_056_415, loans=391_421, current_maturities_ltd=29_578, ent_obligations_current=215_249,
                       accrued_taxes=243_182, current_liabilities=1_935_845, ent_obligations=270_676, ltd=866_756,
                       deferred_tax=285_180, deferred_ent_revenue=434_096, common=69_227, surplus=602_617,
                       reinvested=3_092_255, fx=-181_440, equity_before_treasury=3_582_659, treasury=603_602,
                       equity=2_979_057, total_liabilities_equity=6_771_610),
        },
    },
}


def g(d, *keys):
    return sum(d.get(k, 0) for k in keys)


def income_checks(d):
    yield "gross = revenue - cogs", d["gross"], d["revenue"] - d["cogs"]
    yield "operating income", d["op_income"], d["gross"] - d["sga"] - d["restructuring"]
    yield "pretax income", d["pretax"], (d["op_income"] + d["int_income"] - d["int_expense"] + d["equity_income"]
                                         + d["other"] + d["gain_subsidiary_stock"])
    yield "continuing operations", d["cont_ops"], d["pretax"] - d["taxes"]
    yield "net income", d["net_income"], d["cont_ops"] + d["disc_ops"] + d["disc_gain"]
    to_common = d["net_income"] - d.get("preferred_dividends", 0)
    if "net_to_common" in d:
        yield "net income to common", d["net_to_common"], to_common
    yield "EPS (to the cent)", round(d["eps"] * 100), round(to_common / d["avg_shares"] * 100)


def balance_checks(d):
    yield "current assets", d["current_assets"], g(d, "cash", "securities", "receivables", "fin_sub_receivables",
                                                 "inventories", "prepaid", "notes_rec_cpe")
    yield "investments & other", d["investments"], g(d, "inv_cpe", "inv_cce", "inv_tcc", "inv_other",
                                                    "film_costs", "fin_sub_investments", "rec_other")
    yield "PP&E gross", d["ppe_gross"], g(d, "land", "buildings", "machinery", "containers")
    yield "PP&E net", d["ppe_net"], d["ppe_gross"] - d["depreciation"]
    yield "total assets", d["total_assets"], g(d, "current_assets", "investments", "ppe_net", "goodwill")
    yield "current liabilities", d["current_liabilities"], g(d, "payables", "loans_fin_sub", "loans",
                                                           "current_maturities_ltd", "dividends_in_kind",
                                                           "ent_obligations_current", "accrued_taxes")
    yield "equity before treasury", d["equity_before_treasury"], g(d, "preferred", "common", "surplus", "reinvested",
                                                                   "unearned_restricted", "fx")
    yield "shareholders' equity", d["equity"], d["equity_before_treasury"] - d["treasury"]
    yield "total liabilities & equity", d["total_liabilities_equity"], g(
        d, "current_liabilities", "ent_obligations", "ltd_fin_sub", "ltd", "other_liabilities", "deferred_tax",
        "deferred_ent_revenue", "due_cpe", "equity")
    yield "balance sheet balances", d["total_assets"], d["total_liabilities_equity"]


def main() -> int:
    failures = 0
    for src, stmts in DATA.items():
        for kind, years in stmts.items():
            checks = income_checks if kind == "is" else balance_checks
            for year, d in years.items():
                for name, printed, computed in checks(d):
                    ok = printed == computed
                    failures += not ok
                    print(f"{'ok  ' if ok else 'FAIL'} {src} {kind} {year} {name}: printed {printed:,} computed {computed:,}")
    for (src, kind, year, item), note in CORRECTIONS.items():
        print(f"corrected {src} {kind} {year} {item}: {note}")
    print(f"\n{failures} failure(s)")
    return failures


if __name__ == "__main__":
    raise SystemExit(main())
