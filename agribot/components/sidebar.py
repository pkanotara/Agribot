import streamlit as st
from agribot.utils.constants import TRANSLATIONS

def t(k): 
    return TRANSLATIONS.get(
        st.session_state.get('lang','en'),
        TRANSLATIONS['en']
    ).get(k, k)

def sidebar():
    with st.sidebar:
        st.markdown("### " + t('choose_lang'))
        langs = {'English': 'en', 'हिंदी': 'hi', 'ગુજરાતી': 'gu'}
        sel = st.selectbox("", list(langs.keys()), index=list(langs.values()).index(st.session_state['lang']))
        ln = langs[sel]
        if ln != st.session_state['lang']:
            st.session_state['lang'] = ln
            st.rerun()
        st.info(f"User: {st.session_state.get('username','-')} | Role: {st.session_state.get('role','-')}")
        st.caption(t('auto_login_notice'))
