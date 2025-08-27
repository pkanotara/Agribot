import streamlit as st
from agribot.utils.constants import TASKS, TRANSLATIONS

def t(k):
    lang = st.session_state.get('lang', 'en')
    base = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    return base.get(k, k)

def task_multiselect():
    st.markdown(f"**{t('choose_tasks')}**")

    col1, col2 = st.columns([1, 1])
    if col1.button(t('select_all')):
        st.session_state['selected_tasks'] = [key for _, key in TASKS]
        st.rerun()
    if col2.button(t('clear_selection')):
        st.session_state['selected_tasks'] = []
        st.rerun()

    tasks = [(icon, key, t(key)) for icon, key in TASKS]

    for i, (icon, key, label) in enumerate(tasks):
        is_selected = key in st.session_state['selected_tasks']
        if st.button(f"{icon} {label}", key=f"task_{key}"):
            if is_selected:
                st.session_state['selected_tasks'].remove(key)
            else:
                st.session_state['selected_tasks'].append(key)
            st.rerun()
