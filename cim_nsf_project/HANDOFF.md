# 交接文件：CIM 研究論證的目前狀態

更新：2026/10/8。這份文件讓新的工作環境能直接接續，不必重讀先前的對話。
標記方式：〔事實〕有資料或來源；〔研判〕推論；〔待查〕尚未證實。

閱讀順序建議：本文件 → `CLAUDE.md` → 需要原話或細節時查 `notes/conversation_log.md`（含先前工作階段的壓縮摘要、本階段全部對話與四份研究助理查核報告）。

本包未收錄的東西（需要時請另外補）：
- 研討會最終版簡報 PDF（在 Claude Design 中，請匯出後放進 `deck/`）。
- 更早工作階段的逐字對話：只有壓縮摘要（在 `notes/conversation_log.md` 開頭）。設計細節的反覆修改（配色、字級、版型）只留下結論，`deck/03_設計說明與Design指令.md` 是最初版本，不是最終設計。

---

## 一、專案與目標

- 題目：美國AI晶片NSF科研投資趨勢觀察：聚焦記憶體內運算（CIM）。
- 報告人：曾昱翔（CIER 國際所）。研討會 2026/10/8，15 分鐘。簡報已在 Claude Design 定稿，研討會版本不再修改。
- 現階段目標：以「能做到的最好呈現」為準，重新整理論證，供後續報告或改版使用。
- 論證的出發點：以美國 NSF 的投資為觀察起點，推演對台灣的意涵。結論回答「美國這樣投資，台灣該怎麼因應」，不是一份完整的台灣 CIM 總體戰略。

## 二、論證主軸（目前版本）

### 1. 四步流程（理解框架，使用者認為最有助理解）
一顆 CIM 晶片從無到有：
1. 發明新元件（大學實驗室；對應研究層次的「材料與元件」）
2. 製程整合（晶圓廠或試產線；即「銜接」；嵌入式記憶體多做在後段製程）
3. 電路與晶片設計（設計後下線；對應「電路與架構」）
4. 量產（企業）

關鍵前提：第三步要等第二步完成才做得到。台積電已替 RRAM、MRAM 完成第二步〔事實〕；鐵電尚無對外製程〔事實〕。

### 2. 路線分類（兩層，加一個非路線類別）
| 層級 | 類別 | NSF 件數 | NSF 經費占比 | 角色 |
|---|---|---|---|---|
| 第一層 | SRAM | 2 | 2% | 對照 |
| | 快閃 | 3 | 4% | 對照 |
| | DRAM | 3 | 6% | 對照（產業主導） |
| | 新型非揮發記憶體 | 37 | 61% | 主軸 |
| 第二層 | 鐵電 | 12 | 26% | 主軸，台灣最該補的缺口 |
| | 電阻式 | 17 | 21% | 主軸，第二步已完成 |
| | 磁性 | 8 | 14% | 主軸，第二步已完成，ACED Fab 為實例 |
| 非路線 | 不綁定特定記憶體 | 13 | 24% | 必須交代（架構、工具、軟體） |
| | CMOS 類比記憶電路 | 2 | 4% | 註腳 |
來源：`deck/02_圖表數據.xlsx` 工作表 C07、C03。NSF 60 件，合計 4,224 萬美元。
注意：簡報第 9 頁（C03）與核心頁（C07）用了兩套分類，數字對得上（成熟製程 10 件＝SRAM 2＋快閃 3＋DRAM 3＋CMOS 類比 2），但應統一為上表的兩層分類。

### 3. A 與 B 兩種分法的結合
- A＝記憶體類型（資料呈現方式，和核心頁、NSF 編碼一致）。
- B＝記憶體在哪種製程製造：嵌入式（邏輯製程，第二步由晶圓代工完成，台灣的地盤）／獨立式（DRAM、NAND、獨立式鐵電，第二步由記憶體大廠完成）。
- 用法〔研判〕：A 做描述，B 當解釋變數（解釋台灣為何在某些路線有位置）。不要把 B 當成預先劃好的格子，以免被質疑循環論證。

