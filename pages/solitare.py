import streamlit as st
from module import js_test
from module import weather
from module import clock
import streamlit.components.v1 as components

st.set_page_config(page_title="Solitaire", page_icon="images\game8.png")

code = """
<div>
<script src="https://cdn.htmlgames.com/embed.js?game=ClassicSolitaire&amp;bgcolor=white"></script>
</div>
"""
#사이드 바 위젯
text = st.sidebar.text("채팅")
with st.sidebar:
    js_test.draw_chat()
    col1, col2 = st.columns(2)
    with col1:
        weather.draw_weather()
    with col2:
        clock.draw_clock()

st.title("솔리테어")
components.html(code,width=800,height=600)