import streamlit as st
from agribot.components.sidebar import sidebar
from agribot.utils.constants import TRANSLATIONS, TASKS

def t(k): 
    lang = st.session_state.get('lang', 'en')
    base = TRANSLATIONS.get(lang, TRANSLATIONS['en'])
    return base.get(k, k)

def about_page():
    sidebar()
    st.markdown("""
    <style>
    .agribot-about-main-bg {
        background: none !important;
        margin: 0;
        padding: 0;
    }
    .agribot-about-card {
        background: linear-gradient(105deg, #e8fcf5 88%, #d2f3e6 100%);
        border-radius: 19px;
        border: 2px solid #10b981;
        padding: 38px 44px 32px 44px;
        margin: 40px auto 0 auto;
        box-shadow: 0 4px 18px #05966919;
        color: #14532d !important;
        font-size:1.12em;
        max-width: 1000px;
        min-width: 320px;
        width: 100%;
        display: block;
    }
    .agribot-chips {
        margin: 24px 0 11px 0;
        display: flex; flex-wrap: wrap; gap: 12px;
    }
    .agribot-chip {
        display: inline-block; padding: 9px 20px;
        background: #d1fae5; color: #14532d;
        border-radius: 9px; font-weight:600; font-size: 17px;
        border:1.3px solid #10b981;
        transition: background 0.2s;
    }
    .agribot-chip:hover { background:#b1ece0; color:#026e56;}
    .agribot-about-title {
        font-size:2.1em;
        color:#134e31;
        font-weight: 800;
        margin-bottom:0.39em;
    }
    .agribot-section-head {
        color:#059669; font-size:1.2em; font-weight:650; margin:19px 0 13px 0;
    }
    @media (max-width: 1100px) {
        .agribot-about-card { padding:28px 12px 20px 12px; max-width: 98vw; }
        .agribot-about-title { font-size:1.3em; }
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(
        f"""<div class="agribot-about-main-bg">
        <div class="agribot-about-card">
        <div class="agribot-about-title">
            🌱 AgriBot – {t('title')}
        </div>
        <div style="font-size:1.08em; margin-bottom:23px;">
            <b>{t('welcome')}</b>
            <br>
            <span style="color:#276450;">
                AI-powered assistant for plant health, farming advice, and agricultural decision support.<br>
                Upload images, select the analyses you need, and get instant, reliable insights for your crops.
            </span>
        </div>
        <div class="agribot-section-head">{t('choose_tasks')}</div>
        <div class="agribot-chips">
            {''.join([f"<span class='agribot-chip'>{icon} {t(key)}</span>" for icon, key in TASKS])}
        </div>
        <div class="agribot-section-head">✨ Key Features</div>
        <ul style="margin-left:1.2em; margin-bottom:1em;">
            <li>🌾 <b>AI-based plant disease, pest, and health analysis</b></li>
            <li>📸 Image upload and instant evaluation</li>
            <li>🔢 Multiple insight types at once (disease, advice, fertilizer, growth, more)</li>
            <li>🌐 Multi-language support and auto-translation</li>
            <li>💾 Download and copy AI responses</li>
            <li>🟢 All data processed securely, privacy first</li>
        </ul>
        <div class="agribot-section-head">{t('support')}</div>
        <div>
            {t('support_text')}
        </div>
        <div style='margin-top:26px; font-size:1em; color:#236950; text-align:right;'>
            <i>Version:</i> <b>1.0</b> &nbsp; | &nbsp;
            <i>Developed by Team AgriBot, 2025</i>
        </div>
        </div></div>
        """, unsafe_allow_html=True
    )
