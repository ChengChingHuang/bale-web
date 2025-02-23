import streamlit as st

st.title("這是標題")
st.write("這是一個用 `st.write` 顯示的字串，可以處理多種格式，例如：數字、文字、Markdown、數據框等。")
st.text("這是一個用 `st.text` 顯示的純文字字串，只能顯示純文字，不支持其他格式。")
st.markdown(
    """
這是一個用 `st.markdown` 顯示的字串，可以處理 Markdown 語法。
例如：
* **粗體文字**
* *斜體文字*
* [連結](https://www.example.com)
* 代碼塊：
```python
print("Hello, Streamlit!")
```
"""
)

# 展開元件
with st.expander("點擊展開/收起"):  # 創建一個可展開/收起的區塊
    st.markdown(
        """
        這是展開元件內部
        """
    )

# 數字輸入元件
number = st.number_input("請輸入數字", step=1)
# step=1 表示單位以及增減的數字, min_value 表示最小值, max_value 表示最大值
st.markdown(f"你輸入的數字是：{number}")

# 文字輸入元件
text = st.text_input("請輸入文字")
st.markdown(f"你輸入的文字是：{text}")

# 按鈕元件
if st.button("點我"):
    st.balloons()

# 欄位元件
col1, col2 = st.columns(2)  # 2columns
col1.button("按鈕1", key="btn1")  # 在col1中建立一個按鈕類似st.button("按鈕1")
col2.button("按鈕2", key="btn2")  # 在col2中建立一個按鈕類似st.button("按鈕2")

# 2columns, 可以用比例來設定每個column的寬度,將比例放到list中
col1, col2 = st.columns([1, 2])
col1.button("按鈕1", key="btn3")  # 在col1中建立一個按鈕類似st.button("按鈕1")
col2.button("按鈕2", key="btn4")  # 在col2中建立一個按鈕類似st.button("按鈕2")

# 3columns
col1, col2, col3 = st.columns([1, 2, 3])
col1.button("按鈕1", key="btn5")  # 在col1中建立一個按鈕類似st.button("按鈕1")
col2.button("按鈕2", key="btn6")  # 在col2中建立一個按鈕類似st.button("按鈕2")
col3.button("按鈕3", key="btn7")  # 在col3中建立一個按鈕類似st.button("按鈕3")
