import streamlit as st
import streamlit.components.v1 as components

def copy_to_clipboard_component(text, button_id):
    text = text.replace("'", "\\'").replace('"', '\\"').replace('\n', '\\n')
    html = f"""
    <div>
        <button style="background:#059669;color:white;padding:6px 12px;border-radius:6px"
        onclick="navigator.clipboard.writeText('{text}')">📋 Copy</button>
    </div>
    """
    components.html(html, height=40)
