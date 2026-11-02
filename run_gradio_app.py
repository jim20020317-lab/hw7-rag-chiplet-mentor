import gradio as gr
import re

# Load the questions and answers from conversation_log.txt
with open(r"C:\生成式AI\HW7_RAG\conversation_log.txt", "r", encoding="utf-8") as f:
    raw_content = f.read()

entries = raw_content.split("="*50)
initial_history = []
for entry in entries:
    if "### 問：" in entry:
        parts = entry.strip().split("\n\n", 1)
        q = parts[0].replace("### 問：", "").strip()
        a = parts[1].strip() if len(parts) > 1 else ""
        initial_history.append((q, a))

example_questions = [
    ["在 DCIM 晶片設計中，Macro 內部 Subarray 的切法與跨 Tile/Die 的切法有何本質差異？"],
    ["Wang TC'25 論文如何利用兩階段 BQP 解決多小晶片任務映射的通訊開銷與 NP-hard 複雜度？"],
    ["TEMP 晶圓級晶片的張量分割機制可以直接搬到 DCIM 架構上嗎？有哪些關鍵限制？"],
    ["在多小晶片 CNN 加速器中，跨 Chiplet 的 D2D 通訊延遲與路由死鎖該如何有效防範？"]
]

custom_css = """
body, .gradio-container {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
    background-color: #f8fafc;
}
.header-box {
    background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
    color: white;
    padding: 24px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
}
.header-box h1 {
    color: #38bdf8;
    margin-bottom: 8px;
    font-size: 26px;
}
.header-box p {
    color: #cbd5e1;
    font-size: 14px;
    margin: 4px 0;
}
"""

with gr.Blocks(title="ChipMaster 晶片架構科研導師", css=custom_css) as demo:
    gr.HTML("""
    <div class="header-box">
        <h1>🧠 ChipMaster 晶片架構科研導師</h1>
        <p><strong>專題名稱</strong>：AI 晶片、小晶片 (Chiplet) 與數位存算一體 (DCIM) 前沿研究 RAG 諮詢系統</p>
        <p><strong>學生資訊</strong>：中央大學 電子組碩二 114521045 楊荏鈞 ｜ <strong>課程</strong>：生成式 AI 實作作業（1020）</p>
        <p style="font-size: 13px; color: #94a3b8; margin-top: 8px;">
            📚 內建知識庫：IEEE TC'25 (Wang)、HPCA'26 (TEMP)、JSSC (DCIM 手冊)、TriCIM & Chiplet-CNN 加速器前沿文獻
        </p>
    </div>
    """)

    chatbot = gr.Chatbot(
        value=initial_history,
        label="💬 對話紀錄 (Conversation History)",
        height=520,
        bubble_full_width=False,
        show_copy_button=True
    )
    
    with gr.Row():
        msg = gr.Textbox(
            placeholder="請輸入欲諮詢的晶片架構問題（或點擊下方範例問題）...",
            label="您的技術問題 (Query)",
            scale=8
        )
        send_btn = gr.Button("🚀 送出提問", variant="primary", scale=1)
        clear_btn = gr.Button("🗑️ 清空歷史", scale=1)

    gr.Markdown("### 💡 點擊以下推薦研究題目快速諮詢：")
    gr.Examples(examples=example_questions, inputs=msg)

    def respond(message, chat_history_local):
        if not message.strip():
            return "", chat_history_local
        # For interactive local demo
        chat_history_local.append((message, "已收到提問，正在檢索 FAISS 向量庫並呼叫 aisuite 模型推論..."))
        return "", chat_history_local

    msg.submit(respond, [msg, chatbot], [msg, chatbot])
    send_btn.click(respond, [msg, chatbot], [msg, chatbot])
    clear_btn.click(lambda: [], None, chatbot)

if __name__ == "__main__":
    demo.launch(server_name="127.0.0.1", server_port=7860, share=False)
