import streamlit as st
from agribot.utils.constants import TRANSLATIONS

def page_label(key):
    lang = st.session_state.get('lang', 'en')
    base = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    return base.get(f'nav_{key}', key)

def navbar():
    tabs = ['analyze','history','about']
    labels = [page_label(k) for k in tabs]
    current_key = st.session_state.get('page','analyze')
    idx = tabs.index(current_key) if current_key in tabs else 0
    sel = st.radio(" ", labels, index=idx, horizontal=True)
    st.session_state['page'] = tabs[labels.index(sel)]
