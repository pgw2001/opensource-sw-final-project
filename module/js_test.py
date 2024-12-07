import streamlit.components.v1 as components
import streamlit as st

js_code = """
<script async src="//client.uchat.io/uchat.js"></script>
<u-chat room='opsw8' style="display:inline-block; width:300px; height:500px;"></u-chat>
"""
def draw_chat():
        components.html(js_code,width= 300, height= 500)