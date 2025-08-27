# agribot/pages/history.py

import streamlit as st
from agribot.components.sidebar import sidebar
from agribot.components.copy_button import copy_to_clipboard_component
from agribot.utils.constants import TRANSLATIONS
from agribot.utils.db import load_conversations, save_conversations
from agribot.utils.translator import translate_text

def t(k): 
    lang = st.session_state.get('lang', 'en')
    base = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    return base.get(k, k)

def history_page():
    sidebar()
    st.title(t('history'))
    conversations = load_conversations()
    user_id = st.session_state.get('username', 'guest_user')
    user_history = conversations.get(user_id, [])
    lang = st.session_state.get('lang', 'en')
    api_key = st.secrets.get("GOOGLE_API_KEY", "")

    if st.button(f"🗑 {t('clear_history')}"):
        conversations[user_id] = []
        save_conversations(conversations)
        st.success("History cleared!")
        st.rerun()

    if not user_history:
        st.info(t("no_history"))
        return

    msg_pairs, temp = [], []
    for entry in user_history:
        temp.append(entry)
        if len(temp) == 2:
            msg_pairs.append(temp)
            temp = []
    if temp: msg_pairs.append(temp)

    for idx, pair in enumerate(reversed(msg_pairs)):
        with st.expander(f"{t('timestamp')}: {pair[-1].get('timestamp','')[:16]}", expanded=False):
            for entry in pair:
                if entry["role"] == "model":
                    msg = entry["parts"][0]
                    display_msg = msg if lang == "en" else translate_text(msg, lang, api_key)
                    st.markdown(f"<div class='bot-message'>{display_msg}</div>", unsafe_allow_html=True)
                    copy_to_clipboard_component(display_msg, f"history_{idx}_{entry.get('timestamp', '')}")
                else:
                    st.markdown(f"<div class='user-message'>{entry['parts'][0]}</div>", unsafe_allow_html=True)