### 4. 三層論證
1. 美國端：NSF AI 晶片經費 2023 年高峰；CIM 成長最快；經費往材料元件移動；增量約八成流向未規劃做出實體晶片的研究；核心發現「投入與量產方向相反」（SRAM 2%、新型非揮發 61%）；成因〔研判〕為資助者分工（私人資本、DARPA、SRC、NSF 最前端）；研究到量產多需 5 年以上。
2. 台美對照（國科會 62 件 vs NSF 60 件）：已從「平行對照」改寫為「同一方向，不同位置」。見第三節。
3. 台灣定位：見第四節。

## 三、台美對照的主要發現

### 1. 研究層次的經費占比〔事實，依 B_layer_primary〕
| | 2018–22 元件 | 2018–22 電路＋架構 | 2023+ 元件 | 2023+ 電路＋架構 |
|---|---|---|---|---|
| 美國 | 35% | 38% | 58% | 11% |
| 台灣 | 32% | 47% | 36% | 62% |
- 修正：簡報原說「台灣元件研究下降（56%→40%）」是按件數。按經費台灣持平，是美國加碼。「被反超」改為「往不同層移動」。
- 敏感度：拿掉經費最大的兩件磁性計畫（台大吳安宇，合計約 360 萬美元），台灣電路＋架構仍占 44%，美國全期 24%。

### 2. 路線差異〔事實〕
- 磁性：台灣 8 件 733 萬美元（占台灣 CIM 經費 31%，最大路線），元件層僅 17%；美國 8 件 591 萬，元件層 88%。
- 鐵電：台灣 14 件 237 萬（10%），單件中位數約 9 萬；美國 12 件 1,099 萬（26%），中位數約 76 萬。台灣幾乎沒有電路或晶片層級的鐵電計畫。
- 鐵電元件形式（手動初判，依標題與短摘要）：台灣偏鐵電穿隧接面（4 件，美國 0）、鰭式或環繞閘極鐵電電晶體、多晶矽鐵電薄膜電晶體；美國 2023 年後偏二維鐵電、氧化物通道、後段製程鐵電電容、鐵電 NAND。台積電 IEDM 2024 的氧化物通道鐵電電晶體較接近美國方向〔研判〕。

### 3. 經費結構〔事實〕
| | 單件中位數 | <10 萬美元 | 前 10 大占比 |
|---|---|---|---|
| 台灣 | 10.7 萬 | 48% | 64% |
| 美國 | 59.1 萬 | 0% | 34% |

### 4. 公共資金的管道〔事實〕
- 台灣：國研院（NDL／TSRI）研究人員主持 4 件 CIM 元件與 3D 整合計畫。
- 美國：4 件 SBIR／STTR 新創計畫。
- ACED Fab 合作案兩端都在資料中：美方 Stanford（NSF 2314591，新型 MRAM 元件；論文共同作者含台積電、工研院、陽明交大）；台方台大劉致為（MRAM 記憶體內運算晶片，美方夥伴 Stanford，國研院參與）。

### 5. 解釋機制〔研判，待更多證據〕
「台灣已有某種記憶體的量產製程，公共研究才會往整合端配置，美台分工才會形成。」
- 磁性、電阻式：台積電有量產製程 → 台灣有整合型計畫 → 分工已形成。
- 鐵電：沒有製程 → 只有小額元件計畫 → 分工尚未形成。
- 替代解釋：台灣學界本來就擅長電路設計。目前的路線差異較支持前者，但每條路線只有 8–17 件。

## 四、四步流程分類結果（2026/10/7 新完成，尚未和使用者討論）

方法：`method/codebook_four_step.md`。同一位分類者處理 122 件，依摘要的規劃內容判斷主要步驟與次要步驟，另標 S3 是否規劃下線、記憶體製造位置。結果在 `data/derived/four_step_*.csv`。和 B_layer 的對應一致率 80%；主要差異是 17 件元件層計畫因屬跨層協同設計而被判為 S3 主要、S1 次要。信心「低」：台灣 12 件、美國 4 件。

