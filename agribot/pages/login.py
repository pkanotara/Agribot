import streamlit as st
from agribot.utils.constants import USERS, TRANSLATIONS

def t(k):
    lang = st.session_state.get('lang', 'en')
    base = TRANSLATIONS.get(lang)
    if not base:
        base = TRANSLATIONS.get('en', {})
    return base.get(k, k)

def login_page():
    st.title(t('title'))
    st.subheader(t('login'))
    username = st.text_input(t('username'))
    password = st.text_input(t('password'), type='password')
    if st.button(t('login')):
        if username in USERS and USERS[username]['password'] == password:
            st.session_state['logged_in'] = True
            st.session_state['role'] = USERS[username]['role']
            st.session_state['username'] = username
            st.query_params["user"] = username
            st.query_params["token"] = "STATIC_TOKEN"
            st.rerun()
        else:
            st.error("Invalid credentials!")

    if st.button(t('guest_login')):
        st.session_state['logged_in'] = True
        st.session_state['role'] = 'guest'
        st.session_state['username'] = 'guest_user'
        st.query_params["user"] = "guest_user"
        st.query_params["token"] = "STATIC_TOKEN"
        st.rerun()
