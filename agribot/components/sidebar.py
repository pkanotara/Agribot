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
        sel = st.selectbox("", list(langs.keys()), index=list(langs.values()).index(st.session_state.get('lang','en')))
        ln = langs[sel]
        if ln != st.session_state['lang']:
            st.session_state['lang'] = ln
            st.rerun()

        # User info/status
        is_logged_in = 'username' in st.session_state and st.session_state['username']
        if is_logged_in:
            st.info(f"User: {st.session_state.get('username','-')} | Role: {st.session_state.get('role','-')}")
            st.caption(t('auto_login_notice'))
            st.markdown("---")
            if st.button("🚪 Logout", use_container_width=True):
                for k in ["username", "role"]:
                    if k in st.session_state:
                        del st.session_state[k]
                st.success("Logged out successfully.")
                st.rerun()
        else:
            st.warning("You are not logged in.")