| 經費占比 | 只做 S1 | S1＋S3 跨步驟 | 只做 S3 | 有 S2 | 任何涉及 S1 |
|---|---|---|---|---|---|
| 美國 2018–22 | 0% | 33% | 64% | 0% | 33% |
| 美國 2023+ | 9% | 46% | 37% | 8% | 55% |
| 台灣 2018–22 | 11% | 42% | 43% | 7% | 54% |
| 台灣 2023+ | 26% | 10% | 64% | 2% | 36% |

初步解讀〔研判，需和使用者確認後再定〕：
- 「美國押第一步、台灣押第三步」需要修正得更精確：2023 年後，美國近半經費投在「新元件＋電路架構」的跨步驟協同設計計畫；台灣把元件和電路架構分開資助，跨步驟計畫只占一成。
- 涉及元件的經費：美國 55%、台灣 36%（2023+），方向和 B_layer 結果一致。
- 第二步（製程整合）兩邊都很少。台灣的 S2 計畫 4 件全在 NDL／TSRI，且都在 2018–2021；2023 年後台灣幾乎沒有。研判：國研院 12 吋研究場域（2025–2028）與工研院試產線（2028）可能是恢復這一塊的機會。
- 使用者原先猜「台灣更能做試產驗證」：S2 件數台灣較多（4 對 1），但經費占比相當，且 2023 年後消失，不足以支持。
- 製造位置（B）：鐵電計畫多數無法從摘要判斷（台灣 14 件中 10 件不明、美國 12 件中 6 件不明）。先前「NSF 鐵電以嵌入式為主」的標題初判無法確認，需讀論文全文。

## 五、台灣定位（目前版本）〔研判〕

一句話：NSF 押注第一步的新元件；台灣的優勢在第二、三步。對做在邏輯製程裡的新興記憶體，台灣應把第二步做成多路線平台——RRAM、MRAM 已經做到，嵌入式鐵電是最該補的缺口。成熟路線由產業主導，公共資源以擴散為主。

- 主體：嵌入式新興記憶體的第二步平台（多路線，參考歐洲 FAMES；依 Teece 互補資產理論，路線未收斂前價值在能低成本嘗試多條路線的地方）。
- 優先順序：1 嵌入式鐵電的第二步（試產線納入鐵電模組）；2 深化 RRAM／MRAM 承接（擴大 ACED Fab 類合作、開放國際學研取用）；3 研究端集中並對齊（鐵電研究整併為元件到陣列的大型計畫，對齊後段製程與氧化物通道方向）；4 介面與標準（降為觀察訊號）；5 第三步擴散（缺證據）。
- 不建議：在第一步和 NSF 比材料廣度；在 DRAM-PIM 標準品正面競爭；用公共經費培養 SRAM-CIM 國家隊晶片公司。
- DRAM：不是主軸，只當核心頁的對照列與問答準備。台灣 DRAM 能力分四層：先進通用 DRAM 製程（弱，台灣三家合計約 2.4% 營收）、製造地（美光在台投資逾 1.6 兆元，技術屬美光）、客製化 DRAM 與邏輯 3D 堆疊（愛普 VHM 2021 年量產，力積電、華邦、南亞科試產或展示）、介面（台積電 HBM 底層邏輯晶粒）。
- 檢驗「有能力承接」的五個條件：需求、專屬能力、相對位置、可及性、吸收能力。RRAM、MRAM 五項都過；鐵電、氧化物、二維只到「具備基礎」。

## 六、已確認的重要事實（附來源）

