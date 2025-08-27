import streamlit as st

def init_session():
    defaults = {
        'lang': 'en',
        'page': 'analyze',
        'logged_in': False,
        'role': None,
        'username': None,
        'current_analysis': None,
        'selected_tasks': []
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v
