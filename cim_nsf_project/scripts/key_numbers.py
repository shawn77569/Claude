"""重現本專案的關鍵數字。從專案根目錄執行：python3 scripts/key_numbers.py

輸出：
1. 台美 CIM 計畫的經費結構（件數、總額、中位數、集中度）
2. 研究層次（B_layer_primary）各期經費占比
3. 記憶體路線 × 研究層次
4. 四步流程分類（主要步驟、跨步驟、S2、S3 是否下線、製造位置）
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
DER = ROOT / "data" / "derived"


def load():
    g = pd.read_csv(RAW / "grb_integrated_v2_0_333_20260618.csv")
    c = pd.read_csv(DER / "GRB國科會CIM計畫分類_台美鏡像分析.csv")
    a5 = g[(g.A_tech_route == "A5") & (g.funding_agency == "NSTC")].copy()
    a5["key"] = a5.PI.str.strip() + "|" + a5.project_title.str.strip()
    c["key"] = c["主持人"].str.strip() + "|" + c["計畫名稱"].str.strip()
    m = a5.merge(c, on="key", how="inner")
    tw = m[m["納入分析"] == "是"].copy().reset_index(drop=True)
    tw["bud"] = tw.budget_usd_nominal
    tw["year"] = tw["起始年"]
    tw["route"] = tw["記憶體類型"]
    n = pd.read_csv(RAW / "nsf_cim_annotated_v1_1.csv")
    us = n[(n.sample_status == "保留") & (n.dup_role == "primary")].copy().reset_index(drop=True)
    us["bud"] = us.budget_usd_corrected
    us["year"] = us.year_start
    us["route"] = us.device_route
    return tw, us


def funding_structure(tw, us):
    print("== 1. 經費結構（名目美元）")
    for name, d in [("TW", tw), ("US", us)]:
        b = d.bud
        print(name, "n", len(d), "total_M", round(b.sum() / 1e6, 2),
              "median_K", round(b.median() / 1e3), "<100K", round((b < 1e5).mean(), 2),
              "top10_share", round(b.nlargest(10).sum() / b.sum(), 2))


def layer_shares(tw, us):
    print("== 2. 研究層次經費占比（B1 元件；B2+B3 電路與架構）")
    for name, d in [("TW", tw), ("US", us)]:
        for lab, x in [("2018-22", d[d.year <= 2022]), ("2023+", d[d.year >= 2023])]:
            b = x.bud.sum()
            print(name, lab, "n", len(x),
                  "B1", round(x[x.B_layer_primary == "B1"].bud.sum() / b * 100),
                  "B2+B3", round(x[x.B_layer_primary.isin(["B2", "B3"])].bud.sum() / b * 100))


def route_layer(tw, us):
    print("== 3. 路線 × 元件層經費占比")
    for name, d in [("TW", tw), ("US", us)]:
        d = d.copy()
        d["dev"] = d.B_layer_primary == "B1"
        out = d.groupby("route").apply(lambda x: pd.Series({
            "n": len(x), "bud_M": round(x.bud.sum() / 1e6, 2),
            "dev_bud_share": round(x[x.dev].bud.sum() / x.bud.sum(), 2),
            "median_K": round(x.bud.median() / 1e3)}))
        print(name)
        print(out)


def four_step():
    print("== 4. 四步流程（依 method/codebook_four_step.md 分類）")
    a = pd.read_csv(DER / "four_step_merged.csv", encoding="utf-8-sig")
    a["s1_any"] = (a.step_primary == "S1") | (a.step_secondary == "S1")
    a["s3_any"] = (a.step_primary == "S3") | (a.step_secondary == "S3")
    a["s2_any"] = (a.step_primary == "S2") | (a.step_secondary == "S2")

    def pct(x, mask):
        return round(x[mask].bud.sum() / x.bud.sum() * 100)

    for c in ["US", "TW"]:
        for p in ["18-22", "23+"]:
            x = a[(a.ctry == c) & (a.per == p)]
            print(c, p, "n", len(x),
                  "S1only", pct(x, (x.step_primary == "S1") & (x.step_secondary != "S3")),
                  "S1+S3", pct(x, x.s1_any & x.s3_any),
                  "S3only", pct(x, (x.step_primary == "S3") & (~x.s1_any) & (x.step_secondary != "S2")),
                  "S2any", pct(x, x.s2_any), "S1any", pct(x, x.s1_any))
    print(pd.crosstab(a.ctry, a.step_primary))
    print(pd.crosstab(a.ctry, a.locus))


if __name__ == "__main__":
    pd.set_option("display.width", 200)
    tw, us = load()
    funding_structure(tw, us)
    layer_shares(tw, us)
    route_layer(tw, us)
    four_step()
