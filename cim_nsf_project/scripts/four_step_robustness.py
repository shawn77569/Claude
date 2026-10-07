"""四步流程分類的穩健性檢查。從專案根目錄執行：python3 scripts/four_step_robustness.py

只用 data/derived/four_step_merged.csv，不需要國科會分類檔。
輸出：
1. 互斥分組的經費與件數占比（S1端／跨步驟 S1+S3／S3端／S2 主要／S4）
2. 跨步驟占比的逐件剔除（leave-one-out）範圍與組成計畫
3. 排除信心「低」、期間對齊（只看 2023–24）後的結果
4. bootstrap 95% 區間（按件重抽）
5. 美國 2023 年後：FuSe 計畫的貢獻；B1 經費占比排除 FuSe 後的變化
6. 摘要長度與跨步驟的關係；涉及 S1 的計畫中同時含 S3 的件數
"""
from pathlib import Path
import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DER = ROOT / "data" / "derived"


def load():
    a = pd.read_csv(DER / "four_step_merged.csv", encoding="utf-8-sig")
    sec = a.step_secondary.fillna("")
    a["s1"] = (a.step_primary == "S1") | (sec == "S1")
    a["s3"] = (a.step_primary == "S3") | (sec == "S3")
    a["s2"] = (a.step_primary == "S2") | (sec == "S2")
    a["g"] = np.select(
        [a.s1 & a.s3, a.step_primary == "S2", a.s1, a.step_primary == "S4"],
        ["跨步驟", "S2主要", "S1端", "S4"], default="S3端")
    a["one"] = 1
    a["fuse"] = (a.ctry == "US") & a.project_title.str.contains("FuSe")
    a["alen"] = np.where(a.ctry == "US", a.abstract_en.fillna("").str.len(),
                         a.abstract_zh_plan.fillna("").str.len())
    return a


def shares(d, col="bud"):
    return d.groupby(["ctry", "per"]).apply(
        lambda x: (x.groupby("g")[col].sum() / x[col].sum() * 100).round()).unstack().fillna(0)


def cross_share(x):
    return x[x.g == "跨步驟"].bud.sum() / x.bud.sum() * 100


def main():
    a = load()
    print("== 1. 互斥分組：經費占比（%）")
    print(shares(a))
    print("== 1. 互斥分組：件數占比（%）")
    print(shares(a, "one"))
    print(pd.crosstab([a.ctry, a.per], a.g))

    print("\n== 2. 跨步驟經費占比：逐件剔除範圍")
    for (c, p), x in a.groupby(["ctry", "per"]):
        loo = [(cross_share(x.drop(i)), x.loc[i, "cid"]) for i in x.index]
        xs = x[x.g == "跨步驟"].sort_values("bud", ascending=False)
        print(c, p, "原值 %.0f" % cross_share(x),
              "最低 %.0f（剔除 %s）最高 %.0f（剔除 %s）" % (*min(loo), *max(loo)))
        print("   組成：", [(r.cid, int(r.bud / 1e3), r.confidence) for r in xs.itertuples()])

    print("\n== 3a. 排除信心「低」")
    print(shares(a[a.confidence != "低"]))
    print("== 3b. 期間對齊：只看 2023–24（台灣 2023+ 含 2025 年 11 件，美國只有 1 件）")
    c = a[a.year.between(2023, 2024)]
    print(c.groupby("ctry").apply(
        lambda x: (x.groupby("g").bud.sum() / x.bud.sum() * 100).round()).unstack().fillna(0))

    print("\n== 4. bootstrap 95% 區間（經費占比，5000 次）")
    rng = np.random.default_rng(0)
    for (cc, p), x in a.groupby(["ctry", "per"]):
        b, xc, x1 = x.bud.values, (x.g == "跨步驟").values, x.s1.values
        cs, s1 = [], []
        for _ in range(5000):
            i = rng.integers(0, len(x), len(x))
            t = b[i].sum()
            cs.append(b[i][xc[i]].sum() / t)
            s1.append(b[i][x1[i]].sum() / t)
        print(cc, p, "跨步驟 %.0f [%.0f, %.0f]" % (cross_share(x), *np.percentile(cs, [2.5, 97.5]) * 100),
              " 涉及S1 %.0f [%.0f, %.0f]" % (x[x.s1].bud.sum() / x.bud.sum() * 100,
                                             *np.percentile(s1, [2.5, 97.5]) * 100))

    print("\n== 5. 美國 2023+：FuSe 的貢獻")
    u = a[(a.ctry == "US") & (a.per == "23+")]
    nf = u[~u.fuse]
    print("FuSe 件數", int(u.fuse.sum()), "占經費 %.0f%%" % (u[u.fuse].bud.sum() / u.bud.sum() * 100),
          "占跨步驟經費 %.0f%%" % (u[u.fuse & (u.g == "跨步驟")].bud.sum() / u[u.g == "跨步驟"].bud.sum() * 100))
    print("排除 FuSe：跨步驟 %.0f%%，涉及S1 %.0f%%" % (cross_share(nf), nf[nf.s1].bud.sum() / nf.bud.sum() * 100))
    for p, x in a[a.ctry == "US"].groupby("per"):
        y = x[~x.fuse]
        print("US", p, "B1 經費占比 %.0f%%，排除 FuSe %.0f%%" % (
            x[x.B_layer_primary == "B1"].bud.sum() / x.bud.sum() * 100,
            y[y.B_layer_primary == "B1"].bud.sum() / y.bud.sum() * 100))

    print("\n== 6. 摘要長度（各國內三分位）與跨步驟件數")
    for cc, x in a.groupby("ctry"):
        x = x.assign(q=pd.qcut(x.alen, 3, labels=["短", "中", "長"]))
        print(cc, {k: f"n={len(y)} 跨步驟={(y.g == '跨步驟').sum()} 長度中位數={int(y.alen.median())}"
                   for k, y in x.groupby("q", observed=True)})
    print("涉及 S1 的計畫中同時含 S3（件數）")
    print(a[a.s1].groupby(["ctry", "per"]).apply(lambda y: f"{y.s3.sum()}/{len(y)}"))


if __name__ == "__main__":
    pd.set_option("display.width", 200)
    main()
