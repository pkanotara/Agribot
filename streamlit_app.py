import streamlit as st
from agribot.utils.session import init_session
from agribot.components.sidebar import sidebar
from agribot.components.navbar import navbar
from agribot.pages.analyze import analyze_page
from agribot.pages.history import history_page
from agribot.pages.about import about_page
from agribot.pages.login import login_page
from agribot.utils.constants import USERS

def main():
    init_session()
    query = st.query_params

    if not st.session_state.get('logged_in', False):
        user = query.get('user', None)
        token = query.get('token', None)
        if user in USERS and token == "STATIC_TOKEN":
            st.session_state['logged_in'] = True
            st.session_state['role'] = USERS[user]['role']
            st.session_state['username'] = user

    if not st.session_state.get('logged_in', False):
        login_page()
        return

    navbar()
    pg = st.session_state['page']
    if pg == 'analyze':
        analyze_page()
    elif pg == 'history':
        history_page()
    elif pg == 'about':
        about_page()
    else:
        analyze_page()

if __name__ == "__main__":
    main()