台灣與產業
- 台積電 RRAM：40、28、22 奈米量產；N12e 2025 年通過消費級驗證；6 奈米開發中。MRAM：16 奈米車用 2025 年通過驗證，12 奈米車用、5 奈米高速開發中。大學 shuttle 2025 年擴及 7 奈米。https://investor.tsmc.com/static/annualReports/2025/english/pdf/2025_tsmc_ar_e_ch5.pdf
- 台積電 IEDM 2024：氧化物通道鐵電電晶體（0.009μm²）、鎢摻雜氧化銦電晶體、二維材料堆疊通道。https://research.tsmc.com/chinese/collaborations/events/IEDM2024.html
- 工研院與台積電 SOT-MRAM 陣列晶片，適用記憶體內運算（IEDM 2023，中央社 2024/1/17）。https://www.cna.com.tw/news/ait/202401170041.aspx
- 工研院 12 吋試產線：約 37.72 億元，建物 2027/12 完工，2028Q1 起陸續啟用，28–90 奈米後段製程研發與試產服務。https://www.ctee.com.tw/news/20260211700066-439901 ；範疇含下世代記憶體與整合型 3D 架構，台積電捐設備：https://technews.tw/?p=1512042
- 國研院 12 吋研究場域：2025–2028，79.76 億元。https://www.ctee.com.tw/news/20250205700100-439901
- ACED Fab 台方 6 件（台大 4 件）：https://cdnfinance.technews.tw/2023/06/30/aced-fab-program-6/ ；台大劉致為 MRAM CIM 晶片（夥伴 Stanford、國研院）：https://www.ntu.edu.tw/spotlight/2023/2175_20230727.html
- ACED Fab 資助的 64kb SOT-MRAM（NSF 2314591），共同作者含台積電、工研院、陽明交大：https://www.nature.com/articles/s41928-025-01434-x
- 晶創台灣方案 3,000 億元（2024–2033）：https://www.cna.com.tw/news/ait/202401110164.aspx ；115 年度晶創計畫徵求未見記憶體或 CIM。
- 聯發科天璣 9500「首款支援整合式記憶體內運算架構」的 NPU（新聞稿未寫 SRAM）：https://www.prnewswire.com/news-releases/mediatek-dimensity-9500-unleashes-best-in-class-performance-ai-experiences-and-power-efficiency-for-the-next-generation-of-mobile-devices-302562586.html
- d-Matrix Corsair 台積電 6 奈米：https://www.servethehome.com/d-matrix-presents-corsair-an-in-memory-computing-architecture-for-inference-at-hot-chips-2025/ ；Raptor 邏輯晶粒 N4、3D DRAM 與封裝由世芯：https://www.d-matrix.ai/?p=2109 、https://hwbusters.com/news/d-matrix-raptor-drops-the-memory-phy-32gb-at-100-tb-s-against-hbm4s-192gb-at-18/
- Axelera Metis 台積電 12 奈米：https://www.eenewseurope.com/en/axelera-launches-metis-in-memory-computing-ai-edge-cards/
- 台積電 ISSCC 2024 3 奈米全數位 CIM macro（晶圓廠標準 6T SRAM）：https://dblp1.uni-trier.de/pers/hj86/c/Chih:Yu=Der

DRAM 與 PIM
- Samsung LPDDR5X-PIM（Hot Chips 2026）：https://www.sammyfans.com/2026/08/25/samsung-unveils-lpddr5x-pim-dram/ ；GAIA 最快 2027 量產（據報導）：https://www.trendforce.com/news/2026/08/26/news-samsungs-4nm-gaia-could-mark-first-pim-commercialization-in-ai-pcs-mass-production-as-early-as-2027/
- JEDEC LPDDR6-PIM 接近完成：https://www.hpcwire.com/off-the-wire/jedec-previews-lpddr6-roadmap-expanding-lpddr-into-data-centers-and-processing-in-memory/
- SK hynix HBM4 用台積電 12 奈米 base die：https://digitimes.com/news/a20260424VL208/sk-hynix-tsmc-hbm4-dram.html ；C-HBM4E N3P：https://www.trendforce.com/news/2025/12/01/news-tsmc-unveils-custom-c-hbm4e-details-n3p-logic-dies-reportedly-target-2x-efficiency-gain/ ；美光 HBM4E 交台積電：https://www.tomshardware.com/micron-hands-tsmc-the-keys-to-hbm4e ；Samsung 自製 4 奈米：https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4
- 2Q26 DRAM 市占：https://www.trendforce.com/presscenter/news/20260907-13219.html
- 美光在台投資：https://focustaiwan.tw/business/202610010013
- 愛普 VHM 量產（2021）：https://tw.stock.yahoo.com/news/%E6%84%9B%E6%99%AE%E6%94%9C%E6%89%8B%E5%8A%9B%E7%A9%8D%E9%9B%BB-%E5%8F%B0%E7%A9%8D%E9%9B%BB-%E5%AE%8C%E6%88%90vhmtm%E9%87%8F%E7%94%A2-%E5%AE%A2%E6%88%B6%E7%82%BA%E9%AF%A8%E9%8F%88%E7%A7%91%E6%8A%80-064955926.html

