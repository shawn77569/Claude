# 對話紀錄（自上次壓縮摘要起）

說明：第一段是先前對話的壓縮摘要（涵蓋更早的工作階段）；之後依時間順序列出使用者訊息、Claude 回覆，以及研究助理（子代理）的查核報告。工具呼叫與工具輸出未收錄。

## 先前對話的壓縮摘要

This session is being continued from a previous conversation that ran out of context. The summary below covers the earlier portion of the conversation.

Summary:
1. **Primary Request and Intent**

   **Context.** Shawn (曾昱翔, CIER 國際所 輔佐研究員) is finishing the presentation 「美國AI晶片NSF科研投資趨勢觀察：聚焦記憶體內運算」.
   - Venue: 2026/10/8, 地緣政治影響下的科技布局與治理研討會, 主題一.
   - Talk length: 15 minutes.
   - Production is in Claude Design. Claude's role is content review, verification, and Design-pasteable instructions.

   **Requests over this session:**
   - Per-page reviews.
   - Content upgrades (new industry and research pages, cross-section, timeline, mirror analysis, capability table).
   - Risk review.
   - Logic and story-flow checks.
   - Full speaker script (HTML).
   - Restructure of chapters 3–4, which Shawn found fragmented.

   **Latest request.** Shawn agreed to a full restructure and asked whether more data was needed. He then said: "往下挖論文未必不可行，要不直接試試看? 這樣好像會有更穩健的證據鍊". In other words: trace NSF CIM projects' papers to find where their chips were actually fabricated, to make the 研究→銜接→量產 evidence chain (pp.19/21/23) more robust.

2. **Key Technical Concepts**

   **The proposed story backbone.** A 研究→銜接→量產 chain:
   - **Ch3:**
     - p16 然而 (increment ~80% not planning chip validation).
     - p17 core page (投入與量產方向相反).
     - p18 成因 (資助者分工: d-Matrix 45,000萬; DARPA OPTIMA 7,800萬, existing VLSI; SRC PRISM 5,050萬; NSF CIM 4,224萬 — NSF 位於最前端).
     - p19 銜接段 (研究到量產需5年以上，中間要靠晶圓廠完成整合; chain introduced).
   - **Ch4:**
     - p21 台灣在三段都有基礎、銜接段突出.
     - p22 研究端: 起步早但2023後元件研究被反超 (absorptive capacity, Cohen & Levinthal 1990).
     - p23 三個著力點 (研究端／銜接端／量產端 × 依據／啟示／觀察訊號).
     - p24 結語.
     - p25 封底.
   - Total: 25 pages.

   **Mirror-analysis numbers** (counts, 62 NSTC vs 60 NSF):

   | Measure | Taiwan (NSTC) | US (NSF) |
   |---|---|---|
   | CIM share of AI-chip projects, 2018–20 / 21–22 / 23–24 | 20% / 43% / 26% | 16% / 21% / 25% |
   | Upstream share (B1), 2018–22 → 2023–24 | 56% → 40% (2025: 45%) | 37% → 55% (by funding: 37% → 61%) |
   | Emerging-memory share | ≈60% | ≈62% |
   | CIM projects per year | flat | ×2.4 |

   **Other verified facts:**
   - ACED Fab: Taiwan-side tape-out goes through TSRI; first batch of 6 projects. Sources: 國科會 call; 科技新報 2023/6.
   - AIP FYI (2025/11): the Arizona prototyping/packaging facility and the California design facility will not move forward.
   - ITRI 12吋試產線: 37.7億, completion 2027/12, operations 2028Q1, 28–90nm BEOL, includes 3D integration.
   - TSMC SoIC in volume production since 2025.

   **Abstract-mention check** (no quantitative comparison possible):
   - NSF: 5 of 74 CIM abstracts mention a fab.
   - GRB: 10 of 86.

   **NSF Awards API.** Works through WebFetch, e.g.:
   https://api.nsf.gov/services/v1/awards.json?keyword="..."&printFields=id,title,piFirstName,piLastName,awardeeName,startDate,publicationResearch
   The Bash proxy blocks api.nsf.gov.

3. **Files and Code Sections**

   **Data inputs (read-only):**
   - /mnt/user-data/uploads/nsf_cim_annotated_v1_1.csv
     - 60 primary CIM projects.
     - Columns include device_route, maturity (模擬驗證20 / 元件原型18 / 晶片流片11 / 電路實測7 / 商用硬體實證4), process_compat, abstract_en, budget_usd_corrected.
     - No NSF award IDs.
   - /mnt/user-data/uploads/nsf_integrated_v2_0_362_20260604.csv — 361 records used (NSF-152365 excluded as a duplicate).
   - /mnt/user-data/uploads/grb_integrated_v2_0_333_20260618.csv — NSTC A5 = 86 CIM projects.

   **Outputs:**
   - /mnt/user-data/outputs/GRB國科會CIM計畫分類_台美鏡像分析.csv
     - Columns: 起始年, 主持人, 計畫名稱, 納入分析, 記憶體類型, 規劃成熟度（依摘要）, 研究層次.
     - 62 included; excluded indices {1,2,9,11,13,15,20,28,33,34,35,36,41,54,59,61,64,68,69,70,75,76,77,78}.
   - /mnt/user-data/outputs/講稿_美國AI晶片NSF科研投資趨勢觀察.html
     - 15-minute script, published Artifact https://claude.ai/artifact/AjXNPrEJo5uk14h8LM2hih.
     - Data-driven: a JS `chapters` array of `{p, sec, title, cue, t}`, opt sentences in `<span class="opt">`, pauses in `<span class="pause">`.
     - Total ≈860s.
     - The file changed on disk since it was last read; treat it as current.
     - It needs a rewrite for the new ch3/ch4 structure.

   **Scratchpad:**
   - /tmp/claude-0/-home-claude/be76eb58-def2-5924-bce3-73de4a2fe852/scratchpad/targets.json — 29 trace targets.

4. **Errors and Fixes**
   - api.nsf.gov is blocked from Bash, so WebFetch was used instead.
   - par.nsf.gov, Crossref, OpenAlex and Wiley/ACS rate-limited or blocked some subagent fetches. Gaps are noted per project.
   - The first PS-IMC fetch showed only "Implemented in 28-nm CMOS". A targeted re-fetch confirmed "PS-IMC is prototyped in TSMC 28-nm CMOS."
   - User-driven corrections (from earlier):
     - "台灣研究較分散" was disproved (both sides spread over 28 institutions).
     - "缺口" was reworded to "可著力之處".
     - The ch4 contradiction (追趕 vs 不追趕) was resolved by the "原本領先、被反超" framing.
     - 重點 lines must not serve as transitions.
     - No backup pages.

5. **Problem Solving: paper-trace results**

   **T1 (chip-oriented projects)**

   | Project | Group | Result |
   |---|---|---|
   | NSF-100085 | Yu, Georgia Tech | **TSMC N40 RRAM** (verified: "Both macros were taped-out with TSMC N40 RRAM process", ascent.nd.edu). Also IEDM'16 Tsinghua 130nm RRAM macro, foundry unnamed. |
   | NSF-144368 / 147892 / 149783 | Fan cluster, ASU/JHU/Stanford | **PS-IMC TSMC 28nm** (verified, par 10504121). **PSRAM TSMC 65nm** (verified, par 10389143, NSF 2003749/2144751). SP-IMC, SAFER, FP-IMC: 28nm, foundry unnamed. 65nm RRAM genome macro at **Albany NanoTech, NY** (verified, par 10539375; grants 2314591, 2414603, 2349802, 2342726 + CoCoSys). 64-kb SOT-MRAM (Nature Electronics 2025; TSMC/ITRI/NYCU co-authors), fab not stated. No MRAM-CIM chip yet. |
   | NSF-91603 | Cady, Albany | Albany NanoTech, custom 65nm CMOS + HfO2 ReRAM, 300mm. |
   | NSF-99203 | Lu, Michigan | 65nm on 300mm, foundry unnamed; RRAM added with an Applied Materials tool. |
   | NSF-117046 | Xia, UMass | 180nm, unnamed commercial manufacturer. |
   | NSF-130805 | — | Used TetraMem MX100 (65nm; TSMC per earlier news). |
   | NSF-129873 | Shukla | GF Dresden 28nm FeFET test devices; no chip. |
   | NSF-135355 | — | 90nm node only. |
   | NSF-110407 | Anaflash | Samsung 28nm, not tied to the award. |
   | NSF-93463, 137289, 146726, 147944, 149652, 158153, 155319 | — | No foundry chip (149652: Intel16 design, unconfirmed). |

   **T2 (emerging-memory device projects, 2023–24)**
   - NSF-158156 (Purdue, Li): **TSMC 40nm ULP with foundry RRAM**, PROTEUS/CENTAUR. Verified: "Fabricated in 40 nm ULP CMOS with foundry RRAM"; TSMC thanked for chip fabrication; award 2425498. The project's own In2O3 devices are not on any foundry chip.
   - NSF-139690: EMBER on TSMC 40nm (verified; award 2235462). This is a storage macro, not CIM.
   - NSF-142586: lab HZO plus GF Dresden 22nm FDSOI, inferred from co-authors.
   - NSF-150961: in-house devices; HyFPCiM TSMC 65nm (funding may be CoCoSys).
   - NSF-147884, 140176, 158046, 149953, 158164: university cleanroom only.
   - NSF-158150 and 147921: no hardware yet.

   **Emerging conclusions** (to present with facts and inferences separated):
   - **Fact:** Of NSF CIM work that reaches a chip with a named commercial foundry, it is mostly TSMC — 4 independent research groups. These chips often use TSMC's existing embedded RRAM or SRAM.
   - **Fact:** The US also uses its own research fab, Albany NanoTech, for RRAM-on-CMOS (2 groups), and GF Dresden supplies FeFET test devices.
   - **Fact:** The novel emerging devices NSF funds in 2023–24 remain in university cleanrooms; none is integrated in a foundry yet.
   - **Inference:** The bridge for next-generation devices is still empty. That is where Taiwan (TSMC, TSRI, the 2028 ITRI pilot line) could step in — while noting that Taiwan is not the only route.

6. **All User Messages** (this session, after the earlier summary)
   - 除了這些之外，綜觀整份簡報，還有什麼問題嗎?
   - 我覺得有些簡報頁面的構圖有點太過強烈，比如15、24頁。有些地方文字又太鬆散
   - 我覺得可以適當補充文字內容
   - 上一則指令我還沒輸入
   - Design questions: chapter-number 160px vs rule 3; keeping the cream cards; xlsx no longer available
   - 為什麼最後一頁變這麼空
   - 23頁的構圖還是很奇怪 / 我直接截圖23頁給你看
   - 而且我發現"NSF的錢押在離量產最遠的地方；把它帶到量產，正是台灣擅長的事。"這句話，其實很不像專業的學術或是產業用語，在台灣的語境中。
   - 幫我找出整份簡報有沒有類似的構句問題，同樣進行調整
   - Design questions on 「但」→「然而」 and 「晶片進度」→「晶片驗證」
   - 最新版簡報，幫我重新逐頁確認
   - 最後一頁感覺很怪，左側排版
   - 感覺"本頁要點"跟"如果只記得一句話"字體都偏小?
   - 簡報風格會跟參考簡報太接近嗎? 我想要做一點修改讓大家不要一眼就看出是同一套的
   - 不過我覺得參考簡報的模板使用，似乎比較豐富，跟我們這份有所不同
   - 剛剛的配色調整會影響到閱讀嗎?他正在改我不確定
   - Design question on right-column font sizes and settings
   - 感覺改完新的模板好像沒有比較好，很多地方看起來很怪
   - 封面頁有些字會不會太小
   - 除此之外，右側除了陣列圖之外，有什麼其他的選擇嗎?
   - 改完變這樣，你覺得如何?還沒改右側圖案
   - 封面是這樣 / 現在圖案長這樣 / 感覺很難馬上理解到想要傳達的意思
   - 感覺現在的圖搭配文字的呈現方式，好像沒有原本來的好，原本橫線隔開好像更好，然後這種凸顯數字的呈現方式，也不太符合中文簡報的用法
   - 這樣改完好一點。但是我發現現在很多左右分欄的，右邊剛好都是三條訊息，是剛好的還是刻意的?
   - 或是有可能更多點?
   - 除此之外，還有其他簡報內容需要升級或是查證補足資料的部分嗎? 現在，以一個聽眾的角度而言，這是一份完整且清晰有所觀察的剪報了嗎?
   - "現世代"這個詞是常見用法嗎?
   - 感覺重點部分，不應該作為銜接作用，而是強調本頁內容
   - 第八頁那個圖，畫得是正確的嗎?
   - 現在會有那些地方感覺字太小嗎?
   - 那整體內容上，有需要加強或是補充的嗎? 回顧我們之前討論過的內容，有什麼好的想法可以加入的嗎?
   - 後續觀察重點
   - 其他頁有需要進行對應調整的嗎
   - 24頁的結語有需要調整嗎?還是不影響
   - 簡報裡面所有的內容都經得起考驗跟推敲嗎?每一句話
   - 可以解釋一遍23頁的邏輯給我聽嗎?三個觀察詳細說明
   - 所以這頁簡報設計這樣可以嗎?
   - 現在是這樣，看完之後你再給我調整建議
   - 請以現在這個版本對簡報進行逐頁的嚴格重新審視，並思考需不需要調整，能夠更好才調整，不用為調而調
   - 總結而言，根據這個版本，你可以把這個簡報想要呈現的故事線，根據簡報逐頁說給我聽
   - 感覺22頁的排版有點問題
   - 22和23是有對應的嗎?如果有的話現在容易發現嗎?如果不容易，有必要讓觀眾發現嗎?
   - 我覺得現在簡報，好像缺乏一個地方，讓觀眾知道，這些所謂的新興記憶體的CIM，鐵電材料、磁性材料等等，到底是用來做什麼的?NSF中的案例如何?有產業面的相關實例嗎?不然聽眾會覺得，你說這是這一世代的關注重點，但是我不是很懂他有什麼作用
   - 這些新興記憶體，應該都是作為記憶體產業有案例，但是作為CIM還在研究階段這樣嗎?
   - 這樣只用一頁呈現，會不會太擁擠
   - 所以新興記憶體都是針對邊緣裝置為主嗎?只有DRAM路線是主打雲端?
   - 我覺得這些資訊也很重要，可以思考怎樣能加入簡報中嗎?讓觀眾更好的理解CIM的方向
   - 第17頁的部分，感覺也可以多加說明，這些產品是做什麼的
   - 三星目前在PIM上，是邊緣端較快還是雲端
   - 感覺這樣加起來之後，第10頁是不是擠太多資訊了?
   - 真的不做拆分嗎
   - 現在10跟11頁好像占比很懸殊，要不要乾脆就是一頁講特性跟計劃，另一頁講產業
   - 我覺得拆分完之後，就可以講得更詳細一點，還有什麼相關資訊可以讓內容更充實的嗎?從我們剛剛的討論提到或是可能遺漏的部分
   - 感覺太多在備註裡面了，能不能某種程度讓她出現在簡報李
   - 幫我把這些調整全部合併在一起，我還在剛剛新增一頁的版本
   - 好了 [PDF]
   - 現在這樣呢? 有沒有其他類似剛剛我發現的這種問題
   - 我說的類似問題是指，剛剛我發現這邊可以這樣調整會讓觀眾更好理解
   - 我剛剛在思考，文獻在這篇剪報中的作用是什麼?
   - 我原本是想說14要不要專心在講解重點方向就好，可能可以用類似圖解呈現，但是這樣好像會太擁擠
   - 要不要歸納更多研究計畫重點，容入這張圖?
   - 幫我把這一頁的調整合併
   - 19頁會不會有點多餘的感覺
   - 但是我不想要放備用頁。整份簡報評估下來，有哪些頁數有這種類似問題嗎
   - 這樣第三節會不會變得很單薄，有什麼其他適合加入的新內容嗎?
   - 剛剛的我也還沒調整，幫我合併
   - [PDF, 26 pages]
   - 除了這個之外，還有什麼小型改動，比如像剛剛那樣調整一個一兩頁內容，可以讓整份簡報更充實或是說理更有邏輯
   - 這些感覺都是偏小型的改動，在不設限改動程度跟範圍的前提下，有什麼其他想法嗎?
   - 我覺得一三項還不錯，幫我記起來。可以先做一
   - 所以第一項算是做完了嗎
   - 好
   - 好。我套用進Design，妳先幫我接著做下一步
   - 有其他頁需要進行對應調整的嗎
   - 現在整個簡報的邏輯順序有通順嗎
   - 簡報會提到可能有風險的結論或是訊息嗎
   - 所以我們補充的這些東西，不影響結論是嗎
   - Design reminders: two remaining 「缺口」 wordings
   - 那現在完整的故事推理是怎樣，從頭到尾跟我講一次故事
   - 從一個局外人的角度審視的話，這個故事鍊有說服人嗎?還是有什麼邏輯漏洞?
   - 有哪些在講者備註上的資訊，是應該要出現在簡報上，也就是說漏講到會讓簡報容易被攻擊?
   - 幫我把每一頁要怎麼講寫成完整且通順的講稿。 (answered: 15 分鐘; HTML)
   - 我現在仔細重新講一遍，發現第四節開始的邏輯，我越看越不懂，這是通順的嗎?
   - 那前三節呢?有類似的邏輯不通順或是好像一直在講同一件事情的問題嗎
   - 我覺得現在三和四章的內容，邏輯鍊有點破碎，你可以幫我重新構思，這裡怎麼編排會更好嗎
   - 可以全部重組，但是需不需要蒐集更多資料，或是回去挖原始計畫資訊等等
   - 往下挖論文未必不可行，要不直接試試看? 這樣好像會有更穩健的證據鍊

   **Standing preferences:**
   - Traditional Chinese.
   - Direct; no flattery.
   - Separate facts from inference.
   - Search before stating volatile facts.
   - Present options with tradeoffs.
   - Default to deep, complete analysis.
   - Cite sources.
   - Do not produce pptx files.
   - Earlier deck rules:
     - 重點 emphasizes the page, not a transition.
     - No backup pages.
     - No text under charts; footnotes at page bottom.
     - 重點 on one line.
     - No word breaks in titles.

7. **Pending Tasks**
   - **Task #2 (in progress):** finish consolidating the trace results and checking the evidence.
   - **Task #3 (pending):** update the restructure instruction's pp.18/19/21/23 wording and evidence to match the trace findings.
     - Add the TSMC evidence: 4 independent groups; PROTEUS and Yu's chips.
     - Add the honest nuance: Albany NanoTech is a US research-fab route; novel devices are not yet in any foundry.
     - Provide updated Design instructions.
   - **After Shawn applies the 25-page restructure in Design:**
     - Check the PDF: the chain graphics on p19/p21, merged p22, merged p23.
     - Rewrite the ch3/ch4 portion of the speaker-script HTML: new page order, the 伏筆 fix ("以為NSF在推動CIM商業化"), avoid repeating explanations.
   - Optional: send the 10/8 sensitive Q&A prep. It is already included in the script's QA section.

8. **Current Work**

   I was finishing verification of the subagents' paper-trace results, aimed at Shawn's request: "往下挖論文未必不可行，要不直接試試看? 這樣好像會有更穩健的證據鍊".

   Five parallel subagents traced 29 NSF CIM projects (T1: 18 chip/circuit projects; T2: 11 emerging-memory device projects from 2023–24). I then personally verified these key quotes with WebFetch:
   - PROTEUS (TSMC 40nm ULP with foundry RRAM; NSF 2425498).
   - Yu's group: "Both macros were taped-out with TSMC N40 RRAM process".
   - Albany NanoTech 65nm RRAM macro (par 10539375).
   - "PS-IMC is prototyped in TSMC 28-nm CMOS." (par 10504121).
   - "We prototyped the PSRAM macro (128×128) in TSMC 65nm CMOS" (par 10389143).
   - EMBER: "3 M cells in TSMC 40-nm CMOS", NSF FuSe-TG 2235462.

   The synthesis (section 5) was ready but had not yet been reported to Shawn.

9. **Optional Next Step**

   Report the trace results to Shawn in Traditional Chinese, with sources.
   - Present a table by research group: TSMC ×4 groups; Albany NanoTech ×2; GF Dresden test devices ×2; unnamed or none for the rest.
   - Present the refined conclusions, separating facts from inference:
     - NSF CIM chips with a named commercial foundry are mostly from TSMC, often on TSMC's existing embedded RRAM or SRAM processes.
     - The novel emerging devices funded in 2023–24 are still made in university cleanrooms; none is integrated in a foundry yet.
     - The US also has a research-fab route (Albany NanoTech).
   - Explain how this strengthens and nuances p19/p21/p23. Then give updated Design instruction edits for those pages, for example:
     - p19 block: 「NSF計畫做成晶片時，可確認晶圓廠者多為台積電（4個研究團隊）；新興元件本身仍在大學無塵室」.
     - p21 銜接端: add 「美國學界CIM晶片多採台積電製程（如Purdue 40奈米、Georgia Tech 40奈米RRAM、ASU 28奈米）」.
     - p23 依據: 「新興元件尚未進入任何晶圓廠」.
     - Footnotes citing par.nsf.gov, the Purdue PROTEUS manuscript, and ascent.nd.edu.
   - Mark Task #2 complete and Task #3 in progress.

If you need specific details from before compaction (like exact code snippets, error messages, or content you generated), read the full transcript at: /root/.claude/projects/-home-claude/be76eb58-def2-5924-bce3-73de4a2fe852.jsonl
Continue the conversation from where it left off without asking the user any further questions. Resume directly — do not acknowledge the summary, do not recap what was happening, do not preface with "I'll continue" or similar. Pick up the last task as if the break never happened.

## Claude

我追查了29件NSF CIM計畫的公開論文，找晶片實際在哪裡製作。研究→銜接→量產這條證據鏈確實變得比較穩，但只撐得起較窄的說法；「美國靠台灣量產」這種說法撐不起來，不要講。

#### 一、追查結果

**有明確依據的事實：**

1. **能確認製作地點的晶片，只來自5個團隊。** 其中4個用台積電製程，2個用紐約州的 Albany NanoTech 研究晶圓廠（ASU／JHU 團隊兩邊都用過）。

| 製作地點 | 團隊與晶片 | 資助來源 |
|---|---|---|
| 台積電 | Georgia Tech（Yu）：40奈米 RRAM CIM 晶片 | SRC／DARPA 的 JUMP 計畫，**沒有查到致謝 NSF** |
| 台積電 | ASU／JHU（Fan）：65奈米、28奈米 | NSF |
| 台積電 | Purdue（Li）：PROTEUS、CENTAUR，40奈米＋台積電的 RRAM | NSF 2425498 |
| 台積電 | USC：EMBER，40奈米 RRAM（**儲存用晶片，不是 CIM**） | NSF 2235462 |
| Albany NanoTech | ASU／JHU（Fan）：65奈米 RRAM CIM 晶片 | NSF |
| Albany NanoTech | SUNY（Cady）：RAVENS-2，65奈米＋RRAM | 空軍研究實驗室，不是 NSF |

   - 只算論文有致謝 NSF 的：3個團隊，全部用過台積電。
   - 這些台積電晶片用的都是台積電**本來就有的** RRAM 或 SRAM 製程，不是計畫自己研發的新元件。

2. **NSF 2023–24 年的新興記憶體元件計畫（追查11件），自研的新元件還沒有任何一件進入晶圓廠：**
   - 9件：元件還在大學無塵室（鐵電、磁性、氧化物、二維材料），或還沒有硬體。
   - 2件（Purdue、USC）：做成了晶片，但用的是台積電現有的 RRAM。
   - 0件：計畫自研的新元件做進晶圓廠晶片。

3. **有一個例外值得一提：** ACED Fab 資助的 64kb SOT-MRAM 陣列（Nature Electronics, 2025），共同作者有台積電、工研院、陽明交大，但論文沒寫在哪裡製作。

4. **美國本土的另一條路：** Albany NanoTech 由紐約州的 NY CREATES 營運，2025年7月啟用 NSTC EUV 加速器。簡報裡已有的 AIP FYI 資料是：NSTC 在亞利桑那的原型設施、加州的設計設施不再推進。

**基於推理的判斷（研判）：**
- 用現有記憶體做晶片驗證這一步，美國學界已經大量經過台積電。
- NSF 押注的新元件還沒走到這一步，所以「下一代由誰來銜接」還沒定案。台灣（台積電、TSRI、2028年工研院試產線）和美國 Albany 都是可能的地點。
- 這比原本「台灣擅長銜接」的說法具體，也比較守得住。

#### 二、對故事鏈的影響

**變強的地方：**
- 第19頁有了實證：NSF 的新元件還在研究段。
- 第21頁「銜接段突出」有了實證：NSF 團隊做晶片時用的是台積電。
- 第23頁的觀察訊號可以具體化成「新元件第一次在哪裡做成晶片」，正好接上研討會的地緣政治主題。

**要避免的說法：**
- 「美國依賴台灣」「台積電幫 NSF 量產」：資料只到晶片驗證這一步，沒有到量產。
- 「新元件研究落後或失敗」：這些計畫才啟動2–3年，還沒進晶圓廠是時程上的正常狀態。

