# 🧠 ChipMaster 晶片架構科研導師 —— AI 晶片與小晶片前沿研究 RAG 諮詢系統

國立中央大學 生成式 AI 實作課程 第七週作業（1020）
- **學號**：114521045
- **系級**：電子組碩二
- **姓名**：楊荏鈞
- **專題主題**：打造自己的 RAG 對話機器人（AI 晶片、小晶片與數位存算一體前沿架構問答導師）

---

## 🌟 專題簡介與知識庫特色
本專案打破一般常見的社團或簡單 FAQ 題目，選取高度原創且深具工程價值的 **IEEE 頂尖文獻與晶片架構設計手冊** 作為 RAG 知識庫：
1. **SRAM 數位存算一體 (DCIM) 分割方法目錄**：涵蓋 Bitcell、Subarray、Macro、Tile、Chiplet 多層級物理限制與映射策略。
2. **DCIM × TEMP 晶圓級晶片 (WSC) 張量分割裁決報告**：分析 Weight-Stationary, Output-Stationary, TATP Relay 中繼機制之移植性與邊界條件。
3. **Wang TC'25 多小晶片任務映射導讀**：IEEE Transactions on Computers 頂尖論文，解析兩階段二進位二次規劃 (BQP) 如何降低跨晶片 D2D 通訊與網路壅塞。
4. **多小晶片 CNN 加速器任務分配與 NoC 路由優化**：探討拓撲感知路由、封裝跳步延遲與防死鎖機制。

---

## 📂 專案架構
```
hw7-rag-chiplet-mentor/
├── HW7_RAG01_打造向量資料庫.ipynb       # 程式一：文本讀取、切割、EmbeddingGemma 向量化與建立 FAISS
├── HW7_RAG02_打造_RAG_系統.ipynb        # 程式二：直連載入向量庫、aisuite LLM 串接與 Gradio 對話介面
├── uploaded_docs/                     # 知識庫來源原始文件 (.txt, .pdf)
├── faiss_db/                          # 生成之 FAISS 向量資料庫
└── 作業繳交內容說明.md                  # 完整的作業繳交報告（含人設、截圖、問答實錄、AI協助說明）
```

---

## 🚀 快速開始 (Google Colab 一鍵運行)
1. **直接開啟 RAG02 Colab 筆記本**：
   - 程式碼第 0 步已整合直連下載機制，自動自 GitHub Release 抓取並解壓 `rag-data.zip`。
   - 滿足課程規定，引入 `aisuite[all]` 統一管理大語言模型推論介面。
2. **啟動 Gradio WebApp**：
   - 提供直覺的 Web 介面與點擊式預設研究題目，即時獲取專業架構解析。
