import streamlit as st
from module import js_test

st.markdown(
    """
    <style>
    .st-emotion-cache-1b2ybts{
        visibility:hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 채팅 생성 파트
text = st.sidebar.text("채팅")
with st.sidebar:
    js_test.draw_chat()

st.title("내맘대로 추가한 게임들")
st.header("여러가지 게임을 즐겨보세요")
st.write("특히 바로 밑에 3개의 게임은 저희가 streamlit으로 직접 만든 눈물과 땀의 결실입니다.")
st.write("streamlit으로 게임 만들지 마세요")

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander(label="2048", expanded=True,):
            st.image("images\game1.png")
            st.page_link("pages/Game2048.py", label="플레이", icon="⬜")
    with col2: 
        with st.expander(label="스도쿠", expanded=True,):
            st.image("images\game2.png")
            st.page_link("pages/GameSudoku.py", label="플레이", icon="📅")
    with col3:
        with st.expander(label="snake", expanded=True,):
            st.image("images\game3.png")
            st.page_link("pages/GameSnake.py", label="플레이", icon="🐍")
with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        with st.expander(label="테트리스", expanded=True,):
            st.image("images\game4.png")
            st.page_link("pages/tetris.py", label="플레이", icon="⬜")
    with col2: 
        with st.expander(label="퍼즐보블", expanded=True,):
            st.image("images\game5.png")
            st.page_link("pages/puzzleBobble.py", label="플레이", icon="🔴")
    with col3:
        with st.expander(label="크롬다이노", expanded=True,):
            st.image("images\game6.png")
            st.page_link("pages/GameSnake.py", label="플레이", icon="🦎")