歐洲與美國的整合平台
- CEA-Leti 嵌入式 FeRAM（22 奈米 FD-SOI 後段）：https://www.eejournal.com/industry_news/cea-leti-demonstrates-embedded-feram-platform-compatible-with-22nm-fd-soi-node/
- FAMES 試產線（8.3 億歐元，含 OxRAM、FeRAM、MRAM、FeFET 模組）：https://www.cea.fr/cea-tech/leti/english/Pages/What's-On/Press%20release/cea-leti-announceslaunch-of-FAMES-pilot-line-as-part-of-EU-chips-act-initiative.aspx
- imec NanoIC（25 億歐元，2026/2 啟用）：https://evertiq.com/design/2026-02-09-eu-launches-nanoic-europes-largest-chips-act-pilot-line
- Fraunhofer 與 GF 22FDX 鐵電記憶體：https://www.ipms.fraunhofer.de/en/press-media/press/2026/Ferroelectric-memory-storage.html
- 鐵電業界現況（Semiecosystem 2026/2）：https://marklapedus.substack.com/p/next-gen-ferroelectric-memory-still
- AIP（2025/11）：Natcast 經費收回後，NSTC 三座設施受影響，Albany 聯邦經費前景不明，加州與亞利桑那不再推進：https://www.aip.org/fyi/trump-administration-overhauls-chips-r-d-plans

論文追查（NSF 計畫晶片製作地點，詳見 `data/derived/NSF_CIM計畫晶片製作地點追查.csv`）
- 可確認製作地點的 5 個團隊：台積電 4（Georgia Tech、ASU／JHU、Purdue、USC）、Albany 2（ASU／JHU、SUNY）。
- 只看新興記憶體 CIM 晶片：台積電 2、Albany 2；只算致謝 NSF 的：1 比 1。
- NSF 2023–24 新元件計畫 11 件：0 件自研元件進入晶圓廠。
- 定義參考：Mutlu 等人 PIM 兩種做法 https://arxiv.org/abs/2012.03112

## 七、已修正的錯誤（不要再犯）
1. 「聯發科已量產 SRAM-CIM」→ 新聞稿只寫 CIM 架構，未寫 SRAM。
2. 「德國 FMC 8Gb 送樣」→ 來源不足，不使用。
3. 「Albany 2025/7 啟用 NSTC EUV 加速器」→ 後續 Natcast 經費收回，Albany 聯邦經費前景不明。
4. 「ACED Fab 台方 6 件都是電路與系統」→ 台大劉致為為 MRAM CIM 晶片。
5. 「5 個團隊中 4 個用台積電」放在新興記憶體脈絡會誤導 → 新興記憶體 CIM 晶片是台積電與 Albany 各半。
6. 「台灣元件研究下降、被反超」→ 按經費持平，是美國加碼。
7. 「鐵電台灣件數多於美國」→ 經費只有美國的約 1/5，中位數差約 8 倍。
8. 比較兩個期間不同長度時，必須用年均值，不能用期間總額。
9. 「台灣碰不到 DRAM 本身」→ 台灣有客製化 DRAM 與 3D 堆疊實績。
10. 「成熟 CIM／PIM／新興 CIM」三分法混用兩種標準 → 改用第二節的兩層分類。

