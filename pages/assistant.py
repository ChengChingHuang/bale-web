import streamlit as st
from utils import init_page
from openai import OpenAI
import os
import json
from dotenv import load_dotenv

# 載入環境變數
load_dotenv()

# 初始化 OpenAI 客戶端
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 載入 relu.json 的內容
def load_initial_messages():
    with open("relu.json", "r", encoding="utf-8") as file:
        return json.load(file)["messages"]

# 初始化頁面
init_page()
st.title("文字客服助手")

# 初始化聊天歷史
if "messages" not in st.session_state:
    st.session_state.messages = load_initial_messages()

# 顯示聊天歷史
for message in st.session_state.messages:
    if message["role"] != "system":  # 不顯示系統訊息
        with st.chat_message(message["role"]):
            st.write(message["content"])

# 取得使用者輸入的訊息
if message := st.chat_input("請輸入訊息"):
    # 顯示使用者的訊息
    with st.chat_message("user"):
        st.write(message)
    # 儲存訊息到歷史
    st.session_state.messages.append({"role": "user", "content": message})

    # 取得 AI 回覆
    try:
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=st.session_state.messages,
        )
        assistant_response = completion.choices[0].message.content

        # 顯示助手回覆
        with st.chat_message("assistant"):
            st.write(assistant_response)
        # 儲存助手回覆到歷史
        st.session_state.messages.append({"role": "assistant", "content": assistant_response})

        # 檢查對話次數是否超過 10 次
        if len([msg for msg in st.session_state.messages if msg["role"] != "system"]) >= 10:
            st.session_state.messages = load_initial_messages()
            st.info("已達到 10 次對答，歷史對話已清除並重新載入初始內容。")

    except Exception as e:
        st.error(f"發生錯誤: {str(e)}")
