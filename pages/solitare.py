import streamlit as st
from module import js_test
from module import weather
import streamlit.components.v1 as components

code = """
<div>
<script src="https://cdn.htmlgames.com/embed.js?game=ClassicSolitaire&amp;bgcolor=white"></script>
</div>
"""
#사이드 바 위젯
with st.sidebar:
    st.write("채팅")
    js_test.draw_chat()
    weather.draw_weather()

st.title("솔리테어")
components.html(code,width=800,height=600)