## 八、待辦與未決問題
- 和使用者討論四步流程分類結果（第四節），決定主圖用 B_layer 還是四步分類，或兩者並列。
- 鐵電與快閃計畫的嵌入式或獨立式分類：摘要不足，需讀論文全文。
- 檢驗替代解釋（台灣學界本來擅長電路）：可用歷年 ISSCC 台灣論文或其他路線資料。
- 第三步擴散的證據：中小 IC 設計公司能否取得 CIM 設計模組；台積電是否對外提供 DCIM IP（目前未找到）。
- 台積電嵌入式 RRAM／MRAM 是否開放學界與新創透過 MPW 使用〔待查〕。
- 工研院試產線是否納入鐵電模組〔待查〕；ACED Fab 2025–2026 進度〔待查〕。
- 若改版簡報：統一分類（第二節）；把四步流程做成主軸圖，各章標亮不同步驟；第二層改寫為「同一方向，不同位置」；「PIM 標準參與」降為觀察訊號；結語可改為「NSF 的 CIM 經費集中在距離量產最遠的研發階段；這些技術走向量產時的銜接位置尚未確定，台灣具備基礎，或可提早參與」。
- 講稿（`deck/講稿_美國AI晶片NSF科研投資趨勢觀察.html`）的第三、四章尚未依重組版本改寫；已發布的 Artifact：https://claude.ai/artifact/AjXNPrEJo5uk14h8LM2hih

## 九、先前工作階段的其他重要內容

### 1. 美國端的其他數字〔事實，來源見 `deck/02_圖表數據.xlsx` 與內容稿〕
- NSF AI 晶片經費 2023 年高峰約 6 千萬美元，為前五年平均的 2.2 倍。
- 增量去向（C06，年均萬美元）：規劃做出實體晶片 194→332；尚未做出實體晶片 209→748；增量約八成流向後者（依摘要判讀規劃，非成果）。
- 路線年均（C04，萬美元，2018–22→2023–24）：鐵電 74→364、磁性 27→237、電阻式 103→180、成熟製程記憶體 62→146、不綁定 126→152。鐵電＋磁性約占年均增量 74%，電阻式約 11%。
- 資助者分工：d-Matrix 募資約 4.5 億美元；DARPA OPTIMA 7,800 萬美元（現有製程）；SRC PRISM 5,050 萬美元；NSF CIM 八年約 4,224 萬美元，商業化導向計畫約 7%。「分工」本身是研判，替代解釋包括 NSF 的基礎研究使命、FuSe 等計畫的設計。
- 研究到量產時程案例：知存從成立到量產約 5 年；三星 PIM 2021 年概念驗證，手機用產品預計 2026–27 年量產；TetraMem 創辦人研究曾獲 NSF 資助，台積電 22 奈米，2026 年初步矽驗證。

### 2. 台美鏡像分析的原始數字（按件數）〔事實〕
| 指標 | 台灣（國科會 62 件） | 美國（NSF 60 件） |
|---|---|---|
| CIM 占 AI 晶片計畫比重 2018–20／21–22／23–24 | 20%／43%／26% | 16%／21%／25% |
| 元件層（B1）比重 2018–22→2023–24 | 56%→40%（2025 年 45%） | 37%→55%（按經費 37%→61%） |
| 新興記憶體比重 | 約 60% | 約 62% |
| 每年 CIM 計畫數 | 持平 | 增為 2.4 倍 |
- 注意：第三節按經費、以「2023 年後」計算的結果（台灣元件層持平 32%→36%）才是較準確的說法；按件數的「台灣下降」不再使用。
- 摘要提到晶圓廠：NSF 74 件中 5 件、國科會 86 件中 10 件；摘要長度差異大，無法做量化比較。
- 已推翻：「台灣研究較分散」（兩邊都分散在約 28 個機構）。