**弱點：**
- 能確認製作地點的只有5個團隊，其餘論文多半只寫製程節點、沒寫晶圓廠。所以頁面上一律用「可確認者」這種措辭。
- Georgia Tech 那顆晶片不是 NSF 資助。只算致謝 NSF 的，結論一樣（3個團隊都用台積電）。

#### 三、Design 指令

我看不到你手上重組指令的原始措辭，所以第19頁給整頁內容，第21、23頁只給要替換或加入的部分。

**第19頁**
```
請修改第19頁，以下內容取代重組指令中第19頁的內容。版面維持左圖右文，右側沿用橫線分隔的三個區塊，不要放大數字。

標題：研究走向量產需5年以上，NSF的新元件仍在大學實驗室
（「5年以上」「大學實驗室」用強調色）

左側：沿用「研究→銜接→量產」三段鏈狀圖，三段下方各一行說明：
・研究：大學實驗室製作元件
・銜接：晶圓廠整合，做成晶片驗證
・量產：產品化
鏈狀圖下方沿用原時間軸的三個案例（知存、三星PIM、TetraMem），每例一行，不另加新數字。

右側三個區塊：
1. 小標：9件仍在實驗室，或尚無硬體
   內文：追查NSF 2023–24年新興記憶體元件計畫11件，鐵電、磁性、氧化物與二維材料元件，均在大學無塵室製作。
2. 小標：2件已做成晶片，但採晶圓廠既有製程
   內文：Purdue與USC團隊的晶片在台積電40奈米製作，使用台積電既有的RRAM，並非計畫自研的新元件。
3. 小標：自研新元件進入晶圓廠：尚無
   內文：這些計畫多在2023–24年啟動，距今僅2–3年；何時進入晶圓廠，是後續觀察重點。

本頁要點：NSF近年資助的新元件，尚未跨入晶圓廠整合這一步

註腳：資料來源：作者追查NSF CIM計畫之公開論文（par.nsf.gov、IEEE、Nature等），依論文致謝歸屬計畫，查核至2026年10月；論文發表有時間落差。案例時間軸來源同原頁。
```

**第21頁**
```
請修改第21頁，其餘不變：
1. 在「銜接」段現有內容的最前面加入一行：
   NSF CIM研究團隊的晶片：可確認製作地點的5個團隊中，4個採台積電製程
2. 本頁要點改為：台灣最突出的是銜接段：NSF CIM團隊的晶片多在台積電製作
3. 註腳新增：團隊指NSF CIM計畫主持人之研究團隊。Georgia Tech、ASU／JHU、Purdue、USC採台積電28–65奈米製程；ASU／JHU與SUNY另使用紐約州Albany NanoTech研究晶圓廠。晶片資助來源含NSF、SRC／JUMP、美國空軍研究實驗室；其中致謝NSF者3個團隊，均採台積電。
```

**第23頁（只換「銜接端」這一列）**
```
請修改第23頁的「銜接端」一列，其餘兩列不變：
・依據：NSF CIM團隊的晶片多在台積電製作；但NSF自研的新元件尚未進入晶圓廠
・啟示：或可擴大ACED Fab模式，並評估試產線納入新興記憶體，在新元件首次整合時即參與
・觀察訊號：NSF新元件首次做成晶圓廠晶片的時間與地點（台灣，或美國Albany NanoTech）

註腳新增：ACED Fab資助的64kb SOT-MRAM陣列，共同作者含台積電、工研院、陽明交大（Nature Electronics, 2025）。Albany NanoTech為紐約州研究晶圓廠，2025年7月啟用NSTC EUV加速器；NSTC亞利桑那原型設施與加州設計設施不再推進（AIP FYI, 2025/11）。
```

第24頁結語不用改。「相對優勢」的說法現在有第21頁的實證支撐，但對新元件仍屬研判，維持原措辭即可。

#### 四、可能被問到的問題

- **「學界在台積電下線很正常，這能代表什麼？」** 我只主張「晶片驗證這一步已經經過台灣」。重點在 NSF 的新元件還沒走到這一步，下一代由誰銜接還沒定。
- **「5個團隊的樣本太小。」** 同意。追查的29件中，其他論文大多沒寫晶圓廠，所以頁面只用「可確認者」的說法。
- **「美國有自己的研究晶圓廠吧？」** 有，Albany NanoTech，2個團隊用過。這正是第23頁的觀察訊號。

你把重組套用進 Design 後，把 PDF 給我，我會檢查第19、21頁的鏈狀圖，再改寫講稿第三、四章。

