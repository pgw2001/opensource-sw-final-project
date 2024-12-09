import streamlit as st
from module import js_test
from module import weather
from module import clock

st.set_page_config(page_title="미니게임 수용소",page_icon="https://github.com/user-attachments/assets/dc050b97-fb89-4ffa-8024-2898a6fb7fa6",layout="wide")
st.markdown("""

    <style>
    .st-emotion-cache-1b2ybts{
        visibility:hidden;
    }
    </style>
 """,unsafe_allow_html=True)

#사이드 바 위젯
text = st.sidebar.text("채팅")
with st.sidebar:
    js_test.draw_chat()
    col1, col2 = st.columns(2)
    with col1:
        weather.draw_weather()
    with col2:
        clock.draw_clock()
empty1,con1,empty2 = st.columns([0.3,0.4,0.3])
with con1 : 
    st.image('images/title.png')
    st.header("여러가지 게임을 즐겨보세요")
    st.write("특히 바로 밑에 3개의 게임은 저희가 streamlit으로 직접 만든 눈물과 땀의 결실입니다.")
    st.write("streamlit으로 게임 만들지 마세요")
    st.logo(
        image="https://github.com/user-attachments/assets/034f0f73-2143-4c4e-809f-6d78eec0724a",
        size="large"

        )
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.expander(label="2048", expanded=True,):
                st.image("https://github.com/user-attachments/assets/0e8b1c35-af45-475a-aca7-d27d2fdc40a0")
                st.page_link("pages/Game2048.py", label="플레이", icon="⬜")
        with col2: 
            with st.expander(label="스도쿠", expanded=True,):
                st.image("https://github.com/user-attachments/assets/58c7f3bc-3a28-4c85-b04a-ba8d16ca7560")
                st.page_link("pages/GameSudoku.py", label="플레이", icon="📅")
        with col3:
            with st.expander(label="snake", expanded=True,):
                st.image("https://github.com/user-attachments/assets/9bb67179-2fb4-47b3-8e82-bb1caab05d12")
                st.page_link("pages/GameSnake.py", label="플레이", icon="🐍")
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.expander(label="테트리스", expanded=True,):
                st.image("https://github.com/user-attachments/assets/c0d76497-32a4-4a65-8390-5bd8c8763189")
                st.page_link("pages/tetris.py", label="플레이", icon="⬜")
        with col2: 
            with st.expander(label="퍼즐보블", expanded=True,):
                st.image("https://github.com/user-attachments/assets/ea77c59b-6196-444c-a5fd-32d278c0484f")
                st.page_link("pages/puzzleBobble.py", label="플레이", icon="🔴")
        with col3:
            with st.expander(label="크롬다이노", expanded=True,):
                st.image("https://github.com/user-attachments/assets/cf4f4e96-96bf-464f-b8fd-70655d75c2e6")
                st.page_link("pages/chromedino.py", label="플레이", icon="🦎")
    with st.container():
        col1, col2, col3 = st.columns(3)
        with col1:
            with st.expander(label="팩맨", expanded=True,):
                st.image("https://github.com/user-attachments/assets/9a60bcc1-f4c4-491a-80a7-ffa2b804442d")
                st.page_link("pages/pacman.py", label="플레이", icon="😃")
        with col2: 
            with st.expander(label="솔리테어", expanded=True,):
                st.image("https://github.com/user-attachments/assets/9c9ac912-b34d-44ae-8534-1450ce481c21")
                st.page_link("pages/solitare.py", label="플레이", icon="🃏")
        with col3:
            with st.expander(label="플래피버드", expanded=True,):
                st.image("https://github.com/user-attachments/assets/4b378b92-5273-410a-8018-2c499fc780ef")
                st.page_link("pages/flappybird.py", label="플레이", icon="🐣")
with empty2:
    st.page_link(page="pages/tutorial.py",label="튜토리얼",icon="📕")