### 3. 簡報狀態
- 研討會版本頁序（依講稿）：封面、目錄、研究方法、01 章（經費高峰、CIM 成長最快）、02 章（資料搬運瓶頸、CIM 已進入產品、路線未收斂、新興記憶體潛力、鐵電與磁性增幅最大、往材料元件移動、三個重點方向）、03 章（然而增量八成未規劃晶片、核心頁、研究到量產 5 年以上、成因：資助者分工）、04 章（台灣較早投入、兩地都押新興記憶體、台灣能力與三個著力點、啟示、三個觀察訊號）、結語、封底。
- 曾提出的 25 頁重組版：p16 然而；p17 核心頁；p18 成因；p19 銜接段；p20 章節頁；p21 台灣三段基礎；p22 研究端；p23 三個著力點（研究端／銜接端／量產端 × 依據／啟示／觀察訊號）；p24 結語；p25 封底。是否已套用於 Design 不確定。
- p19／p21／p23 的 Design 指令草稿與後續修正（方案 A：只改措辭；方案 B：第 21 頁依路線呈現），原文在 `notes/conversation_log.md`。注意：當時建議的第 21 頁本頁要點「NSF CIM 團隊的晶片多在台積電製作」已撤回，不要使用。
- 講稿中的 opt 句、停頓標記與問答段落在 `deck/講稿_美國AI晶片NSF科研投資趨勢觀察.html`。

### 4. 問答準備（重點題）
- 「學界在台積電下線很正常，能代表什麼？」→ 只主張晶片驗證這一步經過台灣；NSF 的新元件還沒走到這一步，下一代由誰承接還沒定。
- 「可確認製作地點的只有 5 個團隊，樣本太小？」→ 同意，所以只用「可確認者」的說法。
- 「美國不是有自己的研究晶圓廠？」→ 有，Albany；但 Natcast 經費收回後聯邦經費前景不明。
- 「鐵電是 NSF 增幅最大的路線，銜接的是德國 GF，台灣優勢在哪？」→ 台灣的實績在 RRAM、MRAM；鐵電是尚未確定、需要著力的部分。
- 「PIM 不就是 CIM 的一種嗎？」→ 本報告依記憶體類型區分 CIM 路線；三星稱為 PIM 的 DRAM 產品，在此歸為 DRAM 路線。文獻定義見 Mutlu 等人。
- 「資助者分工有直接證據嗎？」→ 研判，並說明替代解釋。
- 「台灣在 DRAM 有什麼能力？」→ 第五節的四層說明。

### 5. 用到的理論
- Teece（1986）互補資產：路線未收斂前，價值在能低成本嘗試多條路線的地方；主流設計出現後，轉到擁有專屬製造資產的一方。
- Cohen & Levinthal（1990）吸收能力：承接別人的研究，需要自己的研究基礎。

## 十、檔案索引
- `notes/conversation_log.md`：先前工作階段的壓縮摘要＋本階段全部對話＋四份研究助理查核報告（成熟 CIM、PIM、新興記憶體整合能力、四步分類）。工具輸出未收錄。
- `figures/four_step_pipeline.svg`：四步流程圖（可獨立開啟的版本）。
- `CLAUDE.md`：專案規範與使用者偏好。
- `data/raw/`：NSF 標註檔（60 件主樣本，含 device_route、maturity、process_compat、B_layer）、NSF 整合檔（361 件）、GRB 整合檔（333 件，含經費與摘要）、export.xlsx。
- `data/derived/GRB國科會CIM計畫分類_台美鏡像分析.csv`：台灣 86 件 CIM 計畫分類（62 件納入）。
- `data/derived/NSF_CIM計畫晶片製作地點追查.csv`：29 件 NSF 計畫的晶片製作地點、資助歸屬、證據連結。
- `data/derived/four_step_us.csv`、`four_step_tw.csv`、`four_step_merged.csv`：四步流程分類結果；`input_*.csv` 為分類輸入；`map_tw.csv` 為台灣計畫 ID 對照。
- `method/codebook_four_step.md`：四步分類規則；`four_step_worknotes_*.txt`：逐件判斷底稿。
- `scripts/key_numbers.py`：重現經費結構、研究層次、路線、四步分類的關鍵數字。
- `deck/`：內容稿、圖表數據（各頁數字的唯一來源）、Design 指令、講稿、合併初稿 pptx。
- `refs/`：參考簡報 PDF 與先前的兩份 pptx、圖片。