Sources:
- [Purdue PROTEUS 論文手稿（JSSC 2026）](https://engineering.purdue.edu/NanoX/assets/pdf/2026_JSSC_PROTEUS_AAM.pdf)
- [ASCENT：N40 RRAM CIM Macro（Georgia Tech）](https://ascent.nd.edu/events/2022/01/27/221257-ascent-theme-4-n40-rram-compute-in-memory-macro-without-adc-and-with-built-in-error-correction/)
- [PS-IMC，台積電28奈米（par.nsf.gov 10504121）](https://par.nsf.gov/servlets/purl/10504121)
- [PSRAM，台積電65奈米（par.nsf.gov 10389143）](https://par.nsf.gov/servlets/purl/10389143)
- [65奈米 RRAM CIM，Albany NanoTech（par.nsf.gov 10539375）](https://par.nsf.gov/servlets/purl/10539375)
- [EMBER，台積電40奈米（JSSC 2024 論文副本）](https://www.academia.edu/119833869/)
- [Cady 研究團隊：RAVENS-2 於 Albany NanoTech 製作](https://www.albany.edu/nanoscale-science-engineering/cady-research-group)
- [Nature Electronics 2025：64kb SOT-MRAM（ACED Fab 資助）](https://www.nature.com/articles/s41928-025-01434-x)
- [Manufacturing Dive：NSTC EUV 加速器於 Albany 啟用（2025/7）](https://www.manufacturingdive.com/news/chips-act-r-d-nstc-euv-accelerator-facility-opens-albany-new-york/753104/)
- 其餘20餘件計畫的證據連結在檔案「NSF_CIM計畫晶片製作地點追查.csv」中。

## 使用者

新的結果有支撐台灣作為承接新興態CIM這個定位嗎

## Claude

只能部分支撐，而且我上一則有一處推論過頭，要先修正。

新結果能證明的是：美國學界的CIM晶片常在台積電製作。它不能證明台灣是新興記憶體CIM的承接者。NSF近年增加的經費，大部分投入鐵電與磁性；這兩條路線上，台灣的銜接證據最少。

#### 一、修正上一則：「5個團隊中4個用台積電」要拆開看

按晶片種類拆開後：

| 晶片種類 | 台積電 | 美國Albany NanoTech | 德國GF德勒斯登 |
|---|---|---|---|
| SRAM-CIM（現行技術） | ASU／JHU（65、28奈米） | — | — |
| RRAM-CIM | Georgia Tech（JUMP資助）、Purdue | ASU／JHU、SUNY（空軍資助） | — |
| RRAM儲存晶片（非CIM） | USC | — | — |
| 鐵電 | — | — | 2個團隊，僅測試元件、未做成晶片 |
| 磁性 | 尚無MRAM-CIM晶片 | — | — |

拆開之後要注意三點（事實）：

- 「4個團隊」裡，ASU／JHU的台積電晶片是SRAM，USC那顆不是CIM晶片。
- 只看新興記憶體的CIM晶片，台積電2個團隊、Albany 2個團隊，兩邊一樣多。
- 再只算有致謝NSF的：Purdue用台積電、ASU／JHU用Albany，1比1。

所以上一則建議的第21頁本頁要點「NSF CIM團隊的晶片多在台積電製作」，數字本身沒錯。但放在講新興記憶體的第四章，聽眾會讀成「新興記憶體CIM靠台灣」，這個說法撐不住，請不要用。

#### 二、對照NSF的錢投到哪裡

年均經費取自簡報第10頁的數據（C04）。

| 路線 | NSF年均經費（萬美元） | 占增量 | 銜接證據 | 台灣的位置 |
|---|---|---|---|---|
| 鐵電 | 74 → 364 | 約43% | NSF團隊用的是GF德勒斯登的FeFET測試元件。業界方面，德國FMC已有8Gb產品送樣，GF已把鐵電整合進22FDX；台積電仍在研發階段 | 本次追查沒有看到台灣 |
| 磁性 | 27 → 237 | 約31% | 還沒有MRAM-CIM晶片。ACED Fab資助的64kb SOT-MRAM，台積電、工研院是共同作者，但論文沒寫在哪裡製作 | 有合作管道，屬間接證據 |
| 電阻式（RRAM） | 103 → 180 | 約11% | 台積電、Albany各2個團隊 | 有實績，但不是唯一 |
| 最新元件（氧化銦、二維材料、ECRAM） | 分散在各路線 | — | 都還在大學實驗室 | 還沒有人承接 |

鐵電加磁性約占NSF年均增量的74%（500萬／678萬美元）。台灣有銜接實績的RRAM，只占約11%。

#### 三、能支撐和不能支撐的

**能支撐（事實）：**
- 美國學界要把CIM做成晶片時，台積電是主要選擇之一，SRAM和RRAM都有。
- 台積電提供嵌入式RRAM，學界不必自建製程就能做出RRAM-CIM晶片。

**能支撐（研判）：**
- 在最成熟的新興記憶體RRAM上，台灣已經站在銜接段。
- 磁性方面，台灣透過ACED Fab和工研院、台積電的SOT-MRAM研發，有參與管道。

**不能支撐：**
- 「台灣是新興CIM的承接者」。NSF增量最集中的鐵電，晶圓廠整合是歐洲比較快。
- RRAM-CIM晶片在美國本土的Albany也做得出來，美國有自己的替代路徑。

**定位建議（研判）：** 把定位從「台灣可承接」改成「下一代的銜接位置還沒確定」。台灣在RRAM已有實績，在鐵電則落後歐洲，而鐵電正是NSF增幅最大的路線。這樣第23頁反而有更具體的著力點：試產線是否優先評估鐵電。依據有三點：
- 鐵電材料HZO一般認為可以做在晶片後段製程。
- 工研院已有HfO2鐵電記憶體技術。
- 台積電正在研發氧化物通道的鐵電元件。

這一點仍屬研判，簡報上要寫「值得思考」，不要寫成結論。

#### 四、簡報的兩個改法

**方案A：只修措辭，改動最小**

適合距離報告只剩一天的情況。缺點是會失去「鐵電是台灣最需著力的路線」這個新觀察。

```
第21頁：
・銜接段的證據行改為：美國學界CIM晶片的製作地點：台積電（SRAM、RRAM）與美國Albany NanoTech（RRAM）
・本頁要點：不要用上一則建議的版本，維持重組指令原本的本頁要點。

第23頁「銜接端」：
・依據：學界RRAM晶片由台積電與美國Albany分別製作；NSF自研的新元件尚未進入晶圓廠
・啟示：或可擴大ACED Fab模式，並評估試產線納入新興記憶體
・觀察訊號：維持上一則的版本
```

**方案B：在第21頁按路線呈現，邏輯較完整**

好處：把第二章「鐵電與磁性增幅最大」和第四章的著力點接起來，故事鏈閉合，也最經得起追問。代價：第21頁文字變多，講稿第三、四章也要跟著改。

```
第21頁「銜接」段改為三行，其餘不變：
・電阻式：台積電與美國Albany NanoTech皆有學界CIM晶片
・磁性：ACED Fab合作，台積電、工研院參與；尚無CIM晶片
・鐵電：學界使用德國GF元件；台積電仍在研發
本頁要點：台灣在電阻式已有銜接實績，鐵電與磁性的銜接位置尚未確定

第23頁「銜接端」：
・依據：NSF增量約七成四在鐵電與磁性，台灣在這兩條路線的銜接證據最少
・啟示：或可擴大ACED Fab模式；試產線是否優先納入鐵電，值得思考
・觀察訊號：NSF新元件首次做成晶圓廠晶片的時間與地點（台灣、美國Albany或歐洲）

第21頁註腳新增：鐵電業界現況依Semiecosystem（2026/2）；SOT-MRAM依Nature Electronics（2025）；學界晶片依作者追查之公開論文。
```

**兩案都要處理第24頁結語。** 現在的「推動前瞻技術邁向量產，是台灣的相對優勢所在」，在鐵電上會被追問。可以改成：

> NSF的CIM經費，集中在距離量產最遠的研發階段；這些技術走向量產時的銜接位置尚未確定，台灣具備基礎，或可提早參與。

如果不改結語，就要準備問答，例如：「鐵電是NSF增幅最大的路線，銜接的是德國GF，台灣的優勢在哪？」回答時要講出一個區分：台灣的實績在RRAM，鐵電是尚未確定、需要著力的部分。

我的判斷是方案B較好，但它要多花時間。決定後告訴我，我照該方案改講稿。

Sources:
- [Semiecosystem（Mark LaPedus）：Next-Gen Ferroelectric Memory: Still A Work In Progress（2026/2/8）](https://marklapedus.substack.com/p/next-gen-ferroelectric-memory-still)
- [工研院：鐵電隨機存取記憶體（FRAM）](https://www.itri.org.tw/ListStyle.aspx?DisplayStyle=01_content&SiteID=1&MmmID=1071732316365755674&MGID=1126466641377316446)
- [中央社：工研院與台積電合作 開發低功耗新世代記憶體（2024/1/17）](https://www.cna.com.tw/news/afe/202401170041.aspx)
- [Nature Electronics 2025：64kb SOT-MRAM（ACED Fab資助）](https://www.nature.com/articles/s41928-025-01434-x)
- [Shukla團隊：GF 28奈米FeFET（Scientific Reports 2023）](https://www.nature.com/articles/s41598-023-28217-8)
- [Ni團隊：22奈米FDSOI鐵電元件（arXiv 2403.04981）](https://arxiv.org/html/2403.04981v1)
- [Cady團隊：RAVENS-2於Albany NanoTech製作](https://www.albany.edu/nanoscale-science-engineering/cady-research-group)
- [ASU／JHU：65奈米RRAM CIM，Albany NanoTech（par.nsf.gov）](https://par.nsf.gov/servlets/purl/10539375)
- [Purdue PROTEUS：台積電40奈米＋晶圓廠RRAM](https://engineering.purdue.edu/NanoX/assets/pdf/2026_JSSC_PROTEUS_AAM.pdf)
- [ASCENT：Georgia Tech N40 RRAM CIM（JUMP任務）](https://ascent.nd.edu/events/2022/01/27/221257-ascent-theme-4-n40-rram-compute-in-memory-macro-without-adc-and-with-built-in-error-correction/)
- 經費數字：簡報數據檔「02_圖表數據.xlsx」工作表C04

## 使用者

我們先不要改簡報，先討論內容就好。
我覺得我現在的結論是想要收束到，根據我們以上的資料研判，包含科研計畫、學術發表、產業情況，台灣未來在CIM這一個領域可以朝哪個方向發展?或是應該是什麼定位?我們有什麼樣的能力做什麼事情?比如說，若要承接我們就要有能力承接?不一定是指，現在已經在做了，畢竟如新型態CIM等也還沒真的成熟，但是若要說台灣有能力承接，就要論證我們有相對應的能力。那比如PIM或是成熟CIM，我們的發展方向又在哪裡?是不要競爭了嗎?還是有其他相應的定位?如何去論證?

## 研究助理查核報告（子代理，模型產出，非使用者訊息）

### DRAM PIM／近記憶體運算事實查核（截至 2026-10-07）

所有引句都是透過 WebFetch 取得。這個工具會先用一個小模型處理網頁，所以引句大多是逐字擷取，但不保證完全逐字。標示「（譯）」的條目是工具把中文原文轉成英文的版本，不能當作原文引用。要放進簡報的引句，請回原網頁再核一次字句。

---

#### Q1. Samsung PIM 與 SK hynix AiM 現況

| 事實 | 原文引句 | URL | 日期 | 信心 |
|---|---|---|---|---|
| Samsung 在 Hot Chips 2026 發表 LPDDR5X-PIM，與標準 LPDDR5X 同封裝，可用一般記憶體控制器 | "614GB/s of PIM bandwidth at LPDDR5X-9600, compared with 76.8GB/s through the conventional memory interface"；"Uses the same 561-ball package as standard LPDDR5X and can work with a conventional memory controller" | https://www.sammyfans.com/2026/08/25/samsung-unveils-lpddr5x-pim-dram/ | 2026-08-25 | 中（二手科技媒體） |
| Samsung 的定位：LPDDR5X-PIM 是 HBM 的補充；尚未確認導入 Galaxy 手機 | "Samsung has positioned LPDDR5X-PIM as a complement to HBM rather than a replacement"；"Does not mean Samsung is immediately putting PIM into the next Galaxy S or Z series" | 同上 | 2026-08-25 | 中 |
| 第一個可能的商用載體是 Samsung System LSI 的 4nm AI PC 加速器 GAIA，最快 2027 年量產，已送原型給 Lenovo、HP | "GAIA is an AI accelerator for AI PCs being developed by Samsung Electronics' System LSI"；"Samsung has reportedly provided GAIA prototypes to major PC makers, including Lenovo"；"mass production potentially beginning as early as next year" | https://www.trendforce.com/news/2026/08/26/news-samsungs-4nm-gaia-could-mark-first-pim-commercialization-in-ai-pcs-mass-production-as-early-as-2027/ | 2026-08-26 | 中（"reportedly"，引韓媒） |
| 實測：Llama 3.1 8B 在 PIM 上 81.3 tok/s，傳統 LPDDR5X 為 27 tok/s | "81.3 tokens per second with Samsung LPDDR5X-PIM DRAM, compared with 27 tokens per second using conventional LPDDR5X" | sammyfans（同上） | 2026-08-25 | 中（廠商自測數據） |
| 歷史背景：Samsung HBM-PIM（Aquabolt-XL）2021 年發表；SK hynix GDDR6-AiM 2022 年發表，曾規劃與 Sapeon 整合 | "Samsung introduced the industry's first HBM-PIM (Aquabolt-XL) in 2021"；"SK hynix launched Graphics DRAM (GDDR6)-PIM in 2022"；"plans to introduce a technology that combines GDDR6-AiM with AI chips in collaboration with AI chip company Sapeon" | https://www.trendforce.com/news/2024/12/02/news-samsung-and-sk-hynix-reportedly-unite-to-standardize-lpddr6-pim-for-on-device-ai/ | 2024-12-02 | 高 |
| SK hynix AiMX 在 CES 2026 仍是「原型」加速卡 | "AiMX: SK hynix's accelerator card prototype featuring a GDDR6-AiM chip which is specialized for large language models (LLMs)." | https://www.storagenewsletter.com/2026/01/07/ces-2026-sk-hynix-showcases-next-gen-ai-memory-innovation/ | 2026-01-07 | 高（轉載 SK hynix 新聞稿） |

---

#### Q2. JEDEC PIM 標準化

| 事實 | 原文引句 | URL | 日期 | 信心 |
|---|---|---|---|---|
| JEDEC 官方說法：LPDDR6 PIM 標準「接近完成」 | "LPDDR6 PIM standard in development: JEDEC is also nearing completion of a standard for LPDDR6 Processing‑in‑Memory (LPDDR6 PIM) technology" | https://www.hpcwire.com/off-the-wire/jedec-previews-lpddr6-roadmap-expanding-lpddr-into-data-centers-and-processing-in-memory/ | 2026-04-22 | 高（JEDEC 新聞稿轉載） |
| TrendForce 報導同一件事 | "JEDEC is close to finalizing an LPDDR6 Processing-in-Memory (PIM) standard, which integrates compute functions directly into memory" | https://www.trendforce.com/news/2026/04/24/news-jedec-previews-lpddr6-enhancements-develops-socamm2-standard-for-ai-memory/ | 2026-04-24 | 高 |
| 推動者是 Samsung 與 SK hynix 聯合準備向 JEDEC 登錄 | "The collaboration between Samsung and SK hynix on 'Low Power Double Data Rate 6 (LPDDR6)-Processing In Memory (PIM)' products reportedly involves the preparation to register the standardization with the Joint Electron Device Engineering Council (JEDEC)" | TrendForce 2024-12-02（同 Q1） | 2024-12-02 | 中（"reportedly"） |
| 2026 年 8 月時，第一版 LPDDR6-PIM 規格仍描述為「接近定案」 | "The first JEDEC specification for next-generation LPDDR6-PIM is nearing finalization" | TrendForce 2026-08-26（同 Q1） | 2026-08-26 | 中 |

- JEDEC 新聞稿沒有點名任何推動 PIM 的公司。
- 檢視過的來源都沒有提到 MediaTek、Qualcomm 或任何台灣廠商參與或計畫採用。見最後一節。

---

#### Q3. HBM4 邏輯 base die 與 TSMC 的角色

| 事實 | 原文引句 | URL | 日期 | 信心 |
|---|---|---|---|---|
| SK hynix HBM4 用 TSMC 12nm base die | "HBM4 adopts a base die built using TSMC's logic process"；"The product combines a fifth-generation 10nm-class DRAM process with a 12nm base die from TSMC" | https://digitimes.com/news/a20260424VL208/sk-hynix-tsmc-hbm4-dram.html | 2026-04-24（日期由 URL 推得，頁面未顯示） | 高 |
| TSMC 的 base die 節點路線：HBM4 用 N12，C-HBM4E 用 N3P，並把記憶體控制器移進 base die | "TSMC plans to build HBM4 base dies on its N12 node"；"TSMC's custom HBM4E, currently dubbed C-HBM4E, will leap to the N3P node."；"For C-HBM4E, the base die will also integrate memory controllers—components typically housed in the host chip." | https://www.trendforce.com/news/2025/12/01/news-tsmc-unveils-custom-c-hbm4e-details-n3p-logic-dies-reportedly-target-2x-efficiency-gain/ | 2025-12-01 | 高（N12、N3P）／中（標題含 "reportedly"） |
| SK hynix 主流產品用 12nm，高階（NVIDIA、Google TPU）升到 3nm | "SK hynix will deploy TSMC's 12nm process for mainstream server base dies while escalating to 3nm for premium designs targeting NVIDIA's flagship GPUs and Google's TPUs." | 同上 | 2025-12-01 | 中（媒體轉述，非公司確認） |
| Micron HBM4E 的標準與客製 base die 都交給 TSMC，2027 年量產；HBM4 自製 | "Micron will hand TSMC the task of fabricating both standard and custom HBM4E logic dies"；"…with production targeted for 2027." | https://www.tomshardware.com/micron-hands-tsmc-the-keys-to-hbm4e | 2025-09-25 | 高 |
| Samsung HBM4 用自家 4nm 邏輯 base die（不經 TSMC）；HBM4E 2026 下半年送樣，custom HBM 2027 年送樣 | "Leading-edge DRAM with 4nm logic base die maximizes performance…"；"Sampling for HBM4E is expected to begin in the second half of 2026, while custom HBM samples will start reaching customers in 2027" | https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4 | 2026-02-12 | 高（一手） |
| SK hynix 對 custom HBM 的定義：把 GPU／ASIC 的部分功能移進 base die | "Custom HBM (cHBM): A product that integrates some functions located in GPUs and ASICs to the HBM base die, reflecting customer requirements." | storagenewsletter（同 Q1） | 2026-01-07 | 高 |
| CoWoS 整合 HBM 的規模 | "TSMC's currently mass-produced 5.5-reticle-size version is the world's largest today and has already achieved yields of 98%"；"support for up to 24 HBM stacks in 2029" | https://www.trendforce.com/news/2026/05/14/news-tsmc-sees-ai-wafer-demand-rising-11x-from-2022-2026-targets-cowos-with-24-hbm-stacks-in-2029/ | 2026-05-14 | 高 |

---

#### Q4. 台灣記憶體與晶圓代工廠

**華邦（Winbond）CUBE**

| 事實 | 原文引句 | URL | 日期 | 信心 |
|---|---|---|---|---|
| 公司把 CUBE 定位為 2027 年後的成長動能 | 「針對先進應用，華邦電推動的 CUBE（3D 客製化超高頻寬元件）與 Si-Cap（矽電容）新技術，有望在 2027 年後帶動新一輪的成長。」 | https://cdnfinance.technews.tw/2026/08/06/winbond-electronics-second-quarter-profit-hit-a-record-high/ | 2026-08-06 | 高 |
| 量產目標 2027 年（但句子主詞不明，可能指 CUBE 或 Si-Cap） | 「目標在2027年實現量產」；架構：「將DRAM、矽中介層(SiliconInterposer)與矽電容(Si-Cap/整合被動元件IPD)進行2.5D/3D先進封裝整合」 | https://www.ctee.com.tw/news/20260605701650-430201 | 2026-06-05 | 中 |
| 定位為邊緣與穿戴裝置 | 「華邦電的CUBE（Customized Ultra-Bandwidth Elements）技術則專攻邊緣運算的利基藍海，讓客戶彈性搭配自家的SoC晶片。」 | https://www.businesstoday.com.tw/article/category/183025/post/202603200037/ | 2026-04-01 | 中 |
| 已在獲利的是 CMS 客製化記憶體事業，不是 CUBE | 「華邦電在客製化記憶體事業（CMS，更名自 DRAM 事業）方面，受惠 AI 強勁需求，第二季營收季增 78%、年增超過 400%。」 | technews 2026-08-06（同上） | 2026-08-06 | 高 |

- 檢視過的來源都沒有點名 CUBE 客戶。

**力積電（PSMC）**

| 事實 | 原文引句 | URL | 日期 | 信心 |
|---|---|---|---|---|
| COMPUTEX 2026 以「3D AI Foundry」為主題，展示 3D WoW DRAM 堆疊 | 「力積電規劃在COMPUTEX以「3D AI Foundry」為主題，展示涵蓋3D WoW DRAM堆疊技術」 | https://ec.ltn.com.tw/article/breakingnews/5449421 | 2026-05-26 | 高 |
| 同場展示的合作業者 | 「愛普、晶豪科、Zentel Japan、智成與力晶微元等業者」（工具的英文翻譯有誤，以中文原名為準） | 同上 | 2026-05-26 | 中 |
| DRAM 與邏輯整合可縮短資料路徑、降低功耗 | 只取得英文轉述（譯），不能當原文引用 | 同上 | 2026-05-26 | 低 |

- 同場業者是展示夥伴，不等於已量產客戶。
- 沒有查到客戶名稱或量產時程。

**南亞科（Nanya）**

| 事實 | 原文引句 | URL | 日期 | 信心 |
|---|---|---|---|---|
| 客製化 AI 記憶體叫 UltraWIO，與多家邏輯 IC 廠合作，部分產品已試產 | 「南亞科開發的AI記憶體技術為UltraWIO（Ultra Wide I/O），即「超寬輸入輸出介面記憶體」」；「該公司與多家邏輯IC廠合作開發客製AI邏輯晶片與記憶體架構」；「部分產品已進入試產階段，預期下半年將有更多具體成果浮現」 | https://www.ctee.com.tw/news/20260305700104-430501 | 2026-03-05 | 中 |
| 可能用 WoW；第一層 DRAM 堆疊由南亞科自行完成 | 「未來可能採用Wafer-on-Wafer（WoW）技術，其中，第一層DRAM堆疊將由南亞科自行完成」 | 同上 | 2026-03-05 | 中 |
| 將率先採用 hybrid bonding | 「南亞科的客製化記憶體堆疊產品UWIO（Ultra Wide I/O），將率先採用Hybrid Bonding（混合鍵合）技術，大幅提升頻寬。」 | businesstoday（同上） | 2026-04-01 | 中 |

- 沒有查到具名客戶或量產時程。

---

#### Q5. d-Matrix Raptor

| 事實 | 原文引句 | URL | 日期 | 信心 |
|---|---|---|---|---|
| d-Matrix 與世芯（Alchip）合作 3D DRAM，首先用在 Raptor（Corsair 的後繼產品） | "TAIPEI — November 18, 2025 — d-Matrix...and Alchip...are collaboratively developing the world's first 3D DRAM-based datacenter inference accelerator"；"3DIMC will commercially debut on the d-Matrix Raptor™ inference accelerator, the successor to d-Matrix Corsair™." | https://www.d-matrix.ai/?p=2109 | 2025-11-18 | 高（一手） |
| 邏輯晶粒用 TSMC N4，以 face-to-face 方式疊在客製 3D DRAM 上；DRAM 與封裝由世芯負責 | "The logic die, built on TSMC N4, sits immediately above the DRAM"；"d-Matrix Raptor bonds a custom 3D DRAM die face to face with the logic die"；"The DRAM and packaging work is being done with Alchip" | https://hwbusters.com/news/d-matrix-raptor-drops-the-memory-phy-32gb-at-100-tb-s-against-hbm4s-192gb-at-18/ | 2026-08-24 | 中（二手，Hot Chips 2026 報導） |
| 時程：Hot Chips 當下未公布 | "d-Matrix has not said when Raptor ships, in what volume, or what it costs" | 同上 | 2026-08-24 | 中 |
| 時程：之後報導指向 2027 Q4 機櫃級部署 | "full rack-scale deployment targeting Q4 2027" | https://cryptobriefing.com/d-matrix-raptor-xpu-nvidia-mgx-rack-2027/ | 2026-09-10 | 低至中（非專業半導體媒體） |

---

#### Q6. TSMC SoIC

| 事實 | 原文引句 | URL | 日期 | 信心 |
|---|---|---|---|---|
| 第一代 SoIC 已量產 | "first-generation SoIC has already entered mass production" | https://www.trendforce.com/news/2026/05/14/news-tsmc-sees-ai-wafer-demand-rising-11x-from-2022-2026-targets-cowos-with-24-hbm-stacks-in-2029/ | 2026-05-14 | 高 |
| 鍵合間距路線：2025 年 6μm、2028 年 N2 世代 6μm、A14 世代 4.5μm | "the 6-micron bonding pitch version is set for 2025"；"N2-generation SoIC will support 6-micron stacking in 2028"；"the A14 generation is expected to advance further to 4.5-micron" | 同上 | 2026-05-14 | 高 |
| TSMC 提到把 DRAM 直接疊在運算晶片上的方向 | "SoIC and 3D IC technologies for directly stacking DRAM on compute chips" | 同上 | 2026-05-14 | 中（片段引句，上下文未取得） |

---

#### 無法驗證／矛盾資訊

1. **SK hynix AiM／AiMX 量產與客戶**：沒有找到任何量產或商用客戶的報導。2026-01 時 AiMX 仍是「prototype」；2024 年 Sapeon 合作的後續也查不到。LPDDR5X-AiM 沒有查到可驗證的資料。
2. **Samsung HBM-PIM 在 2025–2026 年的商用狀況**：只找到 2021 年發表的背景資料，沒有 2025–2026 年出貨或客戶的報導。LPDDR5X-PIM 目前沒有確認的量產客戶；GAIA 最快 2027 年量產，而且是「reportedly」。
3. **LPDDR6-PIM 正式發布**：2026-04 與 2026-08 都描述為「接近完成」。截至本次查核，沒有找到 JEDEC 正式發布 LPDDR6-PIM 規格的來源。
4. **MediaTek 或其他台灣廠商參與 JEDEC PIM**：無法驗證。檢視過的來源都沒有提及。
5. **SK hynix 高階 base die 用 TSMC 3nm**：只有 TrendForce 轉述媒體報導，沒有公司確認。Samsung newsroom 也沒有點名 HBM4 客戶。asiae 標題寫的「首批量產出貨給 Nvidia」只看過標題，沒有讀內文。
6. **d-Matrix 時程**：hwbusters（2026-08-24）說未公布出貨時程，cryptobriefing（2026-09-10）說目標 2027 Q4 機櫃級部署。兩者可能只是時間先後不同，但後者可信度較低。另外，d-Matrix 自己的新聞稿沒有提 TSMC 節點；N4 只來自二手報導。DRAM 晶圓由哪家製造，所有來源都沒有說明。
7. **華邦 CUBE 量產時程**：工商時報「目標在2027年實現量產」的主詞無法確認是 CUBE 還是 Si-Cap；公司法說的說法是「2027 年後帶動成長」。CUBE 客戶沒有查到。
8. **力積電與南亞科**：都沒有查到具名客戶或量產時程。南亞科與鈺創的合資公司只看過搜尋標題（technews 2025-08-07），沒有讀內文。
9. **SK hynix 與 TSMC 在 2024-04 簽 HBM4 合作 MOU**：只看過搜尋結果標題（Daum 2024-04-19），沒有讀內文。

#### 可存入記憶的事項
CIER 演講的 PIM 事實查核已完成，涵蓋 Samsung LPDDR5X-PIM（Hot Chips 2026）、JEDEC LPDDR6-PIM 尚未定案、TSMC 的 HBM4／HBM4E base die 角色、華邦／力積電／南亞科、d-Matrix 與世芯。相關主題檔為 /areas/cim-pim-research.md。

## 研究助理查核報告（子代理，模型產出，非使用者訊息）

### 核查報告：成熟型 CIM（SRAM／Flash 系）與台灣的位置（截至 2026-10-07）

**方法說明：** 下列引文都由 WebFetch 從原網頁擷取。擷取工具會先經過模型摘要，個別字句可能和原文有細微出入。實際做了約 40 次工具呼叫，超出原先約 25 次的預算。每個事實都附信心等級：高＝一手來源或權威技術媒體，原句明確；中＝二手媒體或間接證據；低＝來源可疑、只看到標題，或擷取結果語意不清。

---

#### Q1. 商用／準商用 CIM 晶片的製程與代工

| 公司／產品 | 事實 | 原文引述 | URL | 日期 | 信心 |
|---|---|---|---|---|---|
| d-Matrix Corsair | TSMC 6nm，數位 SRAM 記憶體內運算（DIMC），chiplet 架構 | "Built on TSMC 6nm." / "Energy Efficient DIMC Architecture" / "2GB of SRAM between all of the chiplets" | https://www.servethehome.com/d-matrix-presents-corsair-an-in-memory-computing-architecture-for-inference-at-hot-chips-2025/ | 2025-08-26 | 高 |
| d-Matrix Corsair 出貨狀態 | 這篇 Hot Chips 報導**沒有寫出貨時程**。另一則搜尋結果標題為「d-Matrix ships Corsair…」（letsdatascience），但未開啟查證 | （無） | https://letsdatascience.com/news/d-matrix-ships-corsair-inference-accelerator-claims-10x-toke-0537dcda | 不詳 | 低 |
| d-Matrix Raptor（3D DRAM） | 邏輯晶粒用 TSMC N4；3D DRAM 與封裝由**世芯（Alchip，台灣）**合作 | "the logic die, built on TSMC N4, sits immediately above the DRAM" / "The DRAM and packaging work is being done with Alchip, a partnership the two companies announced in November 2025" / "d-Matrix has not said when Raptor ships, in what volume, or what it costs" | https://hwbusters.com/news/d-matrix-raptor-drops-the-memory-phy-32gb-at-100-tb-s-against-hbm4s-192gb-at-18/ | 2026-08-24 | 中（二手媒體，未取得 d-Matrix／Alchip 原始新聞稿） |
| EnCharge AI EN100 | 電荷域（capacitor）類比 CIM；目前在早期試用階段 | "The resulting products are with early-access developers now" / "measuring the amount of charge instead of flow of charge" | https://spectrum.ieee.org/encharge-ai | 2025-06-02 | 高（狀態部分） |
| EnCharge EN100 製程／代工 | **未能查證**。該文沒有寫製程節點或代工廠 | — | 同上 | — | — |
| Axelera Metis | TSMC 12nm，數位記憶體內運算（D-IMC） | "It is built on TSMC's 12nm process." / "uses a digital in memory computing architecture… reaching 214TOPS with a power envelope of 3 to 16W." | https://www.eenewseurope.com/en/axelera-launches-metis-in-memory-computing-ai-edge-cards/ | 2023-09-12 | 高 |
| Axelera Europa | 製程與代工**未能查證**（本輪沒有開啟相關頁面） | — | — | — | — |
| Sagence AI | 以 flash 記憶單元做類比 CIM；首款產品原訂 2025 年推出 | "Sagence uses flash memory cells as the conductance values." / "Sagence's first product, to launch in 2025, will be geared toward vision systems" | https://spectrum.ieee.org/analog-ai-2669898661 | 2024-11-19 | 高（技術路線）；製程與代工**未能查證** |
| Mythic M1076／M1108 | 40nm 嵌入式 flash（NOR）類比矩陣處理器；2021 年 7 月起提供評估卡 | "40-nanometer embedded flash process" / "will be available for evaluation beginning in July 2021" | https://www.eetasia.com/mythic-launches-second-ai-chip/ | 2021-06-29 | 高 |
| Mythic（記憶體型態） | 嵌入式 NOR | "The cores are arranged in 108 compute tiles that incorporate embedded NOR memory with digital-to-analog (DAC) converters." | https://www.electronicdesign.com/technologies/embedded/article/21211169/startup-rolls-out-compute-in-memory-chip-for-deep-learning | 2020-12-15 | 高 |
| Mythic（代工廠） | Fujitsu 40nm 製程 | "On the Fujitsu 40 nm process, a near-reticle full-size die should have a capacity of around 300M weights" | https://fuse.wikichip.org/?p=2755 | 頁面未標日期 | 中 |
| 知存科技 WTM2101 | 以 NOR Flash 為基礎的存算一體語音晶片；出貨超過一千萬顆 | 「全球首款基于NOR Flash的存算一体语音芯片」；「已实现超过1000万颗的出货量，应用于华为、小米等品牌的智能可穿戴设备中」 | https://www.tmtpost.com/7944130.html | 2026-04-07 | 中（中國媒體轉述公司說法）；製程與代工**未能查證** |
| 知存 WTM-8 | 視覺用晶片，24+ TOPS（擷取結果為英文摘要，未取得中文原句） | — | 同上 | 2026-04-07 | 低～中 |
| 後摩智能 鴻途 H30／漫界 M50 | SRAM 存算一體；H30 自稱國內首款存算一體智駕晶片；M50 原訂 2025Q4 量產 | 「国内首款存算一体的智驾芯片」；「计划于2025年第四季度正式量产」 | 同上 | 2026-04-07 | 中；製程與代工**未能查證**；M50 是否已實際量產也未查證 |
| Rain AI | **本輪未查證** | — | — | — | — |
| Samsung CIM 產品 | **本輪未查證**。沒有找到 Samsung 商用 CIM 產品的一手來源 | — | — | — | — |

---

#### Q2. 台積電自家的 CIM 研究

| 事實 | 原文引述 | URL | 日期 | 信心 |
|---|---|---|---|---|
| ISSCC 2024 論文 34.4：3nm 全數位 CIM macro，使用晶圓廠標準 6T-SRAM 位元格（作者含 TSMC 的 Yu-Der Chih） | "34.4 A 3nm, 32.5TOPS/W, 55.0TOPS/mm2 and 3.78Mb/mm2 Fully-Digital Compute-in-Memory Macro Supporting INT12 × INT12 with a Parallel-MAC Architecture and Foundry 6T-SRAM Bit Cell. ISSCC 2024: 572-574" | https://dblp1.uni-trier.de/pers/hj86/c/Chih:Yu=Der | ISSCC 2024 | 高 |
| 2023 年 4nm SRAM 數位 CIM macro（台積電研究網頁列出，會議名稱沒有在擷取結果中出現） | "A 4nm 6163-TOPS/W/b 4790−TOPS/mm2/b SRAM Based Digital-Computing-in-Memory Macro Supporting Bit-Width Flexibility and Simultaneous MAC and Weight Update" | https://research.tsmc.com/english/research/artificial-intelligence/publish-time-1.html | 2023 | 高（論文存在）；中（會議是否為 ISSCC） |
| 台積電研究網頁也列出 16nm gain-cell CIM（2024、2025）與 22nm STT-MRAM CIM／近記憶體運算（2023–2025） | 例："A 16nm 216kb, 188.4TOPS/W and 133.5TFLOPS/W Microscaling Multi-Mode Gain-Cell CIM Macro for Edge-AI Devices"（2025）；"A 22nm 104.5TOPS/W μ-NMC-Δ-IMC Heterogeneous STT-MRAM CIM Macro…"（2025） | 同上 | 2023–2025 | 高 |
| **DCIM 是否以設計支援、IP 或 OIP 形式提供給客戶：沒有找到明確公開陳述**。網頁上只有泛稱的句子 | "We are particularly well-positioned to supply the most advanced AI hardware to our customers thanks to our leading-edge logic, memory, and packaging technologies." | 同上 | 不詳 | 高（確認「沒有明確陳述」）；技術論壇與 OIP 簡報本輪沒有取得 |

---

#### Q3. 聯發科（MediaTek）

| 事實 | 原文引述 | URL | 日期 | 信心 |
|---|---|---|---|---|
| **沒有找到可查證的證據**顯示聯發科量產產品（含手機 SoC 的 NPU／APU）採用 SRAM-CIM，也沒有找到聯發科具名的 ISSCC CIM 論文。查過的中、英文搜尋結果都只指向一般性資料 | — | — | — | 結論：無法證實 |
| 聯發科 ISSCC 2020 有 11 篇論文入選（從搜尋標題得知，本輪未開啟全文，無法確認其中是否有 CIM 論文） | "11 MediaTek Papers Selected for ISSCC 2020, the Highest Amount of Any Technology Company" | https://corp.mediatek.com/news-events/press-releases/mediatek-isscc-2020-achievement | 2020 | 中（只看到標題） |

---

#### Q4. 旺宏與其他台灣廠商

| 事實 | 原文引述 | URL | 日期 | 信心 |
|---|---|---|---|---|
| 旺宏在 FMS 2022 發表 FortiX，目標是在 flash 晶片內做 AI 運算 | "FortiX technology for AI-focused computation inside flash chips" | https://blocksandfiles.com/2022/08/12/macronix-compute-in-storage-story/ | 2022-08-12 | 高 |
| FortiX NAND 具備記憶體內搜尋（IMS）功能 | "FortiX NAND having an in-memory search (IMS) function"（可做關鍵字搜尋與 Hamming 距離近似搜尋） | 同上 | 2022-08-12 | 高 |
| 當時仍在開發階段：96 層 FortiX 3D NAND，以及 32 層 3D NOR | "developing 96-layer FortiX 3D NAND with a 64Gbit die in prospect" / "developing a 3D NOR flash variant with 32 layers" | 同上 | 2022-08-12 | 高（2022 年的狀態）；之後是否量產、是否用於 RAG：**未查證** |
| 旺宏與 IBM 合作 3 年，標的是**企業級 SSD**，不是 CIM 或 PCM | 「旺宏董事會決議通過與 IBM 為期三年的企業級固態硬碟儲存(SSD)合作開發計畫，時間自 2023 年 12 月 31 日至 2026 年 12 月 30 日，旺宏支付研發費用及權利金。」 | https://finance.technews.tw/2023/12/27/macronix-wz-ibm/ | 2023-12-27 | 中（只看到搜尋摘要，未開啟全文） |
| 旺宏與 IBM 的 PCM 合作 | **本輪未查證** | — | — | — |
| 世芯（Alchip）參與 d-Matrix Raptor 的 3D DRAM 與封裝（見 Q1） | 見 Q1 | hwbusters | 2026-08-24 | 中 |
| 工研院有 CIM 低功耗 AI 晶片研究（udn 報導，未標日期，沒有提到業者） | 「傳統運算架構需不停在處理器和記憶體之間搬運資料，耗時也耗能；CIM省去頻繁搬運資料的動作」 | https://udn.com/news/story/7240/8943969 | 不詳 | 中 |
| 力旺、晶心、智原或台灣新創是否提供 CIM 晶片或 CIM IP | **未找到任何可查證來源** | — | — | — |

---

#### Q5. 學術地位（ISSCC）

| 事實 | 原文引述 | URL | 日期 | 信心 |
|---|---|---|---|---|
| ISSCC 2025 整體錄取論文數：中國 92、美國 55、韓國 44（這是全部論文，**不是只算 CIM**） | 「中国の採択数は92件と、続く米国（55件）、韓国（44件）に大きく差をつけた。」 | https://eetimes.itmedia.co.jp/ee/articles/2412/02/news047_2.html | 2024-12-02 | 高 |
| ISSCC 2026 整體錄取：中國（含港澳）96 篇，占 257 篇的 37.35%；美國 56、韓國 46 | （數字由擷取結果整理）；另有「清华大学、华为海思的相关论文聚焦存算一体芯片架构优化」 | https://finance.sina.cn/2026-02-28/detail-inhpkhws7078009.d.html?vt=4 | 2026-02-28 | 中（二手媒體） |
| 同一篇稱 AI 加速器與 CIM 合計占 ISSCC 2026 論文 35% 以上 | 「AI加速器与存算一体（CIM）成为绝对主流，占据本届会议论文总数的35%以上」 | 同上 | 2026-02-28 | 低（定義寬鬆，兩類合計） |
| 另一說法：ISSCC 2025 的 CIM「退潮」，在非記憶體類 session 只剩兩篇 | 「存算一體（CIM）技術的悄然退潮…今年在非儲存類Session中僅留下兩篇論文」 | https://hao.cnyes.com/post/140150 | 2025-03-16 | 低（作者為 RexAA，屬自媒體；擷取出的句子不通順） |
| 張孟凡（Meng-Fan Chang）曾任台積電 Corporate Research 處長，同時是清大特聘教授 | "Director, Corporate Research of TSMC and Distinguished Professor, National Tsing Hua University, Taiwan" | https://tlwarc.hg.gatech.edu/node/665598 | 2023-02-14（演講日期） | 高（2023 年時的頭銜）；目前職位未查證 |
| 張孟凡的研究重點是 CIM macro | "embedded volatile and nonvolatile CIM macros designed for multiplication-accumulation (MAC) operations" | 同上 | 2023-02-14 | 高 |
| 張孟凡 1997–2001 年在台積電 DSD 設計嵌入式 SRAM 與 Flash | "From 1997 to 2001, he designed embedded SRAMs and Flash in Design Service Division (DSD) at TSMC" | https://www.ee.nthu.edu.tw/~mfchang/i_biography.html | 頁面未標日期 | 高 |
| 2018 年清大記憶體設計實驗室有 3 篇 ISSCC 入選，含非揮發記憶體內運算電路 | "The NTHU Memory Design Lab team led by Professor Zhang Meng-Fan has 3 papers selected by ISSCC" | https://web.ee.nthu.edu.tw/p/16-1175-130741.php?Lang=en | 2018-01-02 | 高 |
| **ISSCC 中「只算 CIM」的各國論文數（台灣、中國、韓國、美國）：沒有找到任何統計或分析** | — | — | — | 無法證實 |
| **台灣在 ISSCC 2025／2026 的整體論文數：本輪沒有取得** | — | — | — | 無法證實 |

---

#### 無法驗證／矛盾資訊

**無法驗證**
- 以下廠商的製程節點或代工廠沒有查到：EnCharge EN100、Axelera Europa、Sagence、知存（WTM2101、WTM-8）、後摩（H30、M50）。
- Rain AI 與 Samsung 的 CIM 產品本輪沒有查。
- d-Matrix Corsair 是否已量產出貨：只看到一則二手標題。
- 台積電是否以設計支援、IP 或 OIP 形式把 DCIM 提供給客戶：網頁上沒有明確陳述，技術論壇與 OIP 資料也沒有取得。
- 聯發科量產產品採用 CIM：沒有找到任何證據。
- 旺宏 IMS／FortiX 之後的量產狀態與 RAG 應用、旺宏與 IBM 的 PCM 合作：都未查證。
- 力旺、晶心、智原或台灣新創的 CIM IP：沒有找到。
- ISSCC 中只算 CIM 的國別統計，以及台灣的 ISSCC 總篇數：沒有找到。
- 台積電 ISSCC 2021（22nm）與 2022（5nm）DCIM 論文：我記得有，但本輪沒有查證，不應引用。
- 我記得 Mythic 所用的 Fujitsu 三重 300mm 廠後來成為聯電子公司 USJC。這個說法本輪**沒有查證**，不應當作事實引用。

**矛盾或需要留意**
- **CIM 在 ISSCC 的熱度兩說相反：** cnyes 自媒體稱 2025 年 CIM「退潮、非記憶體類 session 只剩兩篇」，新浪稱 2026 年「AI 加速器與 CIM 占 35% 以上」。兩者年份、統計口徑與分類方式都不同，不能直接比較，兩項都只給低信心。
- **2026 年的統計來自二手媒體：** 中國 96 篇、占 37.35% 是新浪財經轉述，還沒有對照 ISSCC 官方的 press kit。
- **Raptor 與 Alchip 合作的出處：** 「2025 年 11 月宣布」只見於 hwbusters，沒有取得 d-Matrix 或 Alchip 的原始新聞稿。
- **中國廠商資料多為自我宣稱：** 知存「出貨超過一千萬顆」與後摩「國內首款」都是公司說法經中國媒體轉述，沒有獨立查證。

## 研究助理查核報告（子代理，模型產出，非使用者訊息）

#### 新興記憶體 CIM：台灣橋接角色事實查核（查核日 2026-10-07）

**方法說明（請先讀）：** 所有引文都是用 WebFetch 取得。這個工具會先經過一個小模型做擷取，因此「原文引述」大多是逐字擷取，但無法百分之百排除少量改寫。要放進簡報的關鍵數字，建議再開原頁核對，尤其是台積電年報、AIP、imec。

---

##### Q1. 台積電嵌入式 RRAM／MRAM

**1a. RRAM 已量產節點與 12/6nm 進度**
- 事實：40、28、22nm RRAM 已量產；12nm 消費級已完成技術驗證，車用級驗證中；6nm 進入開發。
- 原文：「The Company's 40nm, 28nm and 22nm nodes entered volume production and completed the technical qualification of 12nm consumer-grade RRAM, the 12nm automotive grade qualification is currently underway while 6nm node also entered development stage.」
- URL：https://investor.tsmc.com/static/annualReports/2025/english/pdf/2025_tsmc_ar_e_ch5.pdf
- 日期：2025 年報，2026 年發布（確切發布日未查）
- 信心：高

**1b. N12e 與 22nm RRAM 的驗證**
- 事實：N12e RRAM 於 2025 年通過消費級量產驗證；22RRAM 於 2025 年通過 100K cycle 驗證。
- 原文：「N12e® RRAM technology service, TSMC's third generation of resistive random-access memory (RRAM) solution… passed consumer grade qualification for production in 2025.」
- 原文：「22RRAM technology, TSMC's second generation of RRAM technology, passed the 100K-cycle qualification in 2025…」
- URL、日期：同 1a
- 信心：高

**1c. MRAM**
- 事實：16nm MRAM 於 2025 年通過車用級驗證；12nm 車用 MRAM 與 5nm 高速 MRAM 開發中。
- 原文：「In 2025, TSMC successfully completed the qualification of 16nm automotive-grade MRAM… TSMC is simultaneously developing 12nm automotive-grade MRAM and 5nm high-speed MRAM」
- URL、日期：同 1a
- 信心：高

**1d. 早期量產時間點（背景）**
- 原文：「we actually have brought both resistive RAM and MRAM to real production at both the 40nm and 22nm nodes.」
- URL：https://www.eenewseurope.com/en/tsmc-offers-22nm-rram-taking-mram-on-to-16nm
- 日期：2020-08-25
- 信心：高（屬發言轉述）

**1e. 台積電自身的 CIM 研究**
- 事實：年報列有 RRAM+SRAM 異質 CIM 邊緣 AI 處理器，以及 16nm gain-cell CIM macro。
- 原文：「mixed-precision, heterogeneous resistive random-access memory (RRAM) and static random-access memory (SRAM) compute-in-memory (CIM) AI edge processor」
- URL、日期：同 1a
- 信心：中（年報未寫明是哪一場會議發表）

**1f. 大學 shuttle**
- 事實：大學 shuttle 計畫於 2025 年擴及 7nm。
- 原文：「In 2025, TSMC expanded this industry-academia collaboration to include 7nm technology…」
- URL、日期：同 1a
- 信心：高
- 未能驗證：shuttle 或 MPW 是否開放 RRAM/MRAM 選項給大學或新創。

---

##### Q2. 台積電鐵電、氧化物半導體、2D 材料研究

**2a. IEDM 2024 論文**
- 鐵電：台積電 Chun-Chieh Lu 為第一作者，「Demonstration of Ferroelectric FET Memory with Oxide Semiconductor Channel to Achieve Smallest Cell Area 0.009 μm² and High Endurance for Non-Volatile High-Bandwidth Memory Applications」
- 氧化物半導體：「Enhancement-mode Atomic Layer Deposited W-doped In₂O₃ Transistor at 55 nm Channel Length by Oxide Capping Layer with Improved Stability」
- 2D 材料：
  - 「Stacked Channel Transistors with 2D Materials: an Integration Perspective」
  - 「Low-Power CMOS Inverter with Enhancement-mode Operation and Matched VTH at VDD = 1 V on Monolayer 2D Material Channel」
  - 「Bilayer Alloy Contacts for High-Performance p-Type 2D Semiconductor Transistors」
- MRAM：「MRAM Design-Technology-System Co-Optimization for Artificial Intelligence Edge Devices」
- URL：https://research.tsmc.com/chinese/collaborations/events/IEDM2024.html
- 日期：IEDM 2024（2024 年 12 月）
- 信心：高

**2b. SOT-MRAM**
- 事實：年報列有「Type-C spin-orbit torque MRAM (SOT-MRAM) that featured for the first time a circular-shaped magnetic tunnel junction」。
- URL、日期：同 1a
- 信心：中

**2c. 2025–2026 年的論文：** 未能驗證（台積電研究網站的 IEDM2025 頁面回傳 404）。另外，FeRAM 1T1C 與 IGZO 記憶體在 2025–2026 年的台積電發表，也都未查到。

---

##### Q3. 工研院

**3a. 與台積電合作 SOT-MRAM**
- 事實：合作開發 SOT-MRAM 陣列晶片，可用於記憶體內運算，論文在 IEDM 發表。
- 原文：「自旋軌道轉矩磁性記憶體（SOT-MRAM）陣列晶片，搭配創新的運算架構，適用於記憶體內運算」
- 原文：「功耗僅為自旋轉移力矩磁性記憶體（STT-MRAM）的1%」
- 原文：「兼具低功耗及10奈秒高速工作等優點」
- URL：https://www.cna.com.tw/news/ait/202401170041.aspx
- 日期：2024-01-17
- 信心：高
- 注意：報導日期是 2024 年 1 月，發表場合應為 IEDM 2023（2023 年 12 月），不是 2024 年的會議。

**3b. 12 吋試產線：經費、時程、節點**
- 原文：「總經費約37.72億元」
- 原文：「建物預計2027年12月完工」
- 原文：「2028年第一季起陸續啟用」
- 原文：「提供28至90奈米後段製程研發與試產服務」
- URL：https://www.ctee.com.tw/news/20260211700066-439901
- 日期：2026-02-11
- 信心：高

**3c. 12 吋試產線：研究範疇**
- 原文：「量子運算、矽光子、客製化晶片(ASIC)、整合型 3D 架構與下世代記憶體等前瞻技術」
- 原文：「台積電，不僅慷慨捐贈關鍵半導體設備，還派出專業團隊，提供最頂尖的建廠諮詢與技術指導」
- URL：https://technews.tw/?p=1512042
- 日期：2026-02-10
- 信心：高
- 限制：只寫「下世代記憶體／新型記憶體」這類泛稱，沒有點名 MRAM、FeRAM、RRAM 模組。

**3d. 工研院 FeRAM／FRAM 技術：** 未能驗證，沒有找到一手來源。

---

##### Q4. 國研院半導體中心（TSRI）

**4a. ACED Fab 計畫數與分工**
- 事實：共 6 件，學校為台大、成大、中興；TSRI 協助下線驗證；為期三年。
- 原文：「台大、成大、中興大學共六件計畫獲得補助」
- 原文：「國研院台灣半導體研究中心也將協助下線驗證」
- 原文：「為期三年」
- URL：https://cdnfinance.technews.tw/2023/06/30/aced-fab-program-6/
- 日期：2023-06-30
- 信心：高

**4b. ACED Fab 期程與台大件數**
- 原文：「the NSC announced the selection of six projects, with four of them being led by teams from NTU」
- 原文：「2023-2026 Taiwan-US International Cooperative Research Program…」
- URL：https://www.ntu.edu.tw/english/spotlight/2023/2175_20230727.html
- 日期：2023-07-27
- 信心：高
- 6 件計畫題目都是電路與系統應用（深度學習、雷達、電源等），沒有看到新興記憶體元件。

**4c. TSRI 新建 12 吋研究場域**
- 原文：「計畫四年（2025-2028年）斥資79.76億元」
- 原文：「新建12吋半導體製造研究場域，並規劃與半導體業同等級無塵室設備」
- URL：https://www.ctee.com.tw/news/20250205700100-439901
- 日期：2025-02-05
- 信心：高

**4d. 學界可用 7nm（TN7）**
- 原文：「TSMC's 7nm process will soon be available for academic and research use」，標示為「TN7」，「only one batch open in the latter half of 2024」
- URL：https://apps.digitimes.com/news/a20240528PD213/tsmc-7nm-wafer-manufacturing-tsri.html
- 日期：2024-05-28（由 URL 推定）
- 信心：中（付費牆，只取得片段）

**4e. 未能驗證：**
- TSRI 每年 MPW 下線件數、開放的節點清單。
- ACED Fab 在 2025–2026 年的進度或結案資訊。

---

##### Q5. 台灣政策

**5a. 晶創台灣方案**
- 原文：「民國113年至122年投入3000億元經費」
- 原文（四大方向之一）：「推動加速異質整合及先進技術研發」
- 原文（新創支援）：「完成一站式從IC設計、晶片下線、測試，到最後雛型產品試製的pipeline」
- URL：https://www.cna.com.tw/news/ait/202401110164.aspx
- 日期：2024-01-11
- 信心：高

**5b. 115 年度晶創計畫徵求**
- 計畫名稱：「115 年度「晶創計畫：次世代半導體材料與元件整合關鍵技術」計畫徵求公告」
- 內文用語為「大面積半導體及二維材料」；全文沒有出現「記憶體／鐵電／記憶體內運算／異質整合」等字樣。
- URL：https://announce.yzu.edu.tw/files/rd/晶創計畫計畫徵求公告.pdf
- 日期：未標示
- 信心：中

**5c. 結論：** 沒有找到明文以「新興記憶體」或「CIM」為主題的國科會計畫，或專屬試產線。

---

##### Q6. imec 與 NanoIC

**6a. NanoIC 開幕與經費**
- 原文：「The facility represents a total investment of EUR 2.5 billion, of which EUR 700 million coming from EU funding, EUR 700 million from national and regional governments…」
- URL：https://evertiq.com/design/2026-02-09-eu-launches-nanoic-europes-largest-chips-act-pilot-line
- 日期：2026-02-09
- 信心：高

**6b. NanoIC 技術範疇與使用對象**
- 範疇：「semiconductor technologies beyond the 2nm node」
- 使用對象：「IDMs, foundries… start-ups, universities, and fellow European RTOs」
- URL：https://www.eejournal.com/industry_news/imec-inaugurates-nanoic-pilot-line-accelerating-innovation-in-sub-2nm-systems-on-chip/
- 日期：2026-02-09
- 信心：高

**6c. NanoIC 的 A14 邏輯與 eDRAM PDK**
- 原文：「both PDKs are freely accessible」，透過 Europractice 提供。
- URL：https://www.eejournal.com/industry_news/nanoic-extends-its-pdk-portfolio-with-first-a14-logic-and-edram-memory-pdk/
- 日期：2026-02-02
- 信心：高
- 未能驗證：這個 eDRAM 是否為 IGZO 架構。

**6d. imec 鐵電記憶體（VLSI 2026）**
- 原文：「vertically stacked IGZO-based ferroelectric field-effect transistors (FeFETs)」
- 原文：「first functional demonstration of a five-word-line vertical stack」
- 原文（FeCAP）：「low-voltage (~1.3 V) operation… remnant polarization (>40 μC/cm²) and endurance (≥10¹³ cycles)」
- URL：https://www.imec-int.com/en/press/imec-achieves-breakthroughs-ferroelectric-memory-research-next-generation-memory-solutions
- 日期：2026-06-17
- 信心：高
- 限制：imec 的 SOT-MRAM、IGZO 無電容 DRAM 在 2025–2026 年的計畫狀態，只出現在該頁的相關連結中，信心低。NanoIC 文件沒有提到 MRAM、FeRAM、RRAM。

---

##### Q7. CEA-Leti

**7a. 嵌入式 FeRAM 平台（IEDM 2024）**
- 原文：「a scalable hafnia-zirconia-based ferroelectric capacitor platform integrated into the back-end-of-line (BEOL) at the 22nm FD-SOI technology node」
- 原文：「functional 2D ferroelectric capacitors down to 0.0028µm², as well as 3D ferroelectric capacitors」
- 後續計畫：「explore a technology transfer to foundries」
- URL：https://www.eejournal.com/industry_news/cea-leti-demonstrates-embedded-feram-platform-compatible-with-22nm-fd-soi-node/
- 日期：2024-12-11
- 信心：高

**7b. FAMES 試產線**
- 經費：8.3 億歐元。
- 原文：「FD-SOI (with two new generation nodes at 10nm and 7nm), Several types of embedded non-volatile memories (OxRAM, FeRAM, MRAM and FeFETs)… Two 3D integration options (heterogeneous integration and sequential integration)」
- URL：https://www.cea.fr/cea-tech/leti/english/Pages/What's-On/Press%20release/cea-leti-announceslaunch-of-FAMES-pilot-line-as-part-of-EU-chips-act-initiative.aspx
- 日期：2024-06-11
- 信心：高
- 未能驗證：FAMES 在 2025–2026 年的進度。

---

##### Q8. GlobalFoundries 與 FMC

**8a. Fraunhofer IPMS 與 GF：22FDX 嵌入 FRAM**
- 事實：Fraunhofer IPMS 與 GF 共同將氧化鉿 FRAM 嵌入 GF 22FDX，並因此獲 Stifterverband 獎。
- 原文：「Successfully embedded ferroelectric FRAM cells into GlobalFoundries' 22FDX technology node」（此句為擷取工具的摘要，原文措辭待核對）
- URL：https://www.ipms.fraunhofer.de/en/press-media/press/2026/Ferroelectric-memory-storage.html
- 日期：2026-06-11
- 信心：中

**8b. FMC 現況與馬德堡廠計畫**
- 原文：「FMC had announced plans in the summer of 2025 for its chip factory (Fab) in the High-Tech Park Saxony-Anhalt」
- 原文：「These plans are contingent on financing. FMC is applying for funding」
- 原文：「FMC has secured another 100 million euros in funding」
- 原文：「FMC is cooperating with Globalfoundries on this」（指嵌入式鐵電記憶體）
- 原文：「FMC has not yet publicly disclosed precise technical specifications」（指 DRAM+／Cache+）
- URL：https://heise.de/-11151026
- 日期：未標示，內文提及 2025 年 12 月的事件
- 信心：中

**8c. FMC 與 Neumonda 合作 DRAM+**
- 原文：「a disruptive nonvolatile DRAM memory ideal for AI compute」
- URL：https://tech.yahoo.com/computing/articles/dram-memory-designed-dram-performance-112240423.html
- 日期：2025-04-08
- 信心：高

**8d. 未能驗證：**
- DRAM+ 8Gb 送樣。
- GF 以自家名義推出的 FeFET 22FDX／28nm 產品現況。
- FMC 在美國的設廠計畫。

---

##### Q9. Albany NanoTech／NY CREATES

**9a. 原本的規劃**
- 原文：「The EUV Accelerator, which will have initial operations available in 2025…」
- 原文：「Standard NA EUV expected by 2025 and high NA EUV in 2026.」
- URL：https://www.nist.gov/node/1865661
- 日期：未標示（2024 年內容）
- 信心：高（但屬取消前的資訊）

**9b. Natcast 經費被收回後**
- 背景：商務部長 Lutnick 收回 Natcast 的 74 億美元經費，改由 NIST 以廣泛徵求（broad solicitation）方式分配 NSTC 經費。
- 事實：AIP 在「R&D facilities canceled」小節中寫到，包含 Albany 在內的三座設施「will also not move forward」。
- 原文：「The Commerce Department and Natcast said they would initially spend up to $825 million to stand up the Extreme Ultraviolet Accelerator facility…」
- 原文：「NY Creates… noted that New York state had also committed $1 billion to expand the complex but did not answer further questions about how replacement funding would be secured.」
- URL：https://www.aip.org/fyi/trump-administration-overhauls-chips-r-d-plans
- 日期：2025-11-26
- 信心：中高（小節標題與引句經二次擷取）

**9c. 未能驗證：**
- 2026 年是否有替代經費或新的營運安排。
- Albany 是否支援學界做新興記憶體整合。

---

##### 無法驗證／矛盾資訊

1. **台積電 shuttle 是否含新興記憶體：** 沒有一手來源說明大學 shuttle 或 MPW 是否提供 RRAM/MRAM 選項，新創能否使用也查不到。
2. **台積電 2025–2026 年新論文：** 鐵電、IGZO、2D 方面查不到（IEDM2025 頁面回傳 404）。
3. **SOT-MRAM 的年份：** 題目寫「2024」，但實際發表在 IEDM 2023（2023 年 12 月），報導日期是 2024-01-17。
4. **工研院 12 吋線完工時間有兩種說法：**
   - 工商時報、TechNews：建物 2027 年 12 月完工，2028 年第一季起陸續啟用。
   - 優分析標題：「首條12吋試產線2028年完工」。
   - 差異應出在「建物完工」與「產線完工」的定義不同。
   - 經費：題目的 37.7 億，報導原文為「約37.72億元」。
   - 是否「承載特定新興記憶體模組」：只有泛稱「下世代記憶體」，無法確認。
5. **工研院 FeRAM 技術：** 沒有找到一手來源。
6. **TSRI：** 每年 MPW 件數、節點清單，以及 ACED Fab 在 2025–2026 年的進度都查不到。
7. **國科會專案：** 沒有找到明文以新興記憶體或 CIM 為主題的專案或專屬試產線。
8. **NanoIC eDRAM PDK：** 技術型態（是否為 IGZO 2T0C）未說明。
9. **FMC：** 8Gb 送樣找不到任何來源。heise 原文說 DRAM+ 的規格「not yet publicly disclosed」，與 8Gb 送樣的說法有張力。
10. **Albany 前後矛盾：** NIST 舊頁面仍寫「initial operations available in 2025」，與 AIP（2025-11）報導的「will not move forward」矛盾。NIST 頁面應已過時，但 2026 年的後續發展未能查證。

## Claude

我的看法：成熟CIM、PIM、新興CIM不是三題「要不要競爭」，而是同一個定位在三個成熟度上的不同做法。下面先講結論，再講怎麼論證，最後講每一塊的證據到哪裡為止。

#### 結論（研判）

**台灣在CIM的定位，是「記憶體與邏輯的整合層」。** CIM與PIM本質上都是把記憶體和運算放在一起，關鍵工作是製程整合與3D堆疊，台灣在這兩件事上已有實證。台灣不是新記憶體元件的主要研究投入者，這是美國學界；也不主導DRAM本體，這是韓國。三塊的位置如下：

- **成熟CIM**：台灣已經在競爭，產品端有聯發科，製造端有台積電。公共資源的角色是擴散給其他設計業者，不是扶植CIM晶片新創。
- **PIM**：不在DRAM本體和PIM標準品上正面競爭。台灣競爭的是記憶體旁的邏輯晶粒、3D堆疊和邊緣用的客製化記憶體。
- **新興CIM**：RRAM、MRAM可以論證「台灣有能力承接」。鐵電、氧化物、二維材料目前只能論證「具備基礎」，承接需要的公共整合平台和取用管道還沒到位。

#### 一、怎樣才算「有能力承接」：五個條件

要說「台灣有能力做某件事」，下面五個條件都要過。缺任何一個，只能說「有基礎」，不能說「有能力」。

| 條件 | 要回答的問題 | 用什麼證據 |
|---|---|---|
| 需求 | 這一步是否一定有人要做？何時要做？ | 研究端的進度、從研究到量產的時程 |
| 專屬能力 | 台灣有沒有這條路線專用的資產？不能只說「半導體很強」 | 量產製程、產品、研發成果 |
| 相對位置 | 和其他可能的承接地點比，台灣有什麼不同？ | 對手的平台與進度 |
| 可及性 | 需要的人能不能真的用到？ | 多專案晶圓服務（MPW）、合作計畫、開放程度 |
| 吸收能力 | 台灣自己的研究夠不夠參與共同開發？ | 研究件數與占比的趨勢 |

這個框架背後有兩個理論。以下是理論本身，不是資料推出的結論：

- **Teece（1986）的互補資產理論**：技術路線還沒收斂時，價值落在能低成本嘗試多條路線的一方；主流設計出現後，價值轉到擁有專屬製造資產的一方。成熟CIM接近後一階段，新興CIM還在前一階段，所以兩者的定位邏輯不同。
- **Cohen & Levinthal（1990）的吸收能力**：要承接別人的研究成果，自己要有相當的研究基礎。簡報第22頁已經用了這個概念。

論證時要避開四個常見漏洞：

1. **泛稱優勢**：「台積電很強」不等於「台積電能整合鐵電」。
2. **論文不等於服務**：台積電發表鐵電論文，不代表學界或新創用得到。
3. **使用不等於承接**：美國學界在台積電做晶片，不代表他們的研究將來在台積電量產。
4. **存在不等於優勢**：有能力不代表比別人強，論證時一定要擺上對手。

#### 二、成熟CIM（SRAM、快閃記憶體）

**事實：**

- **聯發科**：天璣9500於2025年9月發表，新聞稿說它是第一款為新增的Super Efficient NPU支援「整合式記憶體內運算架構」的晶片，已隨手機出貨〔聯發科新聞稿〕。新聞稿沒寫記憶體類型；TrendForce轉述工商時報，是放在SRAM的脈絡下討論〔TrendForce〕。
- **CIM新創的晶片在台積電製造**：
  - d-Matrix Corsair：6奈米〔ServeTheHome〕。
  - Axelera Metis：12奈米〔eeNews Europe〕。
  - d-Matrix下一代Raptor：邏輯晶粒用台積電N4，3D DRAM與封裝和世芯合作〔d-Matrix新聞稿〕〔Hardware Busters〕。
- **台積電自己的研究**：ISSCC 2024發表3奈米全數位CIM macro，用的是晶圓廠標準的6T SRAM記憶單元〔dblp〕。這表示數位CIM用標準SRAM就能做，擴散門檻相對低（研判）。
- **例外與對手**：
  - Mythic用富士通40奈米嵌入式快閃製程〔WikiChip〕。
  - 中國知存的NOR快閃CIM晶片，公司自稱出貨超過一千萬顆〔鈦媒體〕。
  - ISSCC整體錄取篇數中國居首：2025年中國92篇、美國55篇、韓國44篇〔EE Times Japan〕。但只算CIM的國別統計沒有找到。
- **沒有找到**：台積電把數位CIM當成IP提供客戶的公開說法；聯發科以外的台灣IC設計公司採用CIM的案例。

**定位（研判）**：問題不是要不要競爭，因為台灣已經在競爭，而且產品端和製造端都有位置。真正的問題是公共資源該放哪裡。

- NSF投在SRAM的經費只占2%，把成熟技術留給產業。台灣若用公共經費扶植CIM晶片新創，會和私人資本重疊。
- 依Teece的邏輯，成熟CIM的晶片市場不論誰勝出，多數在台積電製造，台灣已透過製造資產取得價值。
- 公共角色應是擴散：讓聯發科以外的中小IC設計公司（邊緣AI、穿戴裝置、微控制器）也能用上CIM，例如提供經驗證的CIM macro、編譯與設計工具、驗證平台。

**證據強弱**：產品與製造的證據強。擴散的需求和缺口目前是推論，還沒有直接資料，例如中小設計公司能否取得CIM macro。

**什麼情況會推翻這個定位**：CIM晶片廠大量轉到其他晶圓廠製造；中國的快閃CIM在台灣供應鏈之外持續擴大（已有跡象）。

#### 三、PIM（DRAM路線）

**事實：**

- **DRAM-PIM由韓國主導**：
  - Samsung在Hot Chips 2026發表LPDDR5X-PIM。據報導，第一個商用載體可能是自家4奈米AI PC加速器GAIA，最快2027年量產〔TrendForce〕。
  - SK hynix的AiMX加速卡在CES 2026仍是原型〔StorageNewsletter〕。
- **標準**：JEDEC表示LPDDR6-PIM標準「接近完成」（2026年4月）〔HPCwire轉JEDEC〕，由Samsung與SK hynix推動〔TrendForce 2024/12〕。沒有查到任何台灣廠商參與。
- **記憶體旁的邏輯晶粒在台灣製造**：
  - SK hynix的HBM4底層邏輯晶粒（base die）用台積電12奈米〔DIGITIMES〕。
  - 台積電的客製化HBM4E邏輯晶粒用N3P，並把原本在主晶片上的記憶體控制器移進這顆晶粒〔TrendForce〕。
  - Micron HBM4E的標準與客製邏輯晶粒都交給台積電，2027年量產〔Tom's Hardware〕。
  - Samsung用自家4奈米製造〔Samsung〕。
- **客製HBM的性質**：SK hynix定義為「把GPU、ASIC的部分功能整合進HBM底層邏輯晶粒」〔StorageNewsletter〕。這屬於近記憶體運算，不是嚴格定義的PIM，引用時要區分。
- **3D堆疊與台灣記憶體廠**：
  - 台積電SoIC第一代已量產〔TrendForce〕。
  - 華邦CUBE定位邊緣運算，公司說2027年後帶動成長〔科技新報〕。
  - 南亞科UltraWIO採混合鍵合，部分產品已試產〔工商時報〕。
  - 力積電以「3D AI Foundry」為主題展示晶圓堆疊DRAM〔自由時報〕。
  - 以上三家都沒有查到具名客戶。

**定位（研判）**：DRAM本體與PIM標準品需要DRAM製程和標準主導權，韓國明顯領先，台灣不在這裡正面競爭。台灣競爭的是記憶體旁的邏輯與堆疊：

- 三家HBM廠中，SK hynix與Micron的底層邏輯晶粒由台積電製造。
- 客製HBM正把運算功能往這顆晶粒移，PIM與近記憶體運算交會的地方，正好是晶圓代工的工作。
- 邊緣端則由華邦、南亞科、力積電做客製化堆疊記憶體。

這不是放棄競爭，而是選在台灣有資產的層次競爭。

**證據強弱**：底層邏輯晶粒的證據強；台灣記憶體廠的客製堆疊還在試產或展示階段，沒有客戶證據。

**缺口在標準**：LPDDR6-PIM定案後，聯發科等SoC業者會是採用方。台灣沒有參與制定，只能跟隨規格。

**什麼情況會推翻這個定位**：Samsung自製邏輯晶粒的垂直整合模式勝出；客製HBM的運算功能又回到主晶片。

#### 四、新興CIM：五個條件逐項檢驗

| 條件 | 證據 | 判定 |
|---|---|---|
| 需求 | NSF 2023–24年新元件計畫追查11件，0件進入晶圓廠。NSF年均增量約74%投入鐵電與磁性。依案例時程，進入晶片驗證約在2028年後（研判） | 成立 |
| 專屬能力：RRAM | 台積電40、28、22奈米RRAM已量產；N12e在2025年通過消費級驗證；6奈米開發中〔台積電年報〕。美國學界的RRAM-CIM晶片，有2個團隊在台積電製作 | 具備 |
| 專屬能力：MRAM | 台積電16奈米車用MRAM於2025年通過驗證，12奈米車用與5奈米高速MRAM開發中〔台積電年報〕。工研院與台積電合作的SOT-MRAM陣列適用記憶體內運算〔中央社〕。ACED Fab資助的SOT-MRAM論文有台積電、工研院共同作者 | 具備 |
| 專屬能力：鐵電 | 台積電在IEDM 2024發表氧化物通道鐵電電晶體，單元面積0.009平方微米〔台積電IEDM 2024〕，仍屬研發。國科會鐵電CIM計畫累計14件，多於NSF的12件 | 研發與學界有累積，沒有對外製程 |
| 專屬能力：氧化物、二維材料 | 台積電IEDM 2024發表原子層沉積的鎢摻雜氧化銦電晶體、二維材料堆疊通道〔台積電IEDM 2024〕，正好對應NSF資助的Purdue氧化銦研究 | 只有研發層級 |
| 相對位置 | 見下方說明 | 硬體投資規模相當，但台灣沒有指定記憶體模組；鐵電由歐洲領先 |
| 可及性 | 美國學界已在台積電做晶片；台積電大學shuttle於2025年擴及7奈米〔台積電年報〕。但ACED Fab台方6件計畫都是電路與系統題目，不是新興元件〔科技新報〕〔台大〕。嵌入式RRAM／MRAM是否開放學界與新創使用，查不到 | 部分具備 |
| 吸收能力 | 國科會元件層研究占比56%→40%（2025年45%）。鐵電計畫台灣每年約1.5件、持平；NSF由每年0.6件增至4.5件。晶創計畫115年度徵求聚焦大面積半導體與二維材料，沒有出現記憶體或CIM〔元智大學公告〕 | 有基礎，但沒跟上美國的加速 |

**相對位置的細節：**

- **歐洲**：
  - FAMES試產線（8.3億歐元）明列OxRAM、FeRAM、MRAM、FeFET等嵌入式記憶體模組，以及3D整合〔CEA-Leti〕。
  - imec的NanoIC試產線（25億歐元）於2026年2月啟用，開放給新創與大學〔Evertiq〕。
  - CEA-Leti已把鐵電電容整合進22奈米FD-SOI的後段製程，並規劃技轉給晶圓廠〔EEJournal〕。
  - Fraunhofer與GF已把鐵電記憶體嵌入GF的22FDX製程〔Fraunhofer〕。
- **美國**：Natcast經費被收回後，Albany原本規劃的NSTC EUV加速器聯邦經費前景不明〔AIP〕。
- **台灣**：
  - 工研院12吋試產線：37.72億元，2028年第一季起陸續啟用，提供28至90奈米後段製程服務〔工商時報〕。研究範疇含「下世代記憶體」與整合型3D架構，台積電捐贈設備並派團隊協助〔科技新報〕。
  - 國研院新建12吋研究場域：79.76億元，2025–2028年〔工商時報〕。

**判定（研判）：**

- **RRAM、MRAM**：可以論證「台灣有能力承接」。有量產級製程、有研發成果，美國學界也已經在用。
- **鐵電、氧化物、二維材料**：只能論證「具備基礎」。台積電有研發，國內學界也有累積，但三個條件還沒到位：
  - 試產線沒有明定要做哪些記憶體模組。
  - 學研單位能不能取用，管道不明。
  - 國內研究沒跟上美國這兩年的加速。
- 而NSF增量最大的鐵電，歐洲已經有明列模組的公共試產線。
- 所以「承接」最好寫成條件句：**若試產線明定新興記憶體模組、開放國際學研取用、並維持元件研究，台灣可承接。** 這三個條件，正好就是著力點。

**定位（研判）**：簡報第10頁指出記憶體路線還沒收斂，所以台灣不必押單一路線，可以做「多條路線都能整合驗證的平台」，讓不同新元件都能在台灣與CMOS整合驗證。這和Teece的邏輯一致：主流設計出現前，價值在能低成本嘗試多條路線的地方；主流設計出現後，由台灣的量產資產接手。

台灣和歐洲、美國研究型晶圓廠相比，可能的差異有兩點（研判，取決於試產線的實際規劃）：

- 試產線就在量產晶圓廠旁邊。
- 試產線的後段製程節點（28–90奈米），涵蓋台積電嵌入式RRAM、MRAM目前量產的40、28、22奈米中的兩個。

#### 五、把三塊串成一條論證

| 環節 | 內容 | 性質 |
|---|---|---|
| 前提一 | CIM與PIM都要把記憶體與邏輯整合，關鍵在製程整合與3D堆疊 | 事實 |
| 前提二 | 台灣在三塊都有整合能力的實證：聯發科CIM NPU已出貨、CIM新創在台積電製造；兩家HBM廠的底層邏輯晶粒由台積電製造；台積電嵌入式RRAM、MRAM已量產，美國學界在用 | 事實 |
| 前提三 | 台灣不是新元件研究的主要投入者（NSF加速、國科會元件層占比下降），也不主導DRAM-PIM（韓國） | 事實 |
| 推論 | 台灣的比較利益在整合層。政策重點是強化整合層，同時維持足以吸收新元件的研究 | 研判 |
| 必須同時承認的反證 | 中國快閃CIM在台灣供應鏈外出貨；Samsung垂直整合；歐洲的鐵電平台；美國自己的研究型晶圓廠 | 事實 |

這條論證可以直接接上簡報結語「推動前瞻技術邁向量產，是台灣的相對優勢所在」，只是把「相對優勢」具體化為「整合層」，並依成熟度區分三種做法。要不要放進簡報，你決定。

#### 六、查證時發現三處要修正的事實

這三處跟簡報或我前幾則的說法有關，明天前要處理：

1. **「聯發科已量產SRAM-CIM」**：聯發科新聞稿只寫「整合式記憶體內運算架構」，沒有寫SRAM。建議改講「聯發科天璣9500已在NPU採用記憶體內運算架構」。
2. **我上一則說「德國FMC已有8Gb產品送樣」**：只有一個二手來源；另一來源說FMC的規格尚未公開。請不要用，改講「Fraunhofer與GF已將鐵電記憶體嵌入22FDX」。
3. **Albany**：我上一則寫「2025年7月啟用NSTC EUV加速器」不完整。AIP（2025/11）報導，Natcast經費收回後，原規劃的三座NSTC設施都受影響，Albany的聯邦經費前景不明，加州與亞利桑那兩座則明確不再推進。簡報若只寫「亞利桑那、加州設施不推進」，可以補上Albany也受影響；講到Albany時，只說「紐約州研究型晶圓廠」。

Sources:
- 〔聯發科新聞稿〕[MediaTek Dimensity 9500（2025/9/22）](https://www.prnewswire.com/news-releases/mediatek-dimensity-9500-unleashes-best-in-class-performance-ai-experiences-and-power-efficiency-for-the-next-generation-of-mobile-devices-302562586.html)
- 〔TrendForce〕[NVIDIA's $20B Groq Deal Spotlights SRAM Shift—MediaTek NPU Already On Board（2025/12/30）](https://www.trendforce.com/news/2025/12/30/news-nvidias-20b-groq-deal-spotlights-sram-shift-mediatek-npu-already-on-board/)
- 〔ServeTheHome〕[d-Matrix Corsair at Hot Chips 2025](https://www.servethehome.com/d-matrix-presents-corsair-an-in-memory-computing-architecture-for-inference-at-hot-chips-2025/)
- 〔eeNews Europe〕[Axelera launches Metis（TSMC 12nm）](https://www.eenewseurope.com/en/axelera-launches-metis-in-memory-computing-ai-edge-cards/)
- 〔d-Matrix新聞稿〕[d-Matrix與世芯合作3D DRAM（2025/11/18）](https://www.d-matrix.ai/?p=2109)
- 〔Hardware Busters〕[d-Matrix Raptor（2026/8/24）](https://hwbusters.com/news/d-matrix-raptor-drops-the-memory-phy-32gb-at-100-tb-s-against-hbm4s-192gb-at-18/)
- 〔dblp〕[台積電ISSCC 2024 3奈米全數位CIM macro](https://dblp1.uni-trier.de/pers/hj86/c/Chih:Yu=Der)
- 〔WikiChip〕[Mythic（富士通40奈米）](https://fuse.wikichip.org/?p=2755)
- 〔鈦媒體〕[知存、後摩（2026/4/7）](https://www.tmtpost.com/7944130.html)
- 〔EE Times Japan〕[ISSCC 2025錄取篇數](https://eetimes.itmedia.co.jp/ee/articles/2412/02/news047_2.html)
- 〔TrendForce〕[Samsung GAIA與PIM商用化（2026/8/26）](https://www.trendforce.com/news/2026/08/26/news-samsungs-4nm-gaia-could-mark-first-pim-commercialization-in-ai-pcs-mass-production-as-early-as-2027/)
- 〔StorageNewsletter〕[SK hynix CES 2026](https://www.storagenewsletter.com/2026/01/07/ces-2026-sk-hynix-showcases-next-gen-ai-memory-innovation/)
- 〔HPCwire轉JEDEC〕[JEDEC LPDDR6 PIM（2026/4/22）](https://www.hpcwire.com/off-the-wire/jedec-previews-lpddr6-roadmap-expanding-lpddr-into-data-centers-and-processing-in-memory/)
- 〔TrendForce 2024/12〕[Samsung與SK hynix推動LPDDR6-PIM標準](https://www.trendforce.com/news/2024/12/02/news-samsung-and-sk-hynix-reportedly-unite-to-standardize-lpddr6-pim-for-on-device-ai/)
- 〔DIGITIMES〕[SK hynix HBM4採台積電12奈米base die](https://digitimes.com/news/a20260424VL208/sk-hynix-tsmc-hbm4-dram.html)
- 〔TrendForce〕[台積電C-HBM4E（N3P）（2025/12/1）](https://www.trendforce.com/news/2025/12/01/news-tsmc-unveils-custom-c-hbm4e-details-n3p-logic-dies-reportedly-target-2x-efficiency-gain/)
- 〔Tom's Hardware〕[Micron HBM4E base die交由台積電](https://www.tomshardware.com/micron-hands-tsmc-the-keys-to-hbm4e)
- 〔Samsung〕[Samsung HBM4（4奈米base die）](https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4)
- 〔TrendForce〕[台積電SoIC與CoWoS（2026/5/14）](https://www.trendforce.com/news/2026/05/14/news-tsmc-sees-ai-wafer-demand-rising-11x-from-2022-2026-targets-cowos-with-24-hbm-stacks-in-2029/)
- 〔科技新報〕[華邦CUBE（2026/8/6）](https://cdnfinance.technews.tw/2026/08/06/winbond-electronics-second-quarter-profit-hit-a-record-high/)
- 〔工商時報〕[南亞科UltraWIO（2026/3/5）](https://www.ctee.com.tw/news/20260305700104-430501)
- 〔自由時報〕[力積電3D AI Foundry（2026/5/26）](https://ec.ltn.com.tw/article/breakingnews/5449421)
- 〔台積電年報〕[台積電2025年報第五章（RRAM、MRAM、大學shuttle）](https://investor.tsmc.com/static/annualReports/2025/english/pdf/2025_tsmc_ar_e_ch5.pdf)
- 〔台積電IEDM 2024〕[台積電IEDM 2024論文列表](https://research.tsmc.com/chinese/collaborations/events/IEDM2024.html)
- 〔中央社〕[工研院與台積電合作SOT-MRAM（2024/1/17）](https://www.cna.com.tw/news/ait/202401170041.aspx)
- 〔工商時報〕[工研院12吋試產線（2026/2/11）](https://www.ctee.com.tw/news/20260211700066-439901)
- 〔科技新報〕[工研院試產線研究範疇（2026/2/10）](https://technews.tw/?p=1512042)
- 〔工商時報〕[國研院12吋研究場域（2025/2/5）](https://www.ctee.com.tw/news/20250205700100-439901)
- 〔科技新報〕[ACED Fab台方6件計畫（2023/6/30）](https://cdnfinance.technews.tw/2023/06/30/aced-fab-program-6/)
- 〔台大〕[ACED Fab台大團隊（2023/7/27）](https://www.ntu.edu.tw/english/spotlight/2023/2175_20230727.html)
- 〔元智大學公告〕[晶創計畫115年度徵求公告](https://announce.yzu.edu.tw/files/rd/晶創計畫計畫徵求公告.pdf)
- 〔CEA-Leti〕[FAMES試產線](https://www.cea.fr/cea-tech/leti/english/Pages/What's-On/Press%20release/cea-leti-announceslaunch-of-FAMES-pilot-line-as-part-of-EU-chips-act-initiative.aspx)
- 〔Evertiq〕[NanoIC試產線啟用（2026/2/9）](https://evertiq.com/design/2026-02-09-eu-launches-nanoic-europes-largest-chips-act-pilot-line)
- 〔EEJournal〕[CEA-Leti嵌入式FeRAM平台（2024/12/11）](https://www.eejournal.com/industry_news/cea-leti-demonstrates-embedded-feram-platform-compatible-with-22nm-fd-soi-node/)
- 〔Fraunhofer〕[Fraunhofer IPMS與GF 22FDX鐵電記憶體（2026/6/11）](https://www.ipms.fraunhofer.de/en/press-media/press/2026/Ferroelectric-memory-storage.html)
- 〔AIP〕[AIP FYI：CHIPS R&D計畫調整（2025/11/26）](https://www.aip.org/fyi/trump-administration-overhauls-chips-r-d-plans)
- NSF與國科會的件數、經費：簡報數據檔（C04）、國科會CIM計畫分類檔、NSF CIM計畫晶片製作地點追查檔
- 理論：Teece, D. J. (1986). Profiting from technological innovation. *Research Policy*, 15(6)；Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity. *Administrative Science Quarterly*, 35(1)

## 使用者

我們大框架分的三類，是算嚴謹的嗎?
也就是成熟CIM、PIM、新興CIM這樣

## Claude

不算嚴謹。這三類拿來口頭分組可以，但如果要撐「台灣定位」這種論證，有四個問題。核心問題是三類用了兩種不同的分類標準，還和簡報自己的定義互相矛盾。

#### 一、四個問題

**1. 一個分法裡用了兩種標準（事實）**

「成熟／新興」分的是商業化階段；「PIM」分的是運算位置或記憶體類型。標準不同，三類就不互斥，舉三個例子：

- DRAM 路線本身就有不同成熟度：三星 LPDDR5X-PIM 已在樣品階段，鐵電 DRAM（FMC 的 DRAM+）和 3D DRAM 還在研發。後者該歸「PIM」還是「新興CIM」？按現在的分法說不清楚。
- 鐵電可以嵌在邏輯晶片裡（GF 22FDX、CEA-Leti 的後段製程 FeRAM），也可以做成獨立記憶體（SK hynix 的 FeNAND）。同一種材料，會跨兩類。
- 有些東西找不到歸屬：客製 HBM 的底層邏輯晶粒、d-Matrix Raptor 把 DRAM 疊在邏輯晶粒上、旺宏的 NAND 記憶體內搜尋。上一則我把前兩者硬塞進 PIM，其實不精確。

**2. 「新興CIM」把「新型記憶體」和「不成熟」綁在一起（事實）**

RRAM 當記憶體已經量產：台積電 40、28、22 奈米都在量產。不成熟的是「拿它來做 CIM」這個用途。所以「成熟／新興」要明說指的是 CIM 應用的成熟度，不是記憶體本身。簡報先前討論第10、11頁時，已經把這個區分講清楚，三分法的名稱卻又把它模糊掉了。

**3. 「成熟CIM」內部差異很大（事實）**

- SRAM-CIM 是數位式，業者有聯發科、d-Matrix、Axelera，都在台積電生產。
- 快閃 CIM 多為類比式，業者有中國的知存（自稱出貨超過千萬顆）和 Mythic（富士通 40 奈米嵌入式快閃）。

兩者的產業結構和台灣的位置不同，放在同一類，會把差異蓋掉。

**4. 和簡報自己的定義衝突，也和文獻不一致（事實）**

- 第8頁按運算位置分：PIM 是「把運算單元放進記憶體晶片」，CIM 是「直接在記憶陣列裡運算」，兩者並列。
- 核心頁卻把 DRAM（三星 LPDDR5X-PIM）列為 CIM 的一條記憶體路線，等於 PIM 屬於 CIM。
- 文獻常見的用法正好相反。Mutlu 等人把 PIM 當總稱，底下分兩種做法：「processing-using-memory」利用記憶體晶片的類比原理就地運算，接近一般說的 CIM；「processing-near-memory」把運算邏輯放在記憶體旁邊，包括 3D 堆疊。照這個定義，是 CIM 屬於 PIM。
- 業界用詞也不統一：三星把自家 DRAM 產品叫 PIM，ISSCC 電路社群把陣列內運算叫 CIM。

所以，如果台上把「成熟CIM、PIM、新興CIM」當三個並列類別，有人問「PIM不就是CIM的一種嗎？」，簡報本身前後就答不一致。

#### 二、三分法其實有一個對的地方

三類背後真正在分的，是「記憶體由誰製造」：

- SRAM 用邏輯製程，由晶圓代工主導。
- DRAM 用獨立記憶體製程，由記憶體大廠主導，主要是韓國。
- 新型非揮發記憶體目前在研究階段，加上晶圓代工的嵌入式製程。

上一則的定位論證，靠的正是這個維度，不是成熟度。所以問題出在名稱和標準沒講清楚，不是方向錯了。

#### 三、三種改法

**方案A：按記憶體類型分，和核心頁一致**

分成 SRAM、快閃、DRAM、新型非揮發記憶體（RRAM、MRAM、鐵電）四類，成熟度改成每類的屬性，不再當類別名稱。

- 優點：只用一種標準，四類互斥；和核心頁、NSF 資料的編碼一致，數字直接能用；明天不用改任何資料。
- 缺點：四類而不是三類；近記憶體整合（底層邏輯晶粒、3D 堆疊）只能附在 DRAM 底下；看不出「誰製造」這個真正驅動定位的因素。

**方案B：兩個維度，「記憶體在哪種製程製造」×「CIM應用的階段」**

| | 已量產或樣品 | 研究階段 |
|---|---|---|
| **嵌在邏輯製程中**（晶圓代工主導） | SRAM-CIM（聯發科、d-Matrix、Axelera）、嵌入式快閃 CIM（Mythic） | RRAM、MRAM、鐵電的嵌入式 CIM（台積電嵌入式製程與研發、CEA-Leti、GF） |
| **獨立記憶體製程**（記憶體大廠主導） | DRAM-PIM（三星 LPDDR5X-PIM）、NAND 記憶體內搜尋 | 3D DRAM、鐵電 DRAM 與 NAND（FMC DRAM+、SK hynix FeNAND） |
| **兩列之間的介面**（近記憶體整合） | 客製 HBM 的底層邏輯晶粒（台積電為 SK hynix、Micron 代工）、3D 堆疊（SoIC、世芯與 d-Matrix 合作） | 疊在邏輯晶粒上的新型記憶體 |

- 優點：
  - 每個維度只用一種標準，「PIM是不是CIM」的爭議自然消失，因為不再拿這兩個詞當類別。
  - 列這個維度直接解釋台灣的定位（研判）：台灣強在第一列和兩列之間的介面，弱在第二列，而且成熟或新興都一樣弱。
  - 上一則「整合層」的定位，就是第一列加上介面。
  - 鐵電被拆成兩條路徑，可以看出台灣能競爭的是嵌入式鐵電，獨立式鐵電記憶體幾乎沒有台灣的位置。這比上一則「鐵電由歐洲領先」更精確。
- 缺點：
  - 比較抽象，台上要多一頁說明。
  - NSF 和國科會的資料沒有按「嵌入式或獨立式」編碼，例如 NSF 的 FeNAND 計畫屬獨立式，其他鐵電計畫多屬嵌入式。要用這個分法放數字，得重新分類，明天前做不到。
  - 少數案例的歸屬需要再查。例如知存的 NOR 快閃是嵌入式還是獨立製程，我沒有查證。

**方案C：按運算位置分，和第8頁一致**

分成記憶陣列內（CIM）、記憶體晶片內（PIM）、記憶體旁（近記憶體）三類。

- 優點：技術上最乾淨，和第8頁、Mutlu 的文獻定義一致。
- 缺點：和產業結構、成熟度都對不上，定位論證要另外接；也和 NSF 資料的編碼方式不一致。

#### 四、建議（研判）

- **明天的簡報**：用方案A的名稱，資料和核心頁都不用動。口頭上不要說「成熟CIM、PIM、新興CIM」，改說「SRAM與快閃（已量產）、DRAM（PIM，樣品階段）、新型非揮發記憶體（研究中）」。另外準備一句定義來應付問答：「本報告依記憶體類型區分CIM路線；三星稱為PIM的DRAM產品，在此歸為DRAM路線。」
- **之後寫成報告或論文時**：用方案B。它把「台灣強在嵌入式與整合介面、弱在獨立記憶體」講成一個結構性的論點，比按成熟度分更經得起推敲。代價是要把兩邊計畫重新編一次「嵌入式或獨立式」，鐵電是最需要重編的一類。

Sources:
- [Mutlu et al., A Modern Primer on Processing in Memory（arXiv 2012.03112）](https://arxiv.org/abs/2012.03112)（PIM 兩種做法的定義）
- [台積電2025年報第五章](https://investor.tsmc.com/static/annualReports/2025/english/pdf/2025_tsmc_ar_e_ch5.pdf)（RRAM 量產節點）
- [CEA-Leti 嵌入式FeRAM平台（EEJournal, 2024/12）](https://www.eejournal.com/industry_news/cea-leti-demonstrates-embedded-feram-platform-compatible-with-22nm-fd-soi-node/)
- [Fraunhofer IPMS與GF 22FDX鐵電記憶體（2026/6）](https://www.ipms.fraunhofer.de/en/press-media/press/2026/Ferroelectric-memory-storage.html)
- [FMC DRAM+（Yahoo Tech, 2025/4）](https://tech.yahoo.com/computing/articles/dram-memory-designed-dram-performance-112240423.html)
- [Semiecosystem：Next-Gen Ferroelectric Memory（2026/2）](https://marklapedus.substack.com/p/next-gen-ferroelectric-memory-still)（SK hynix FeNAND）
- [Samsung LPDDR5X-PIM（SammyFans, 2026/8）](https://www.sammyfans.com/2026/08/25/samsung-unveils-lpddr5x-pim-dram/)
- [Mythic（富士通40奈米嵌入式快閃，WikiChip）](https://fuse.wikichip.org/?p=2755)
- [知存WTM2101（鈦媒體, 2026/4）](https://www.tmtpost.com/7944130.html)
- [旺宏FortiX記憶體內搜尋（Blocks & Files, 2022/8）](https://blocksandfiles.com/2022/08/12/macronix-compute-in-storage-story/)
- 第8頁與核心頁的定義：簡報內容稿與講稿

## 使用者

A和B兩種分法會怎麼影響到我們後續的論證?

## Claude

簡單說，A 決定資料怎麼呈現，B 決定結論怎麼推出來。

- **A（按記憶體類型分）**：美國端的證據鏈完全不用動。但台灣定位只能逐項列出各類現況，再歸納出「整合層」，所以比較容易被質疑是挑案例。
- **B（記憶體在哪種製程製造 × CIM 應用階段）**：定位可以從產業結構直接推出來，結論更明確，尤其是鐵電。代價是資料要重新分類，還要回應「這個框架是不是替台灣量身打造」的質疑。

兩者不必二選一，用法放在最後。

#### 一、對每一段論證的影響

| 論證環節 | 用 A | 用 B |
|---|---|---|
| 美國端核心發現：NSF 投入方向與量產進度相反 | 不受影響。核心頁本來就是按記憶體類型、依成熟度排序 | 結論不變，因為反向關係在成熟度這一軸。新增的一個觀察見下方第 4 點 |
| 成熟 CIM 的定位 | SRAM 和快閃分成兩列。快閃那一列會露出缺口：台灣的證據只有旺宏 FortiX，2022 年仍在開發；有量產的是中國知存。台上得回答「快閃 CIM 台灣在哪裡」 | 快閃依做法拆開：嵌入式快閃（如 Mythic）歸邏輯製程那一列；獨立式快閃（3D NAND CIM）歸獨立記憶體那一列。台灣在後者較弱，有結構上的理由可以解釋 |
| PIM 的定位 | 只能放在 DRAM 那一列，台灣的角色變成附註「在邏輯端」。HBM 底層邏輯晶粒歸哪一類說不清楚 | DRAM-PIM 屬「獨立記憶體 × 已量產或樣品」，台灣不在這格，在兩列之間的介面。底層邏輯晶粒自然有位置，「不在 DRAM 本體競爭」也成了推論結果，不是主觀選擇 |
| 新興 CIM 的定位 | 拆成 RRAM、MRAM、鐵電三小列，跟第 10 頁一致。結論：RRAM 和 MRAM 可以論證有能力承接，鐵電只具備基礎 | 鐵電再拆成嵌入式和獨立式。結論變成：台灣可以競爭的是嵌入式鐵電，對手是歐洲研究型晶圓廠和 GF；獨立式鐵電記憶體（FeNAND、DRAM+）不是台灣的戰場 |
| 政策著力點 | 對應現有第 23 頁的研究端、銜接端、量產端，結構不用改 | 著力點改依格子排列：嵌入式新興記憶體的整合平台、嵌入式成熟技術的擴散、介面（邏輯晶粒、3D 堆疊、標準）、研究吸收能力。獨立記憶體那一列只列為觀察對象 |
| 「整合層」總結 | 歸納法：逐項看完，再總結台灣的資產集中在代工和整合 | 演繹法：整合層本身就是框架的一個軸，定位從結構推出 |

#### 二、B 會多出一個 A 看不到的發現（研判，初步）

我按標題把 NSF 的 12 件鐵電計畫初步分了類：

- **明確屬嵌入式、或標榜可做在晶片後段製程的，5 件**：後段製程鐵電電容、在 CMOS 上整合 FeFET、Purdue 氧化銦平台、Ferro-CoDE、高效能鐵電記憶體（CAREER 計畫）。
- **明確屬獨立式的，1 件**：鐵電垂直 NAND。
- **從標題判斷不了的，6 件**：二維鐵電材料、模型框架、應用導向的題目。

如果這個比例在細讀摘要後還成立，就代表 NSF 增量最大的鐵電路線，主要押在嵌入式這一格。這一格要靠晶圓代工承接，所以台灣和 NSF 這筆投資的相關性，比 A 呈現的更高。同時也更清楚，台灣在這格的對手是歐洲：CEA-Leti 已有後段製程 FeRAM 平台，GF 與 Fraunhofer 已把鐵電記憶體做進 22FDX。

這只是看標題的初判，要放進論證之前，得逐件讀摘要確認。

#### 三、各自會被怎麼追問

**用 A 時：**

1. 「為什麼台灣在 SRAM 強、在 DRAM 弱？」A 只能列出事實，說不出原因。
2. 「RRAM 台積電早就量產了，為什麼算離量產最遠？」要靠「這裡講的是 CIM 應用的成熟度」這個定義來回答，定義必須先講清楚。
3. 「HBM 底層邏輯晶粒算哪一類？」A 沒有對應的位置。

**用 B 時：**

1. **「你用台灣強的維度來分類，再推出台灣強，是不是循環論證？」** 這是 B 最大的風險。回應有兩層：
   - 這個維度和台灣無關，是產業結構本身。嵌入式記憶體由晶圓代工當作製程選項提供，例如台積電的 RRAM、MRAM；獨立記憶體由記憶體廠用自有製程生產。
   - 這個框架同樣標出台灣弱的格子，也就是整個獨立記憶體那一列，不是只挑對台灣有利的部分。
2. **「簡報的數字是按記憶體類型算的，B 的格子沒有數字。」** 確實如此，要等重新分類後才補得上。
3. **邊界案例怎麼歸？** 快閃、鐵電、把 3D DRAM 疊在邏輯晶粒上這幾類，都需要判斷。分類規則要事先寫明：依實作方式分，不依材料分。

#### 四、要多做多少工作

- **A**：零。
- **B**：比想像中少，只有兩類需要逐件重新分類。其餘可以直接對應：SRAM 一定是嵌入式；DRAM 一定是獨立式；RRAM 和 MRAM 的 CIM 研究以嵌入式為主（研判，依台積電嵌入式製程與學界晶片的追查結果）。

| 需要重新分類的 | NSF | 國科會 |
|---|---|---|
| 鐵電 | 12 件 | 14 件 |
| 快閃 | 少數幾件 | — |

#### 五、建議用法（研判）

讓兩者分工：A 負責描述，B 的「製造位置」負責解釋。

- 資料照 A 呈現，核心頁、經費數字都不動，這是資料本來的分類方式。
- B 不拿來當類別，而是當解釋變數：說明台灣為什麼在某些類型有位置、在某些類型沒有。

這樣同時拿到 A 的資料一致性和 B 的解釋力，又不必把整份資料重新分類。循環論證的質疑也比較小，因為 B 是在事後解釋已經呈現的資料，不是預先替台灣劃好的格子。

時間上這樣安排：

- **明天的報告**：簡報不改，只在口頭結論加一句：「台灣的能力集中在以邏輯製程製造記憶體，以及記憶體與邏輯的整合；這說明了台灣為何在 SRAM 和嵌入式新型記憶體有位置，在 DRAM 本體則不在。」
- **之後寫報告**：完整採用 B，把鐵電和快閃重新分類，並把「嵌入式鐵電是台灣可以競爭的格子」當成一個需要檢驗的命題來寫。

Sources:
- NSF 鐵電計畫標題：本研究資料檔 nsf_cim_annotated_v1_1.csv（依標題初判）
- [CEA-Leti 嵌入式 FeRAM 平台（EEJournal，2024/12）](https://www.eejournal.com/industry_news/cea-leti-demonstrates-embedded-feram-platform-compatible-with-22nm-fd-soi-node/)
- [Fraunhofer IPMS 與 GF 的 22FDX 鐵電記憶體（2026/6）](https://www.ipms.fraunhofer.de/en/press-media/press/2026/Ferroelectric-memory-storage.html)
- [台積電 2025 年報第五章（嵌入式 RRAM、MRAM）](https://investor.tsmc.com/static/annualReports/2025/english/pdf/2025_tsmc_ar_e_ch5.pdf)
- [旺宏 FortiX（Blocks & Files，2022/8）](https://blocksandfiles.com/2022/08/12/macronix-compute-in-storage-story/)
- [知存 WTM2101（鈦媒體，2026/4）](https://www.tmtpost.com/7944130.html)

## 使用者

可以先跟我分析，目前而言，我們整體的論證脈絡是什麼嗎?
最後得到了什麼結果

## Claude

整體來說，這套論證分三層：先看美國 NSF 把錢投在哪裡，再和台灣國科會的同類計畫對照，最後檢驗台灣的能力、推出台灣的定位。前兩層大多有資料直接支撐；第三層的核心是推論，所以最後得到的是有條件的定位，不是「台灣可以承接」這種無條件的主張。

#### 一、論證脈絡

**研究問題：** 美國 NSF 對 AI 晶片的科研投資，在記憶體內運算（CIM）上呈現什麼趨勢？這對台灣有什麼意義？

##### 第一層：美國端（以 NSF 資料為主）

1. **現象**：NSF 的 AI 晶片經費在 2023 年達到高峰；各技術路線中，CIM 成長最快。〔事實〕
2. **背景**：AI 晶片的瓶頸已從運算轉向資料搬運，CIM 是把運算移到資料所在處。CIM 已有量產產品，但記憶體路線還沒收斂。〔事實〕
3. **方向**：NSF 的 CIM 經費往材料與元件移動，增幅最大的是鐵電（年均 74→364 萬美元）和磁性（27→237 萬美元）。〔事實〕
4. **轉折**：年均增量中約八成，流向還沒規劃做出實體晶片的研究。〔事實；依計畫摘要判讀，反映的是規劃而非成果〕
5. **核心發現**：NSF 的投入和量產進度方向相反。已量產的 SRAM 只占 2%，還在研究階段的新型非揮發記憶體占 61%。〔事實〕
6. **成因**：美國各資助者之間有分工。有明確市場的由私人資本推動，現有製程的應用由 DARPA 承擔，NSF 負責最前端。〔研判，沒有直接檢驗〕
7. **距離**：從研究到量產，近年案例多需 5 年以上。論文追查發現，NSF 2023–24 年 11 件新元件計畫中，0 件進入晶圓廠，元件都還在大學實驗室。〔事實〕

##### 第二層：台美對照（國科會 62 件對 NSF 60 件）

8. **起步**：台灣較早投入，CIM 占 AI 晶片計畫的比重在 2021–22 年就到 43%，之後回落到 26%。美國每年的 CIM 計畫數增為 2.4 倍，台灣大致持平。〔事實〕
9. **相同處**：兩地押注的方向一致，新興記憶體都約占六成。〔事實〕
10. **差異處**：美國轉向材料與元件研究（37%→55%），台灣同期下降（56%→40%，2025 年回到 45%）。〔事實；台灣 2023–24 年只有 15 件，樣本小〕

##### 第三層：台灣定位（最近幾輪討論的內容）

11. **檢驗「承接」說法**：
    - 追查發現，美國學界能確認製作地點的晶片，5 個團隊中有 4 個用台積電。〔事實〕
    - 但只看新興記憶體的 CIM 晶片，台積電 2 個團隊、美國 Albany 研究晶圓廠 2 個團隊，各半。〔事實〕
    - 所以「台灣是新興 CIM 的承接者」這種強說法撐不住。〔研判〕
12. **路線差異**：NSF 增量約 74% 在鐵電與磁性。台灣有銜接實績的 RRAM，只占增量約 11%。〔事實〕
13. **能力檢驗**：用五個條件逐一檢查——需求、專屬能力、相對位置、可及性、吸收能力。
    - RRAM、MRAM 五項都過：台積電有量產製程，美國學界也在使用。
    - 鐵電、氧化物、二維材料只到「具備基礎」：台積電有研發，但工研院試產線沒有明定要做哪些記憶體模組，學研取用管道不明，國內研究也沒跟上美國這兩年的加速。歐洲則已有明列模組的公共試產線。〔事實與研判混合〕
14. **分段定位**〔研判〕：
    - **成熟 CIM**：台灣已經在競爭，聯發科天璣 9500 的 NPU 採用 CIM 架構，CIM 新創的晶片在台積電製造。公共資源的角色是擴散，不是扶植晶片新創。
    - **PIM**：DRAM 本體與 PIM 標準由韓國主導。台灣的位置在記憶體旁的邏輯晶粒和 3D 堆疊——台積電為 SK hynix、Micron 代工 HBM 底層邏輯晶粒。
    - **新興 CIM**：有條件的承接者。
15. **總論點**：台灣在 CIM 的位置是「記憶體與邏輯的整合層」。〔研判〕
16. **分類修正**：「成熟 CIM／PIM／新興 CIM」混用了兩種分類標準。建議資料照記憶體類型呈現；另用「記憶體由誰製造（邏輯製程嵌入，還是獨立記憶體製程）」解釋台灣為何在某些類型有位置、某些沒有。〔研判〕

#### 二、層與層之間的接點

這套論證最容易被打的地方，在層與層的銜接處。

| 接點 | 需要的前提 | 支撐程度 |
|---|---|---|
| 第一層 → 第三層 | NSF 的前端研究日後需要和邏輯製程整合，而台灣可能參與這一步 | 部分成立。新元件確實還沒進晶圓廠，美國學界也已在用台積電；但在新興記憶體上，美國也有本土的 Albany |
| 第二層 → 研究端著力點 | 要承接別人的研究，自己要有相當的研究基礎（吸收能力） | 理論成立（Cohen & Levinthal）；資料顯示台灣元件研究占比下降，但台灣樣本小 |
| 能力 → 定位 | 五個條件都成立，才能說「有能力承接」 | RRAM、MRAM 成立；鐵電等只有部分成立，所以結論必須寫成條件句 |
| 各段定位 → 整合層總論點 | 台灣的資產集中在邏輯製程與整合，而這正是 CIM 和 PIM 需要的 | 每一段都有事實支撐，但目前是歸納出來的。改用「記憶體由誰製造」當解釋變數後，才算有結構上的理由 |

第一層第 6 點（資助者分工）一直是研判，沒有直接檢驗。其他可能的解釋也存在，例如 NSF 本來就以基礎研究為使命，或是 FuSe 等計畫的設計本身就偏向材料。簡報已標為研判，問答時要準備這一題。

#### 三、最後得到的結果

**一句話總結（研判）：** NSF 把 CIM 經費集中在離量產最遠的新元件，尤其是鐵電與磁性。這些元件要走到量產，需要和邏輯製程整合，時間大約在 2028 年以後。台灣的能力集中在記憶體與邏輯的整合層，所以台灣的定位是「整合層」；對下一代新興 CIM，則是「有條件的承接者」。

**按可信度分三級：**

| 層級 | 內容 |
|---|---|
| 已確立（事實） | 美國端第 1–7 點；台美對照的方向一致與研究層次分歧；追查結果（NSF 新元件 0 件進入晶圓廠、學界晶片的製作地點）；台積電嵌入式 RRAM、MRAM 量產；台積電代工 HBM 底層邏輯晶粒；聯發科 CIM 架構出貨；歐洲有明列模組的試產線 |
| 有條件成立（研判＋證據） | 台灣在成熟 CIM 與 PIM 邏輯端已有位置；RRAM、MRAM 有承接能力；整合層的定位 |
| 尚未證實 | 台灣能否承接鐵電、氧化物、二維材料。條件有三個，這三個條件本身就是著力點：試產線明定嵌入式新興記憶體模組、開放國際學研取用、維持元件研究的吸收能力 |

**這輪討論對原本結論的修正：**

- 原本「推動前瞻技術邁向量產，是台灣的相對優勢所在」，對成熟技術和 RRAM、MRAM 成立；對鐵電則是有待補足的條件。
- 「台灣擅長銜接」從一句概括，具體化為「整合層」。哪些已經成立、哪些還欠條件，現在可以分開講。

#### 四、還沒完成的部分

- **簡報**：第一、二層和第三層的骨架（研究端、銜接端、量產端三個著力點），簡報裡已有。第三層的細化——條件句、路線差異、整合層、分類方式——目前只在討論中，還沒進簡報。
- **之後寫報告要補的事**：
  1. 把鐵電與快閃計畫按嵌入式或獨立式重新分類。依標題初判，NSF 鐵電計畫以嵌入式為主，需要讀摘要確認。
  2. 查台灣中小 IC 設計公司能否取得 CIM 設計模組。
  3. 追蹤台灣在 JEDEC PIM 標準的參與情況。
  4. 追蹤工研院試產線最後納入哪些記憶體模組。
- **明天前要修正的三處事實**：
  1. 「聯發科已量產 SRAM-CIM」改為「CIM 架構」，因為新聞稿沒寫是 SRAM。
  2. 不要用「FMC 8Gb 送樣」，來源不足。
  3. 提到 Albany 時，不要說 NSTC 的 EUV 加速器仍在運作。

## 使用者

我發現第二層，也就是GRB那裏，對整體的論證是不是沒有什麼幫助

## Claude

你的感覺大致對。GRB（國科會計畫資料）這一層目前得出三個發現，只有一個真正撐住最後的結論。另外兩個，一個推論過度，一個和結論接不上。

不過它不是沒有用。它有一個別人取代不了的用途，目前還沒發揮出來。

#### 一、三個發現逐一檢查

| 發現 | 目前的用途 | 有沒有撐住結論 | 問題 |
|---|---|---|---|
| 台灣較早投入（2021–22年 CIM 占43%），之後回落；美國每年計畫數增為2.4倍 | 鋪陳「原本領先、被反超」 | 間接 | 這是時序描述，對「台灣定位在整合層」沒有直接作用。回落的原因也沒有檢驗：只知道時間上和半導體射月計畫重疊，晶創台灣方案的效果還沒進入資料 |
| 兩地新興記憶體都約占六成 | 推論「公私分工可能不只是美國的現象」 | 沒有 | 推論過度。公部門研究偏重新興記憶體，不等於存在分工。要證明分工，需要台灣私部門的對照資料，我們沒有 |
| 美國轉向材料與元件層，台灣同期下降（56%→40%，2025年回到45%） | 支撐研究端的著力點（吸收能力） | 有，三個裡唯一一個 | 樣本小（2023–24年只有15件），以件數計算，2025年又回升 |

#### 二、為什麼會這樣：衡量的層次對不上（研判）

GRB 衡量的是國科會這一個資助者的研究投入。但最後的結論是「台灣在產業鏈中處於整合層」，這個結論的主要證據來自台積電、聯發科、工研院，不是 GRB。

所以 GRB 能支撐的，只有結論裡跟公共研究有關的那一塊，也就是五個條件裡的「吸收能力」。把它當成和美國端平行的「台美對照」來講，篇幅和它對結論的貢獻不成比例，聽眾就會覺得這一段和前後接不上。

#### 三、它能撐、但目前沒用到的地方

**1. 判斷台灣的缺口在哪一段（事實＋研判）**

- 國科會的鐵電 CIM 計畫累計14件，比 NSF 的12件多，其中11件規劃做到元件原型。
- 但台灣沒有對外提供的鐵電整合製程，工研院試產線也沒有明定鐵電模組。

所以台灣在鐵電的缺口在中段（銜接），不在研究端。這讓「試產線納入嵌入式鐵電模組」這個建議有了依據：上游已經有研究成果等著接。只看產業資料，說不出這一點。

**2. 按路線看吸收能力（事實）**

| 鐵電計畫件數 | 2018–22年 | 2023–24年 |
|---|---|---|
| 台灣（國科會） | 每年約1.6件 | 每年約1.5件 |
| 美國（NSF） | 每年0.6件 | 每年4.5件 |

台灣持平，美國在 NSF 增量最大的路線上大幅加速。這比「元件層占比下降」更具體，也直接對上第三層的路線分析。

**3. 一個可能的發現，但目前不能用**

依摘要判讀，規劃做到晶片層級的比例：

- 台灣：約18%（62件中11件）
- 美國：約37%（60件中22件）

如果這個差距成立，代表台灣的公共研究並沒有對準自己的整合優勢。但兩邊摘要的長度和編碼方式不同：台灣摘要較短，有10件沒寫成熟度。所以不能直接比較，暫時不要用。

#### 四、三種處理方式

**A：頁面不動，只改講法**
- 怎麼做：把第二層從「台美比較」改成「台灣研究端的條件檢驗」，講三點：
  1. 研究基礎存在：鐵電累計14件。
  2. 但沒有跟上美國的加速。
  3. 所以研究端是承接的條件之一。

  「公私分工不只是美國的現象」這句，如果還在頁面或講稿上，就刪掉。「台灣起步早」縮成一句帶過。
- 優點：明天就能用，GRB 的每個數字都對到結論。
- 代價：頁面標題可能仍是「台美比較」的框架，講法和頁面之間會有一點落差。

**B：之後寫報告時重新定位**
- 怎麼做：GRB 這一章改問「台灣的公共研究，是否對準台灣的定位？」，用上面三個用途作為證據，補上經費資料，並用一致的方式重新編碼兩邊摘要。
- 優點：GRB 從配角變成能撐住結論的證據。
- 代價：要補資料、重新編碼，明天來不及。

**C：從主論證移除，只留給問答**
- 優點：故事最精簡，只講美國端和台灣產業能力。
- 代價：
  - 吸收能力這個條件失去證據。
  - 「台灣學界的鐵電研究有累積」這句話也沒有依據。
  - 這場研討會談科技布局，聽眾很可能問「那台灣自己投資在哪裡」。你不放備用頁，這題只能靠口頭回答。

**我的判斷（研判）：** 明天用 A，之後的報告用 B，不建議 C。GRB 並不是多餘的，問題在於它被放在「平行對照」的位置，而它真正的用途是「台灣研究端的條件檢驗」。

資料來源：國科會 CIM 計畫分類檔（62件）、NSF CIM 計畫標註檔（60件）、簡報數據檔 C04 與 C09。件數均依本研究的分類。

## 使用者

先不要考慮明天簡報這件事情，我們以能夠做的最好的呈現為目標考慮就好。
我認為GRB作為平行對照，沒有充分發揮它的作用。
聽完的感覺像是，喔台灣也有在做，方向差不多但是比較早，阿然後呢?這代表什麼
有沒有更一步的差別，比如說，台灣看似更能夠做到試產驗證，是不是間接證明台灣在這種銜接層的能力更好?
或是同樣是以新型態記憶體為主，側重的技術方向有沒有差別，或是投注的情形之類的。
因為如果完全相同的話，感覺有一種講了等於沒講的感覺

## Claude

拆開比較後，兩邊確實有實質差異，而且這個差異能和整份論證接上。

一句話說：**兩邊都押新興記憶體，但美國把錢押在「發明新元件」，台灣把錢押在「用這些記憶體做電路、架構與晶片」。** 2023年後，這個分歧還在擴大。

你原本猜的「台灣更能做到試產驗證」，從計畫資料看不出來。真正的差別不在做不做晶片，而在錢投在研發鏈的哪一層。

以下比較國科會CIM計畫62件與NSF CIM計畫60件。研究層次（元件、電路、架構）兩邊用同一套編碼標準，經費依各自資料庫的名目美元。

#### 一、先回答「台灣是不是更能做試產驗證」

| | 規劃做到晶片（按件數） | 規劃做到晶片（按經費） |
|---|---|---|
| 台灣 | 18%（62件中11件） | 36% |
| 美國 | 37%（60件中22件） | 40% |

按經費兩邊差不多；按件數，美國反而較高。所以研究計畫的資料不支持「台灣較常做到晶片」（事實）。

另外，台灣摘要很短（中位數約285字），NSF摘要約3,000字元。我們依摘要判斷「規劃做到哪一步」，台灣這邊容易低估。這項數字本身就不適合拿來分高下。

#### 二、真正的差異

##### 1. 錢投在研發鏈的不同層（事實）

各層次占經費的比重：

| | 2018–22 元件層 | 2018–22 電路＋架構 | 2023後 元件層 | 2023後 電路＋架構 |
|---|---|---|---|---|
| 美國 | 35% | 38% | 58% | 11% |
| 台灣 | 32% | 47% | 36% | 62% |

2023年後，美國的錢大幅移向元件，台灣的錢更集中在電路與架構，方向正好相反。

**這裡要修正簡報原本的說法。** 「台灣元件研究占比下降（56%→40%）」是按件數算的。按經費算，台灣元件層一直持平在三成多，並沒有下降，是美國加碼了。所以「被反超」的框架不準確，應該改成「兩邊往不同層移動」。

敏感度檢查：台灣經費集中在少數大型計畫。拿掉經費最大的兩件磁性計畫（台大同一位主持人，合計約360萬美元）後，台灣電路＋架構仍占44%，美國全期為24%，差異依然存在。

##### 2. 磁性路線的對比最鮮明（事實）

| | 件數 | 經費 | 元件層占該路線經費 | 占本國CIM經費 |
|---|---|---|---|---|
| 台灣 | 8 | 733萬美元 | 17%（8件中僅1件是元件研究） | 31%，台灣最大的路線 |
| 美國 | 8 | 591萬美元 | 88% | 14% |

- 美國研究的是新的磁性元件：SOT-MRAM、STT輔助SOT、斯格明子賽道、磁域壁記憶體。
- 台灣研究的是拿MRAM做架構、電路與晶片。

研判：台積電已有量產的嵌入式MRAM，台灣的公共研究是在既有元件上做整合與應用。

##### 3. 有一組計畫直接對上（事實）

NSF的ACED Fab計畫（Stanford，研發新型MRAM），和國科會的「臺美半導體合作計畫」（台大劉致為，MRAM記憶體內運算晶片，美方夥伴是Stanford，國研院半導體中心也參與）是同一個合作案的兩端。

美方那端的SOT-MRAM論文，共同作者有台積電、工研院、陽明交大。這是資料中看得到的實例：美國做元件，台灣做晶片。

**這也要修正我前面的說法。** 我之前說「ACED Fab台方6件都是電路與系統題目，沒有新興元件」，這是錯的。台大的這一件就是MRAM記憶體內運算晶片。

##### 4. 鐵電：台灣件數多，但規模小、方向也不同（事實＋研判）

| | 件數 | 經費 | 單件中位數 | 占本國CIM經費 |
|---|---|---|---|---|
| 台灣 | 14 | 237萬美元 | 9.1萬美元 | 10% |
| 美國 | 12 | 1,099萬美元 | 75.5萬美元 | 26% |

元件形式也不同（依標題與摘要，我自己分類的，屬初判）：

- **台灣**偏向讓鐵電材料配合現有電晶體結構：
  - 鐵電穿隧接面4件（美國0件）
  - 鰭式或環繞閘極的鐵電電晶體3件
  - 可堆疊的多晶矽鐵電薄膜電晶體2件
- **美國2023年後的新計畫**偏向新材料與新堆疊方式：二維鐵電材料2件、氧化物半導體通道、後段製程鐵電電容、鐵電NAND。

研判：台積電在IEDM 2024發表的是氧化物通道鐵電電晶體，比較接近美國的方向，而不是台灣學界的主流方向。如果美國押的材料路線勝出，台灣學界在鐵電的研究累積，未必能直接接上。

另外，台灣在鐵電幾乎沒有做到電路或晶片層級的計畫。只有2025年一件3D鐵電穿隧晶片，經費約14萬美元。

##### 5. 經費結構不同（事實）

| | 單件中位數 | 低於10萬美元的計畫 | 前10大計畫占總經費 |
|---|---|---|---|
| 台灣 | 10.7萬美元 | 48% | 64% |
| 美國 | 59.1萬美元 | 0% | 34% |

台灣是「少數大型整合計畫，加上大量小額元件計畫」，美國是中型計畫平均分布。台灣的元件研究多半是單一主持人、兩年期的小額計畫。

**比較絕對金額時要保留**（研判，未逐項查證）：NSF經費含間接成本與人事費，國科會計畫一般不含主持人薪資、管理費比例也較低。所以「台灣237萬對美國1,099萬」這種絕對差距會被放大。比較穩健的是各國自己的內部比重，例如鐵電占台灣CIM經費10%、占美國26%。

##### 6. 公共資金通往產業的管道不同（事實＋研判）

- **台灣**：國研院（奈米元件實驗室、半導體研究中心）的研究人員親自主持4件CIM元件與3D整合計畫，國研院也是ACED Fab的合作單位。
- **美國**：有4件是新創公司申請的SBIR或STTR計畫。

研判：美國靠新創把研究帶向市場，而這些新創做晶片時用的是台積電；台灣靠國研院和晶圓代工把研究接到製程。

#### 三、這代表什麼

拆開比較後，第二層對整體論證有三個作用：

**1. 為「整合層」定位補上第二種證據。**
原本「台灣在整合層」只靠產業證據（台積電、聯發科）。現在台灣的公共研究也呈現同樣的分工：美國押發明，台灣押整合與應用。ACED Fab的MRAM計畫則顯示，這種分工已經在一個合作案裡實際運作（研判）。

**2. 把缺口定位得更精確。**
在台灣把錢投在整合的地方（磁性），有台積電量產製程撐著，分工運作得起來。在美國增量最大的鐵電，台灣三方面都不足：
- 元件研究的規模不足，而且多為小額計畫。
- 幾乎沒有整合型計畫。
- 元件方向和NSF、台積電的最新方向不一致。

所以前面說的「鐵電只具備基礎」，可以講得更具體：基礎是件數，缺的是規模、整合計畫和方向的對齊。

**3. 改寫研究端的建議。**
不是籠統地「增加元件研究」，而是「把鐵電研究集中成較大型、從元件做到陣列的計畫，對齊後段製程與氧化物通道的方向，並接到2028年的試產線」（研判）。

整個第二層的講法也跟著改：從「台灣也有做、方向差不多、比較早」，改成「**同一個方向，不同的位置；分工在磁性已經運作，在鐵電還沒形成**」。

#### 四、這些發現的限制

- **摘要長度不同**：研究層次的分類受摘要長短影響較小，但仍有影響；規劃成熟度受影響較大，所以前面不採用。
- **樣本小**：單一路線只有8到17件，結果容易被一兩件大型計畫左右。磁性路線已做過敏感度檢查。
- **鐵電元件形式是我手動分類的**：依標題和短摘要判斷，正式使用前應讀完整計畫書再確認。
- **經費成本結構不同**：見第二節第5點，應以各國內部比重為主。

#### 五、如果要做到最好的呈現（研判）

第二層可以用四張圖講完：

1. **兩國各層經費比重的前後期對照**：美國往元件移，台灣往電路與架構移。這是主圖。
2. **磁性與鐵電兩條路線的層次組成並排**：磁性顯示分工已經運作，鐵電顯示分工還沒形成。
3. **ACED Fab MRAM合作案**：一頁案例，美方元件、台方晶片，加上台積電與工研院的共同作者。
4. **鐵電的規模與方向差異**：作為第三層「缺口在哪」的引子。

這樣第二層就不再是平行對照，而是第一層（美國押元件）和第三層（台灣在整合層、缺口在鐵電）之間的橋。

資料來源：
- 國科會CIM計畫分類檔（62件）、GRB整合資料（研究層次為同一編碼標準的B_layer_primary）、NSF CIM計畫標註檔（60件），作者整理計算
- [台大焦點新聞：臺美ACED Fab計畫台大四件入選（2023/7/27）](https://www.ntu.edu.tw/spotlight/2023/2175_20230727.html)
- [Nature Electronics 2025：64kb SOT-MRAM（ACED Fab資助，台積電、工研院、陽明交大共同作者）](https://www.nature.com/articles/s41928-025-01434-x)
- [台積電IEDM 2024論文列表（氧化物通道鐵電電晶體）](https://research.tsmc.com/chinese/collaborations/events/IEDM2024.html)

## 使用者

那這對整體論證來說有什麼幫助?

## Claude

它的作用是：讓第二層從「平行描述」變成真正撐住結論的一環，而且還補上了整份論證原本最缺的東西——一個解釋機制。具體有四個作用，下面逐一說明，最後講它沒辦法做到的事。

#### 一、四個作用

**1. 讓「整合層」定位有了第二種、獨立的證據**

原本「台灣在整合層」只靠產業證據：台積電的嵌入式記憶體、聯發科的產品、代工 HBM 底層晶粒。批評者可以說這是挑幾家企業的案例。

現在有三種彼此獨立的資料，都指向同一個方向：

| 資料來源 | 顯示的事 | 性質 |
|---|---|---|
| 產業 | 台灣的資產集中在晶圓代工與整合 | 事實 |
| 論文追查 | 美國學界做晶片時，常在台積電製作 | 事實 |
| 公共研究經費 | 2023年後，台灣62%的經費投在電路與架構，美國58%投在元件 | 事實 |

三種資料互相印證，結論就比較難被說成是挑案例。ACED Fab 的 MRAM 合作案則讓這個分工有了一個看得見的實例：美方做元件，台方做晶片。

**2. 提供原本沒有的解釋機制**（這是最大的收穫，研判）

把三條路線並排，會出現一個規律：

| 路線 | 台積電有沒有量產製程 | 台灣公共研究的配置 | 美台分工 |
|---|---|---|---|
| 磁性（MRAM） | 有，嵌入式 MRAM 已量產 | 經費83%投在架構、電路與晶片；ACED Fab 是對應的合作案 | 已形成 |
| 電阻式（RRAM） | 有，嵌入式 RRAM 已量產 | 約一半經費投在兩件大型晶片計畫；美國學界的晶片也在台積電製作 | 已形成 |
| 鐵電 | 沒有對外製程，只在研發 | 幾乎全是小額元件計畫，沒有整合型計畫 | 尚未形成 |

由此可以提出一個假說：**台灣已經有某種記憶體的量產製程，公共研究才會往整合端配置，美台分工才會形成。**

這把原本零散的觀察串成一個因果邏輯，對建議也有直接意義。鐵電目前卡在一個循環裡：沒有製程，就沒有整合研究；沒有整合研究，就接不住美國的元件成果。工研院試產線之所以重要，是因為它是能打破這個循環的公共工具。這比原本「台灣有試產線，所以可以用」的理由強得多。

**3. 把缺口從模糊的條件變成具體的指標**

原本對鐵電的說法只是「具備基礎、條件不足」。現在可以講出三個可以衡量的缺口：

| 缺口 | 現況 |
|---|---|
| 規模 | 鐵電占台灣CIM經費10%，美國是26%；單件計畫的中位數，台灣約9萬美元，美國約76萬美元 |
| 整合計畫 | 只有一件小型晶片計畫 |
| 研究方向 | 台灣學界偏向鐵電穿隧接面、鰭式電晶體結構；美國和台積電的新研究偏向氧化物通道、二維材料 |

這三項之後都可以追蹤，也直接對應到研究端的建議。

**4. 修掉一個內部矛盾**

原本的說法是「台灣元件研究下降、被美國反超」，但結論又說「台灣可以承接」。一個研究在退步的國家要去承接別人的研究，前後說不通。

按經費重新計算後，台灣元件研究的比重其實持平（32%→36%），真正的變化是兩邊往研發鏈的不同層移動。說法從「落後」改成「分工」，矛盾就消失了，第二層和第三層的立場也一致了。

#### 二、整份論證前後的差別

| 環節 | 之前 | 之後 |
|---|---|---|
| 第一層（美國） | NSF押注元件 | 不變 |
| 第二層（台美對照） | 台灣也有做、方向差不多、比較早 → 聽眾問「然後呢？」 | 同一個方向，投在不同的層；分工在有量產製程的路線已形成 |
| 第三層（台灣定位） | 整合層，主要靠產業證據；新興記憶體寫成條件句 | 整合層，有三種資料互證；分工能不能形成，取決於台灣有沒有量產製程；缺口具體落在鐵電 |
| 建議 | 試產線、維持研究、標準參與，三項並列 | 試產線是打破鐵電循環的工具；研究端改為集中規模、對齊方向 |

改寫後的故事線（研判）：

> 美國NSF把CIM經費押在發明新元件，台灣的公共研究則押在用這些記憶體做電路與晶片。這種分工在台灣已有量產製程的磁性與電阻式記憶體上已經形成，ACED Fab就是實例；但在NSF增幅最大的鐵電，台灣沒有製程、沒有整合型計畫，元件研究規模小、方向也不一致，分工尚未形成。2028年啟用的試產線，是補上這一環的關鍵。

#### 三、它做不到的事

1. **相關不等於因果。**「有量產製程，公共研究才往整合端配置」是推論。另一種解釋是：台灣學界本來就以電路設計見長，所以經費自然偏向電路與架構。

   兩者可以這樣分辨：如果純粹是學界傳統，整合型計畫應該在三條路線都出現；實際上鐵電幾乎沒有。這個路線差異比較支持「量產製程先行」的解釋，但每條路線只有8到17件，只能算初步支持。正式寫作時，兩種解釋都要並列。

2. **看不出這是刻意的分工。** 資料只顯示兩邊各自的配置剛好互補，不代表美台有協調。ACED Fab 是唯一有制度設計的案例。

3. **受少數大型計畫影響。** 磁性路線的結果有一部分來自同一位主持人的兩件大型計畫。拿掉這兩件後，台灣電路加架構仍占44%，美國是24%。方向不變，但差距縮小。

4. **編碼限制仍在。** 台灣的摘要短；鐵電元件形式是我手動分類的；兩國經費的成本結構也不同，絕對金額會放大差距。所以論證應該以各國自己的內部比重為主。

這四點正式寫作時都要明列。其中第1點最重要，因為整個新增的解釋機制就建立在它上面。

## 使用者

我有點不清楚，這整個流程會是怎麼樣，就是NSF跟GRB到底在做什麼不同的事情，應該說我對於整個半導體從上到下的流程不是很了解

## Claude

圖中的百分比，是2023年後各自CIM經費的分布。

#### 一、一顆CIM晶片從無到有的四步

**第一步：發明新元件**（對應研究層次的「材料與元件層」）
在大學實驗室做出一顆新的記憶體元件。這一步問的是：它能不能存資料、能存幾種狀態、用多久會壞。成果是幾顆元件或小陣列，還不是晶片。

例如NSF資助的Purdue氧化銦電晶體、二維鐵電材料、新型SOT-MRAM。

**第二步：製程整合**（也就是我們一直說的「銜接」）
把新元件做進晶圓廠的標準製程，讓它能和數十億個電晶體做在同一片晶圓上，而且良率穩定。這一步只有晶圓廠或試產線做得到，通常要花好幾年。

整合出來的記憶體，叫「嵌入式記憶體」。它多半做在晶片的「後段製程」，也就是電晶體上方的金屬連線層之間。這就是為什麼工研院試產線提供「28到90奈米後段製程服務」很關鍵：新記憶體正是要做在這一層。

台積電已經替RRAM、MRAM完成這一步（事實）：

| 記憶體 | 台積電已量產的節點 |
|---|---|
| RRAM | 40、28、22奈米 |
| MRAM | 16奈米（車用等級） |

鐵電目前只在研發，還沒有對外提供的製程（事實）。

**第三步：電路與晶片設計**（對應「電路與架構層」）
有了製程，設計團隊才能在上面工作：

- **電路**：讀寫電路、類比與數位訊號轉換。
- **架構**：許多運算區塊怎麼排，AI模型怎麼放上去。

設計完成後「下線」，也就是把設計交給晶圓廠做出測試晶片。學界通常和其他團隊共用一片晶圓，台灣由國研院半導體中心代辦。

例如國科會資助的這幾件：

| 計畫 | 內容 |
|---|---|
| 台大吳安宇 | MRAM架構 |
| 中央大學謝易叡 | RRAM內容定址記憶體晶片 |
| 台大劉致為 | MRAM記憶體內運算晶片 |

**第四步：量產**
由企業把晶片做成產品，例如聯發科天璣9500的NPU，以及在台積電生產的d-Matrix晶片。

#### 二、NSF和國科會做的事有什麼不同

| | NSF | 國科會 |
|---|---|---|
| 經費主要投在 | 第一步：發明新元件（2023年後占58%） | 第三步：用既有記憶體設計電路與晶片（2023年後占62%） |
| 核心問題 | 下一代記憶體長什麼樣 | 現有的新型記憶體能做出什麼晶片 |

關鍵在於，第三步必須等第二步完成才做得到。沒有製程，就沒有東西可以設計晶片。

研判：台灣能把公共研究的錢放在第三步，是因為台積電已經替RRAM、MRAM完成了第二步。鐵電沒有第二步，所以台灣的鐵電研究只能停在第一步，而且多是小額計畫。這就是我們看到的路線差異。

ACED Fab合作案剛好把這條流程跨國串起來：

1. Stanford（NSF資助）做第一步：新型MRAM元件。
2. 那篇論文的共同作者有台積電、工研院，也就是負責第二步的單位。
3. 台大加上國研院（國科會資助）做第三步：MRAM記憶體內運算晶片。

#### 三、對回整份論證

| 論證環節 | 在這條流程上的位置 |
|---|---|
| 第一層：NSF押注離量產最遠的研究 | 錢集中在第一步 |
| 「銜接」需要晶圓廠 | 就是第二步，台灣的強項（台積電、工研院試產線） |
| 第二層：國科會的配置 | 錢集中在第三步，用已整合的記憶體做晶片，這就是「整合層」 |
| 缺口 | 鐵電卡在第二步。試產線的角色，是替還沒有商用製程的記憶體補上這一步 |

要補一句保留：實際研發不是嚴格單向的。電路設計常會回頭要求元件改進，也有計畫同時跨好幾步。這四步是為了看清分工而做的簡化，不是精確的時間順序。

## 使用者

我覺得這個流程感覺很不錯 有助於理解台灣跟美國的投資差異

## Claude

這張圖可以直接拿來當整份簡報或報告的主軸，因為它把三件原本分開講的事放上同一條線：

- 美國押注在哪裡：第一步，發明新元件。
- 台灣押注在哪裡：第三步，設計電路與晶片。
- 銜接為什麼重要：第二步，製程整合。

正式使用前，有三個地方要講精確，不然會被追問。

**1. 研究層次不等於做到哪一步。**
圖上的58%、62%，是按「研究做在哪一層」計算的。架構層的研究很多只做模擬，不一定真的下線做成晶片。前面算過，按經費計，規劃做到晶片的比重是台灣36%、美國40%，兩者差不多。所以圖上要標成「研究層次」，口頭上也不能說「國科會的計畫都在做晶片」。比較準確的說法是：國科會的錢多投在第三步這一層的研究。

**2. 圖中的比例都是2023年後的經費分布。**
2018–22年兩邊其實差不多，元件層都在三成左右。分歧是2023年後才出現的，這正好對應美國的晶片法案時期和FuSe計畫。這個時間點本身就是一個觀察，可以標在圖上。

**3. 「台灣能押第三步，是因為台積電完成了第二步」是推論。**
另一個可能的解釋是：台灣學界本來就以電路設計見長，所以經費自然偏向電路與架構。目前比較支持前一種解釋的證據，是路線差異：已有量產製程的磁性、電阻式記憶體，台灣都有整合型計畫；沒有製程的鐵電則幾乎沒有。但每條路線只有8到17件，正式寫作時兩種解釋都要並列。

如果要以這張圖當主軸，可以讓它在不同章節反覆出現，每次標亮不同位置：

| 章節 | 標亮的位置 | 要講的事 |
|---|---|---|
| 美國的投資 | 第一步 | NSF經費集中在離量產最遠的地方 |
| 研究到量產的距離 | 第二步 | NSF的新元件還沒有任何一件進入晶圓廠，中間要靠晶圓廠或試產線完成整合 |
| 台美對照 | 第一步與第三步 | 同樣押新興記憶體，投在不同的步驟；ACED Fab合作案把第一步和第三步連起來 |
| 台灣的定位與缺口 | 第二步的兩條路線 | RRAM、MRAM已完成整合，分工已經成形；鐵電卡在這一步，試產線的角色就在這裡 |

這樣聽眾只要記住一張圖，就能跟上整條論證，各章也不會像各講各的。代價是要用一頁先把四個步驟講清楚，大約一分鐘，而且前面幾章的圖要改成配合這條主軸的版本。

## 使用者

這對於整體論證的理解有什麼幫助呢

## Claude

它對理解的幫助在於：原本整份論證用了好幾套詞彙，各自講一個發現；這條四步流程把它們放到同一條線上，而且讓發現之間的因果關係看得見。具體有四點。

**1. 把好幾套抽象說法，統一成一條線上的位置**

我們一路用過「上游、前端、離量產最遠」「銜接」「研究層次（元件、電路、架構）」「成熟度（模擬、元件原型、晶片）」「整合層」。每個詞單獨聽都抽象，聽眾還得自己判斷它們之間是什麼關係。

放到四步流程上，每個詞都只是一個位置：

| 原本的說法 | 在流程上的位置 |
|---|---|
| 前端、上游、離量產最遠 | 第一步 |
| 銜接 | 第二步 |
| 整合層 | 第二步加第三步 |

聽眾只需要記住一張圖。

**2. 讓整份論證的關鍵前提被看見：第三步要等第二步完成才做得到**

這是整條論證的樞紐。沒有這張圖時，下面四件事是四個分開的發現；有了這張圖，它們都是同一個依賴關係推出來的結果：

- NSF的新元件還在實驗室，代表它們還沒過第二步，所以離量產遠。
- 台灣的強項在晶圓廠，代表台灣掌握的是第二步。
- 國科會的錢集中在第三步，因為只能在已經整合好的記憶體上設計晶片。
- 鐵電是缺口，因為它沒有第二步。

聽眾記住的不再是四個數字，而是一個機制。

**3. 讓聽眾自己推出結論**

圖上美國在第一步、台灣在第三步，中間隔著第二步。聽眾看到這個畫面，自然會問：「下一代記憶體的第二步，由誰來做？」

這正是我們要提出的政策問題。由聽眾自己問出來，比我們直接宣稱「台灣可以承接」更有說服力。這個問題也直接接上研討會的主題：第二步可能發生在台灣、美國 Albany，或歐洲的試產線，地點的競逐本身就是地緣政治的一部分。

**4. 讓結論的「條件」變得具體，也化解原本的矛盾**

- **條件變具體**：原本的「有條件承接」很抽象。在圖上它變成按路線回答的是非題：RRAM、MRAM 的第二步已經完成，鐵電還沒有。
- **矛盾消失**：原本「台灣元件研究被反超」和「台灣可以承接」聽起來衝突。放到流程上就說得通了：台灣本來就不主攻第一步，它站在第二步和第三步，這是分工，不是落後。

**這張圖做不到的事**

它是幫助理解的框架，本身不是證據，也不會讓資料更強。它還有一個風險：圖太整齊，會讓論證看起來比資料能支撐的更確定。前面提過的三個保留要一併交代：

- 研究層次不等於研發進度。
- 實際研發不是單向進行的。
- 「台灣押第三步，是因為台積電完成了第二步」仍是推論。

## 使用者

我覺得看起來不錯。
所以從這個框架的角度分析，台灣未來的方向到底是什麼?從我們剛剛討論的那個A和B的分法而言，怎麼結合起來進行總結

## Claude

結合 A 分法（記憶體類型）、B 分法（記憶體在哪種製程製造）和四步流程，結論是：台灣未來的方向，不是在第一步跟美國比發明新元件，而是三件事：

- 嵌入在邏輯晶片裡的記憶體，把第二步（製程整合）做成平台。
- 獨立製造的記憶體，守住它和邏輯晶片之間的介面。
- 所有路線，都把第三步（電路與晶片設計）擴散出去。

以下說明怎麼推出這個結論。

#### 一、三個工具各自回答一個問題

| 工具 | 回答的問題 | 在論證中的角色 |
|---|---|---|
| A：記憶體類型（SRAM、快閃、DRAM、新型非揮發記憶體） | 錢投在哪種記憶體、各自多成熟 | 資料的分類方式，核心頁和經費數字都按它 |
| B：記憶體在哪種製程製造 | 第二步由誰掌握 | 解釋台灣為什麼能在某些記憶體做第二步，在另一些不能 |
| 四步流程 | 研究在哪一步、卡在哪一步 | 讓投資差異和缺口看得見 |

B 是關鍵（事實＋研判）：

- **做在邏輯製程裡的記憶體**（嵌入式，例如 SRAM、RRAM、MRAM、嵌入式鐵電）：第二步由晶圓代工完成。這是台灣的地盤。
- **用獨立記憶體製程製造的**（DRAM、NAND、獨立式鐵電記憶體）：第二步由記憶體大廠用自己的製程完成，主要是韓國。台灣碰不到記憶體本身，只能做它和邏輯晶片之間的介面，也就是 HBM 底層的邏輯晶粒（記憶體堆疊最下面那一層）和 3D 堆疊。

所以合起來的規則是（研判）：**A 告訴我們錢在哪裡，B 告訴我們台灣能不能做第二步，四步流程告訴我們現在卡在哪一步。**

#### 二、總表：每一類記憶體，台灣站在哪裡、該往哪走

| 記憶體（A） | 製造位置（B） | 第二步現況 | 台灣現在的位置 | 未來方向（研判） |
|---|---|---|---|---|
| SRAM | 邏輯製程 | 早已完成 | 第三、四步：聯發科天璣 9500 採 CIM 架構；台積電代工 d-Matrix、Axelera | 擴散：讓更多台灣設計公司用得上 |
| DRAM | 獨立記憶體 | 韓國記憶體廠掌握 | 介面：台積電代工 SK hynix、Micron 的 HBM 底層邏輯晶粒；華邦、南亞科、力積電的客製堆疊記憶體試產中 | 守住介面，提早參與 PIM 標準 |
| RRAM、MRAM | 邏輯製程（嵌入式） | 台積電已完成並量產 | 第二、三步：國科會經費主力在這裡；ACED Fab 把美國的第一步接到台灣的第三步 | 深化承接：擴大 ACED Fab 這類合作，開放國際學研取用 |
| 嵌入式鐵電 | 邏輯製程 | 尚無人完成，歐洲領先（CEA-Leti、GF） | 只有小額的第一步研究，方向和 NSF、台積電不一致，幾乎沒有第三步 | 最優先補的缺口 |
| 氧化物、二維材料 | 邏輯後段製程（研判） | 尚無人完成 | 台積電有研發，學界零星 | 對齊研究方向，維持吸收能力 |
| 獨立式新型記憶體（FeNAND、DRAM+） | 獨立記憶體 | 記憶體廠掌握（SK hynix、德國 FMC） | 幾乎沒有 | 不是主戰場，只觀察 |
| 快閃 | 兩者皆有 | 嵌入式在日本等地，獨立式在記憶體廠 | 證據不足：旺宏 FortiX 2022 年仍在開發；量產者是中國知存 | 資料不足以下判斷，暫不列優先 |

#### 三、台灣的三個角色

**角色一：第二步的平台**（適用於做在邏輯製程裡的新型記憶體）

- **已具備**：RRAM、MRAM 有台積電量產製程；美國學界的晶片在台積電製作；ACED Fab 已有實例。
- **要補上**：嵌入式鐵電，以及氧化物和二維材料。工具是 2028 年啟用的工研院試產線，它提供 28 到 90 奈米的後段製程服務，正好對應嵌入式新型記憶體所在的那一層。
- **為什麼是多路線平台，而不是押單一路線**（研判）：路線還沒收斂。依 Teece 的互補資產理論，在主流技術出現之前，價值在能低成本嘗試多條路線的地方。這和歐洲 FAMES 試產線明列多種記憶體模組的做法一致。

**角色二：介面供應者**（適用於獨立製造的記憶體）

- 不在 DRAM 本體和 PIM 標準品上正面競爭，因為那需要記憶體製程和標準的主導權。
- 台灣守的是「記憶體旁的邏輯」：HBM 底層邏輯晶粒、3D 堆疊、邊緣裝置用的客製化堆疊記憶體。客製化 HBM 正把運算功能往底層晶粒移，這是 PIM 和晶圓代工交會的地方。
- **缺口在標準**：LPDDR6-PIM 由韓國主導，台灣廠商在定案後只能是採用者。

**角色三：第三步的擴散者**（適用於所有路線）

- SRAM-CIM 已經進入產品，公共資源不必扶植 CIM 晶片新創，那會和私人資本重疊。
- 公共資源應該讓聯發科以外的中小 IC 設計公司也能用上 CIM：經驗證的設計模組、設計工具、驗證平台。
- **保留**：這個方向目前缺直接證據，例如中小公司是否真的取得不到 CIM 設計模組，還需要查。

#### 四、優先順序（研判）

| 順位 | 項目 | 理由 |
|---|---|---|
| 1 | 嵌入式鐵電的第二步 | NSF 增量最大的路線；台灣三方面都不足（規模、整合型計畫、研究方向）；歐洲已有明列鐵電模組的公共試產線；美國 2023–24 年計畫進入晶片驗證約在 2028 年後，和試產線啟用時間吻合 |
| 2 | 深化 RRAM、MRAM 的承接 | 分工已經成形，成本最低、最容易見效。要確認台積電的嵌入式記憶體是否開放學界和新創使用，這一點目前查不到 |
| 3 | 第一步的研究：集中並對齊 | 不是全面增加元件研究，而是把鐵電研究整併成較大型、從元件做到陣列的計畫，對齊後段製程和氧化物通道的方向，接到試產線 |
| 4 | 介面與標準 | 產業已經在做，公共角色較小，主要是標準參與 |
| 5 | 第三步擴散 | 方向合理，但需要先補證據 |

#### 五、不建議做的事（研判）

- 在第一步和 NSF 比新材料的廣度。台灣的元件研究應該以「吸收得了、接得上」為目標，而不是比誰發明得多。
- 在 DRAM-PIM 標準品上正面競爭。
- 用公共經費培養 SRAM-CIM 的國家隊晶片公司。

#### 六、一句話總結（研判）

> NSF 押注的是第一步，台灣的優勢在第二步和第三步。做在邏輯製程裡的記憶體，台灣應把第二步做成多路線平台——RRAM、MRAM 已經做到，嵌入式鐵電是最該補的缺口；獨立製造的記憶體，台灣守住與邏輯晶片的介面；所有路線則把第三步擴散給更多設計業者。

#### 七、這個結論的保留

1. 「做在邏輯製程裡的，台灣才能做第二步」來自產業結構，本身站得住。但「台灣公共研究往第三步配置，是因為台積電完成了第二步」仍是推論，還有「台灣學界本來就擅長電路設計」這個替代解釋。
2. 嵌入式與獨立式的分法，還沒有套用到兩邊的計畫資料上。依標題初判，NSF 的鐵電計畫以嵌入式為主，但需要逐件讀摘要確認。如果結果相反，第一優先的判斷就要調整。
3. 試產線是否真的納入鐵電模組、國際學研能否取用，都還不確定。這兩點本身就是後續要觀察的訊號。

## 使用者

所以台灣在dram類沒什麼能力嗎

## Claude

不是沒有能力，而是能力的形態不同。我上一則說「台灣碰不到記憶體本身，只能做介面」，這句說得太重，要修正。

把「DRAM 能力」拆成四層來看，台灣在其中兩層很弱，在另外兩層有實績。

#### 一、四層 DRAM 能力

| 能力層次 | 台灣的位置 | 依據 |
|---|---|---|
| **1. 掌握先進通用 DRAM 與 HBM 記憶體晶粒的製程技術** | 弱 | 2026 年第二季全球 DRAM 營收：三星 39.4%、SK hynix 24.9%、美光 23.3%（TrendForce）。南亞科、華邦、力積電合計約 37 億美元，依 TrendForce 數字推算約占 2.4%（事實＋計算）。 |
| **2. 作為 DRAM 的製造地** | 強，但技術屬於美光 | 美光在台投資逾新台幣 1.6 兆元。台中是它在台最大的製造基地，涵蓋前段、後段、封裝測試和 HBM 生產（Focus Taiwan，2026/10/1）。在台產能占美光多少，報導沒有寫。 |
| **3. 客製化 DRAM，以及 DRAM 與邏輯的 3D 堆疊** | 有實績 | 見下方說明 |
| **4. 介面：HBM 底層邏輯晶粒與封裝** | 強 | 台積電為 SK hynix HBM4（12 奈米）和美光 HBM4E（2027 年）代工底層邏輯晶粒；CoWoS 和 SoIC 已量產；世芯與 d-Matrix 合作 3D DRAM。 |

**第 2 層的意思**：DRAM 製造的人才和供應鏈在台灣，但技術路線和產品決策在美光手上。這是「在台灣的能力」，不是「台灣企業的能力」，政策上要分開看。

**第 3 層的實績**：

- **愛普**（DRAM 設計與介面 IP）在 2021 年宣布 VHM 量產。VHM 是把 DRAM 和邏輯晶片做真正的 3D 堆疊，分工是愛普提供技術、力積電製造客製化 DRAM 晶圓、台積電製造邏輯晶片並完成堆疊，客戶是一家無晶圓廠公司（鉅亨網，2021/8/25）。2025 年愛普表示，已有多個 AI 高效能運算客戶案在設計導入（鉅亨網，2025/3/4）。
- **其他廠商**：
  - 南亞科 UltraWIO：採混合鍵合，部分產品試產。
  - 華邦 CUBE：鎖定邊緣裝置，公司說 2027 年後帶動成長。
  - 力積電：以「3D AI Foundry」展示 DRAM 晶圓堆疊，並取得美光的製程授權來擴產（TrendForce）。

#### 二、這對定位的修正

原本 DRAM 那一列只寫「守住介面」，應改成兩條路（研判）：

| 路線 | 誰主導 | 台灣的位置 |
|---|---|---|
| **標準化 PIM**（JEDEC 的 LPDDR6-PIM、HBM-PIM） | 韓國，掌握第 1 層製程和標準 | 主要是採用者 |
| **客製化近記憶體運算**（把客製 DRAM 疊在邏輯晶片上，如 VHM、CUBE、UltraWIO、d-Matrix Raptor） | 尚未定型 | 國內有完整分工：客製 DRAM（力積電、華邦、南亞科）、DRAM 設計 IP（愛普）、邏輯製造與堆疊（台積電）、晶片設計服務（世芯） |

客製化這條路是台灣在 DRAM 這一列真正的機會。

和最主要的對手比（研判）：三星同時擁有 DRAM 和晶圓代工，HBM4 用自家 4 奈米製作底層邏輯晶粒，走垂直整合。台灣則是多家公司分工的開放生態。哪一種模式勝出還不確定，這本身就是一個觀察訊號。

另外，兩邊的公共研究幾乎都不碰 DRAM 型 CIM：NSF 只有 3 件，國科會只有 1 件（事實）。這一列由產業主導，公共研究不是主要施力點。政府能做的，比較是標準參與和客製堆疊的驗證平台。

#### 三、要保留的地方

1. 客製堆疊路線還缺 AI 客戶證據。愛普 2021 年的量產客戶沒有公開產品類型；華邦、南亞科、力積電都沒有具名客戶。所以「台灣在客製化近記憶體運算有機會」目前是推論。
2. 台灣 DRAM 廠的部分製程來自美光授權（力積電），技術自主程度有限。
3. 邊緣裝置最後會採用標準化的 LPDDR-PIM，還是客製堆疊，還沒有定論。如果標準化路線勝出，台灣在這一列就主要是採用者和介面供應者。

修正後，總表的 DRAM 列：台灣現在的位置是「介面，加上客製化 DRAM 與邏輯 3D 堆疊（愛普 VHM 已量產，其他廠商試產或展示中）」；未來方向是「客製化 DRAM 與邏輯的 3D 整合，加上標準參與」。

Sources:
- [TrendForce：2Q26 DRAM 營收與市占（2026/9/7）](https://www.trendforce.com/presscenter/news/20260907-13219.html)
- [Focus Taiwan：美光在台投資逾 1.6 兆元（2026/10/1）](https://focustaiwan.tw/business/202610010013)
- [鉅亨網：愛普攜手力積電、台積電完成 VHM 量產（2021/8/25）](https://tw.stock.yahoo.com/news/%E6%84%9B%E6%99%AE%E6%94%9C%E6%89%8B%E5%8A%9B%E7%A9%8D%E9%9B%BB-%E5%8F%B0%E7%A9%8D%E9%9B%BB-%E5%AE%8C%E6%88%90vhmtm%E9%87%8F%E7%94%A2-%E5%AE%A2%E6%88%B6%E7%82%BA%E9%AF%A8%E9%8F%88%E7%A7%91%E6%8A%80-064955926.html)
- [鉅亨網：愛普 VHM 獲採用，首個 AI 高效能運算案設計中（2025/3/4）](https://news.cnyes.com/news/id/5881743)
- [科技新報：力積電推出 3D WoW 晶圓堆疊（2026/5/26）](https://technews.tw/2026/05/26/powerchip-technology-launches-3d-wow-wafer-stacking-technology/)
- [DIGITIMES：SK hynix HBM4 採台積電 12 奈米底層邏輯晶粒](https://digitimes.com/news/a20260424VL208/sk-hynix-tsmc-hbm4-dram.html)
- [Tom's Hardware：美光 HBM4E 底層邏輯晶粒交由台積電](https://www.tomshardware.com/micron-hands-tsmc-the-keys-to-hbm4e)
- [Samsung：HBM4 採自家 4 奈米底層邏輯晶粒](https://news.samsung.com/global/samsung-ships-industry-first-commercial-hbm4)

## 使用者

但是DRAM是不是跟這次簡報的主軸比較沒關係

## Claude

大致對。DRAM 不是這份簡報的主軸，但不能整個拿掉。它在論證裡只需要扮演一個角色。

#### 為什麼不是主軸（事實）

- 簡報的主軸是 NSF 把 CIM 經費押在哪裡，答案是新興記憶體（61%）。
- DRAM 在 NSF 的 CIM 經費只占 6%（3 件），國科會只有 1 件。兩邊的公共研究幾乎都沒碰。
- DRAM 型 PIM 由產業主導：三星的 LPDDR5X-PIM、JEDEC 的標準制定，都不是靠公共研究推動。

所以台灣在 DRAM 的能力（客製堆疊、HBM 底層邏輯晶粒），用的是產業資料，不是我們的核心資料（NSF、國科會、論文追查）。把它放進結論，等於讓結論超出證據能支撐的範圍。

#### DRAM 該保留的角色

1. **核心頁的一列。** DRAM 已經走向產品化，NSF 卻投入很少。這正好支持「投入與量產方向相反」和「公私分工」兩個論點。這是它在主論證裡唯一的功能。
2. **台灣定位裡的一句背景**，不再自成一個角色。例如：「成熟路線（SRAM、DRAM）由產業主導，公共資源的角色有限，主要是擴散與標準觀察。」
3. **問答準備。** 談 AI 晶片時，很可能有人問 HBM 或 PIM。上一則整理的台灣 DRAM 四層能力，適合當備答內容，或放進報告附錄。

#### 對上一版總結的修正

上一版把「介面供應者」列為台灣三個角色之一，範圍拉得太寬。應該重新聚焦（研判）：

- **主體**：嵌入式新興記憶體的第二步平台。RRAM、MRAM 已做到，嵌入式鐵電是缺口。這是 NSF 資料、國科會資料、論文追查三者共同指向的地方。
- **背景**：成熟路線由產業主導。SRAM 由台灣業者在第三、四步實際運作；DRAM 則由韓國主導，台灣在介面與客製堆疊有利基。公共資源在這兩條路線只做擴散與觀察，不另立主角。

修正後的一句話總結：

> NSF 押注第一步的新元件；台灣的優勢在第二、三步。對做在邏輯製程裡的新興記憶體，台灣應把第二步做成多路線平台——RRAM、MRAM 已經做到，嵌入式鐵電是最該補的缺口。成熟路線則由產業主導，公共資源以擴散為主。

簡報原本把「PIM 標準參與」列為量產端的著力點之一。依這個邏輯，它比較適合降為觀察訊號，不必和試產線、研究集中並列為主要建議。

## 使用者

因為主軸是要從美國觀察進行推演嗎?
我在想，那總共CIM的觀察應該要分成幾條路線?
SRAM、DRAM、快閃、新興記憶體?

## Claude

對，整份簡報的邏輯是「以美國 NSF 的投資為觀察起點，推演它對台灣的意涵」。這決定了兩件事：

- **路線怎麼分**，要以美國資料能說明的範圍為準。
- **每條路線講多深**，看 NSF 的錢在哪裡，以及哪裡需要拿來做對照。

所以結論應該回答「美國這樣投資，台灣該怎麼因應」，而不是一份完整的台灣 CIM 戰略。這也是 DRAM 只當對照組的原因。

#### 路線怎麼分：四條路線、新興記憶體拆三支，再加一個非路線類別

你列的 SRAM、快閃、DRAM、新興記憶體是對的，這正是核心頁的四列。但要做到完整，還需要補兩件事。

| 層級 | 類別 | NSF 件數 | NSF 經費占比 | 在論證中的角色 |
|---|---|---|---|---|
| 第一層：記憶體類型（依商業化程度排序） | SRAM | 2 | 2% | 對照：已量產，NSF 幾乎不投 |
| | 快閃 | 3 | 4% | 對照 |
| | DRAM | 3 | 6% | 對照：走向產品化，由產業主導 |
| | 新型非揮發記憶體 | 37 | 61% | 主軸 |
| 第二層：新型非揮發記憶體再拆 | 鐵電 | 12 | 26% | 主軸：NSF 增幅最大，也是台灣的缺口 |
| | 電阻式（RRAM） | 17 | 21% | 主軸：第二步已由台積電完成 |
| | 磁性（MRAM） | 8 | 14% | 主軸：第二步已完成，ACED Fab 是實例 |
| 非路線類別 | 不綁定特定記憶體（架構、設計工具、軟體） | 13 | 24% | 必須交代，否則有四分之一的經費下落不明 |
| | CMOS 類比記憶電路 | 2 | 4% | 註腳即可 |

資料：簡報數據檔 C07、C03，NSF 60 件，合計 4,224 萬美元（事實）。

需要補的兩件事：

1. **新型非揮發記憶體要拆成三支。** 第二步做到哪裡、台灣的位置、美台分工是否成形，這些分析都發生在這一層。只寫「新興記憶體」，會看不出 RRAM、MRAM 和鐵電的差別，也就推不出「鐵電是缺口」。
2. **不綁定特定記憶體要明列。** 它占 NSF CIM 經費約四分之一，不是任何一條記憶體路線，而是架構、設計工具、演算法研究。核心頁目前放在註腳，這樣處理可以，但口頭上要帶一句。它在四步流程上屬於第三步的工具。研判：這類研究可以銜接到「擴散」那條建議——設計工具和驗證平台，正是這類研究的產出。

#### 簡報現在的一個不一致

第 9 頁（C03）和核心頁（C07）用的是兩套分類：

- **第 9 頁**：鐵電、不綁定、電阻式、成熟製程記憶體、磁性。SRAM、快閃、DRAM 合併成「成熟製程記憶體」（10 件，15%）。
- **核心頁**：SRAM、快閃、DRAM、新型非揮發記憶體。新興三支合併，不綁定和 CMOS 類比電路放在註腳。

兩頁的數字其實對得上：成熟製程 10 件 = SRAM 2 + 快閃 3 + DRAM 3 + CMOS 類比 2。但聽眾看到兩種分法，會以為是兩套資料。

**建議**：整份簡報統一用上面的兩層分類，各頁依需要展開其中一層。

- 第 9 頁：第一層展開到記憶體類型，新興再拆三支。
- 核心頁：只用第一層。
- 第 12 頁之後：只看新興三支。

註腳可以寫明：「成熟製程記憶體＝SRAM、快閃、DRAM 與 CMOS 類比電路」。

#### 對應到台灣的方向

| 類別 | 美國觀察 | 對台灣的意涵（研判） |
|---|---|---|
| SRAM、快閃、DRAM | NSF 幾乎不投，由產業推動 | 台灣也由產業主導；公共角色是擴散與觀察，不另立重點 |
| 鐵電 | NSF 增量最大，元件都還在實驗室 | 最該補的第二步缺口 |
| RRAM、MRAM | NSF 研究元件，美國學界做晶片時多用台積電 | 分工已成形，深化承接 |
| 不綁定 | NSF 約四分之一的經費投在架構與工具 | 可作為第三步擴散的研究基礎 |

這樣路線分法、論證深度和結論三者就一致了：重點放在 NSF 的錢所在的地方，其他路線作為對照。

## 使用者

前面的四步流程可以幫每個計劃劃分進去嗎?

## Claude

可以，而且值得做。這一步正好可以檢驗兩件事：國科會的經費是不是真的集中在第三步，以及台灣在第二步（製程整合）的計畫是否比美國多。

做法有兩個前提要先講清楚：

- 分類依據是計畫摘要寫的規劃內容，不是實際成果。
- 一件計畫可能跨好幾步，所以會標「主要步驟」和「次要步驟」。

我會先訂一份分類規則，讓同一位分類者處理兩邊共122件計畫，確保標準一致。分類時順便把「嵌入式或獨立式」也標上，之後要用的B分法就一次補齊。分完後我再抽查。

## 研究助理查核報告（子代理，模型產出，非使用者訊息）

#### 分類結果

兩國共 122 件都讀過標題、摘要與關鍵詞（台灣另讀英文摘要）後分類，已寫入：
- `/tmp/claude-0/-home-claude/be76eb58-def2-5924-bce3-73de4a2fe852/scratchpad/grb/out_us.csv`：60 列
- `/tmp/claude-0/-home-claude/be76eb58-def2-5924-bce3-73de4a2fe852/scratchpad/grb/out_tw.csv`：62 列

已用 python 驗證：表頭與指定一致；cid 集合與各自輸入完全相同，沒有重複或缺漏；step_primary 只有 S1 到 S4；其他欄位都在允許值內；reason 全部 40 字以內。

**step_primary 件數**

| | S1 | S2 | S3 | S4 |
|---|---|---|---|---|
| 美國（60） | 14 | 1 | 44 | 1 |
| 台灣（62） | 24 | 4 | 34 | 0 |

- **S2 共 5 件：** NSF-146726（FeFET 與 CMOS 大規模整合）、TW-01、TW-03、TW-11、TW-23。全部在 NDL／TSRI 或 CMOS 晶圓上做整合。
- **S4 只有 1 件：** NSF-93463（SBIR 二期明寫開發實際產品）。
- **信心「低」：** 美國 4 件、台灣 12 件。台灣多半是摘要只寫影響、沒有工作內容的計畫，例如 TW-25、38、47、62。

#### 最難判斷的 15 件

1. NSF-144368：SAS-MRAM 以客製 BEOL 做在 40nm CMOS 晶粒上（S2），又要下線 IMC 晶片並開發演算法（S3）。題名以晶片為主，判 S3，次要 S2。
2. NSF-158150：一項元件目標對兩項電路／加速器目標，判 S3，次要 S1。但新 memcapacitor 元件也可能被視為主貢獻。
3. NSF-147944：ECRAM 新電解質元件與交叉陣列架構、SLAM 演算法份量接近，判 S3，次要 S1，信心低。
4. NSF-117046：3D 憶阻陣列與擴散式憶阻器（S1）對演算法與 PCB 系統（S3），兩兩平手，判 S1，信心低。
5. NSF-129873：FerroCoDE 含鐵電材料與元件，但主張的是系統引擎，判 S3，次要 S1。
6. NSF-158156：氧化銦 Fe-OSFET 元件與 Transformer 演算法、系統展示份量相當，判 S1，信心低。
7. NSF-93463 與 NSF-110407：兩件都是 SBIR 二期。前者明寫「develops the actual semiconductor product」判 S4；後者是 IP 設計、下線、驗證，判 S3。
8. NSF-147884 與 NSF-130805：感測內運算，兼含新元件與系統整合。系統面工作項目較多，判 S3，次要 S1。
9. TW-03：NC-FinFET 加 RRAM 的 1T1R 在 NDL／CIC 建製程流程，判 S2。但元件特性與可靠度分析佔很大篇幅，也可能被判 S1。
10. TW-11：工作以 HZO 薄膜物性為主，但目標寫明在 TSRI 把鐵電閘極做進 FinFET 並整合成 4T SRAM，符合 codebook 的 S2 範例，判 S2，次要 S1。
11. TW-14：FinFET 閘極接 RRAM 的 SG-NVM，在 NDL 做後段整合。新穎處是記憶單元結構，判 S1，次要 S3，沒有判 S2。
12. TW-34：同一類 RG-FET，做 TCAM 晶片「設計與實作」。新單元判 S1，次要 S3，信心低。
13. TW-58：團隊新提的 3D FTJ 嵌入式記憶體概念，並與先進邏輯製程整合做出實體晶片，判 S1，次要 S2，信心低。
14. TW-35：codebook 把「晶圓級成長以供整合」列為 S2，但本件首要是開發新憶阻器，單晶片三維只是「奠定基礎」，判 S1，次要 S2。
15. TW-08 與 TW-44：都是新元件（FTJ／MRAM、鐵電記憶體）加演算法加晶片或加速器。按工作主題數判 S3，次要 S1，信心低。

#### codebook 不清楚之處與我的處理

- **跨層共同設計計畫的主要步驟：** 這類摘要通常每一層都宣稱是貢獻，「主張的主要貢獻」幾乎無從區分。我改數明列的工作項目或 thrust 屬於哪一步，平手時看題名主軸，並把信心降為低。
- **S2 與「新單元結構在國家實驗室製作」的界線：** 第 3 條只寫在 TSRI／NDL 整合可判 S2，沒說新記憶單元本身就在 FinFET 上製作時怎麼算。我的處理是：新穎處在單元或元件本身時判 S1、整合列為次要（TW-14、34、58）；單元結構既有、新穎處在整合時判 S2（TW-03、11）。
- **s3_silicon 的「下線」範圍：** codebook 只寫下線、測試晶片或量測矽晶片。我另外把以下兩類也算下線：
  - 實驗室自製硬體在 PCB 或可撓基板上的系統示範；
  - 實際量測商用 3D NAND 晶片（NSF-158966）。

  在商用 UPMEM 上跑軟體則依 codebook 判「模擬」。「模擬」只用在明寫模擬、模擬器、FPGA，或純軟體／演算法的計畫；沒寫的一律填「不明」。
- **locus 沒有「混合」類，也沒說泛稱記憶體怎麼算。** 我的處理：
  - 同時處理 DRAM 與 SRAM（NSF-144223）填不明；
  - 針對泛稱 NVM 或憶阻器的架構、工具、演算法填不適用；
  - 點名特定記憶體但沒說實作方式的架構研究填不明；
  - 有實際設計的 CIM 晶片或巨集，記憶體必然和邏輯在同一晶片上，填嵌入式；
  - 只宣稱「與 CMOS 相容」，不據此判為嵌入式。
- **摘要只寫影響、沒有工作內容的台灣計畫（TW-25、38、47、62）：** 只能依題名加關鍵詞判斷，信心一律標低，沒有因字少改判別的步驟。

工作底稿（含每列判斷）在 `/tmp/claude-0/-home-claude/be76eb58-def2-5924-bce3-73de4a2fe852/scratchpad/work/us_dec.txt` 和 `tw_dec.txt`。

## Claude

122件計畫都已分進四步流程，交接包也準備好了。分類結果有一個重要發現：它讓「美國押第一步、台灣押第三步」這句話需要再修正得更精確。

#### 四步分類結果（經費占比）

| | 只做發明元件 | 元件加電路架構（跨步驟） | 只做電路與架構 | 涉及製程整合 | 涉及元件的合計 |
|---|---|---|---|---|---|
| 美國 2018–22 | 0% | 33% | 64% | 0% | 33% |
| 美國 2023後 | 9% | 46% | 37% | 8% | 55% |
| 台灣 2018–22 | 11% | 42% | 43% | 7% | 54% |
| 台灣 2023後 | 26% | 10% | 64% | 2% | 36% |

**1. 差異不在「誰做哪一步」，而在「步驟有沒有接在一起」（研判）。**
2023年後，美國近半經費投在同時做新元件和電路架構的跨步驟計畫。台灣則把元件和電路架構分開資助，跨步驟的計畫只占一成。

**2. 原本的方向仍然成立。**
2023年後，涉及元件的經費美國占55%、台灣占36%，和先前用研究層次算出的結果一致。

**3. 你先前猜的「台灣更能做試產驗證」，證據不夠。**
- 以製程整合為主的計畫，台灣有4件、美國1件，但兩邊經費占比差不多。
- 台灣這4件全由國研院主持，都在2018到2021年。2023年後台灣幾乎沒有這類計畫。
- 研判：國研院的12吋研究場域和工研院試產線，可能是恢復這一塊的機會。

**4. 嵌入式與獨立式的分類，從摘要判斷不出來。**
台灣14件鐵電計畫中10件無法判斷，美國12件中6件無法判斷。我先前依標題初判「NSF鐵電計畫以嵌入式為主」，目前無法確認，要讀論文全文才行。

這個分類依據的是摘要寫的規劃內容。台灣摘要較短，信心「低」的有12件，美國只有4件。和原本研究層次的分類相比，一致率80%，差異主要是17件跨層協同設計的計畫。

#### 交接包內容

「cim_nsf_project.zip」裡有：

- **`HANDOFF.md`**：論證現況、關鍵數字（附來源）、10項已修正的錯誤、待辦事項、檔案索引。新環境的接手者先讀這份就能接上進度。
- **`CLAUDE.md`**：你的寫作偏好與簡報既定規則，Claude Code 開啟專案時會自動讀取。
- **資料**：原始資料、台灣計畫分類、論文追查、四步分類結果，以及分類規則與逐件判斷底稿。
- **`scripts/key_numbers.py`**：重現所有關鍵數字。我已實際跑過，數字與上面一致。
- **簡報與參考檔**：內容稿、圖表數據、Design指令、講稿、合併初稿與參考簡報。

這次對話的內容不會跟著移過去，所以 `HANDOFF.md` 已經整理了接手所需的全部脈絡。四步分類的結果我們還沒討論，文件裡標成「待和使用者確認」。

#### 要不要放到 GitHub

你現有的4個 GitHub 儲存庫都是公開的。這份資料有國科會計畫明細，簡報也還沒發表，不建議放進公開儲存庫。有兩個做法：

1. 新開一個私人儲存庫，我把整包推上去，雲端環境就能直接開啟。你同意的話，告訴我儲存庫名稱即可。
2. 你自己把 zip 帶到新環境。

## 使用者

這些已經夠完整包含我們之前討論的所有東西了嗎

## 使用者（工作進行中插入）

我等下想把這個討論轉移到Claude code的雲端上面操作，協助我進行必要內容的轉移

## 使用者

這些已經夠完整包含我們之前討論的所有東西了嗎

（此後的回覆與交接包內容見 HANDOFF.md。）
