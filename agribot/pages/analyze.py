import streamlit as st
from datetime import datetime
from PIL import Image
import io, mimetypes, os
import google.generativeai as genai

from agribot.components.sidebar import sidebar
from agribot.utils.constants import TRANSLATIONS

REPORTS_FOLDER = "reports"
os.makedirs(REPORTS_FOLDER, exist_ok=True)
ANALYSIS_TASKS = [
    ('🦠', 'detect_disease'),
    ('💊', 'get_suggestions'),
    ('🛡', 'preventive'),
    ('📚', 'general_tips'),
    ('📈', 'growth'),
    ('🌾', 'fertilizer'),
    ('🐛', 'pest'),
    ('💧', 'irrigation')
]

def t(k):
    lang = st.session_state.get('lang', 'en')
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(k, k)

def analyze_page():
    sidebar()
    st.markdown(
        f"<h1 style='color:#14532d'>{t('title')}</h1>"
        f"<p style='font-size:17px;color:#356859;'>{t('welcome')}</p>",
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown(f"#### 1️⃣ {t('upload')}")
    uploaded_file = st.file_uploader(
        t('upload'),
        type=['png', 'jpg', 'jpeg'],
        help="JPG or PNG"
    )
    file_ok = False
    image = None
    if uploaded_file:
        try:
            image = Image.open(uploaded_file)
            st.image(image, caption="Upload", use_container_width=True)
            st.caption(f"{t('file')}: {uploaded_file.name} | {t('size')}: {uploaded_file.size/1024:.1f} KB | {t('dimensions')}: {image.size[0]}x{image.size[1]}")
            file_ok = True
        except Exception:
            st.error("Unable to open the uploaded file. Please check the file format.")

    st.markdown(f"#### 2️⃣ {t('select_task')}")

    if "selected_tasks" not in st.session_state:
        st.session_state["selected_tasks"] = []
    col_sel1, col_sel2 = st.columns(2)
    all_keys = [key for _, key in ANALYSIS_TASKS]
    with col_sel1:
        if st.button(t('select_all')):
            st.session_state["selected_tasks"] = all_keys.copy()
            st.rerun()
    with col_sel2:
        if st.button(t('clear_selection')):
            st.session_state["selected_tasks"] = []
            st.rerun()

    selected_tasks = st.session_state["selected_tasks"]
    cols = st.columns(2)
    for i, (icon, key) in enumerate(ANALYSIS_TASKS):
        label = t(key)
        with cols[i % 2]:
            checked = key in selected_tasks
            new_val = st.checkbox(f"{icon} {label}", key=f"task_{key}", value=checked)
            if new_val and (key not in selected_tasks):
                selected_tasks.append(key)
                st.session_state["selected_tasks"] = selected_tasks
            elif (not new_val) and (key in selected_tasks):
                selected_tasks.remove(key)
                st.session_state["selected_tasks"] = selected_tasks

    st.markdown(f"#### 3️⃣ {t('choose_tasks')}")
    col1, col2 = st.columns(2)
    with col1:
        crop = st.text_input(t('task_label'), placeholder="e.g., Tomato")
        age = st.text_input("Plant Age", placeholder="e.g., 3 weeks, 2 months")
    with col2:
        symptoms = st.text_area("Symptoms", placeholder="Yellow spots, curled leaves, etc.", height=64)

    st.markdown("<br>", unsafe_allow_html=True)
   
    analyze = st.button(f"🔬 {t('analyze')}", use_container_width=True)

    if analyze:
        if not (file_ok and st.session_state["selected_tasks"]):
            st.error(t('error_upload'))
        else:
            with st.spinner(t('analyzing')):
                try:
                    context_lines = []
                    if crop: context_lines.append(f"Crop: {crop}")
                    if age: context_lines.append(f"Age: {age}")
                    if symptoms: context_lines.append(f"Symptoms: {symptoms}")
                    context_str = "\n".join(context_lines)
                    task_labels = [t(key) for key in st.session_state["selected_tasks"]]
                    prompt = (
                        f"Target Language: English.\n"
                        f"Tasks: {', '.join(task_labels)}\n"
                        f"Context:\n{context_str}\n"
                        "Respond in short, clear bullet points (max 5 per section)."
                    )
                    api_key = st.secrets["GOOGLE_API_KEY"]
                    genai.configure(api_key=api_key)
                    model = genai.GenerativeModel("gemini-1.5-flash")
                    mime_type, _ = mimetypes.guess_type(uploaded_file.name)
                    image_io = io.BytesIO(uploaded_file.getvalue())
                    image_file = genai.upload_file(
                        path=image_io,
                        display_name=uploaded_file.name,
                        mime_type=mime_type or "image/jpeg"
                    )
                    response = model.generate_content([prompt, image_file])
                    resp_en = response.text.strip()
                    genai.delete_file(image_file.name)
                    st.session_state["analysis_result"] = {
                        "en": resp_en,
                        "timestamp": datetime.now().isoformat(),
                        "tasks": ", ".join(task_labels),
                        "image_name": uploaded_file.name,
                        "context": context_str
                    }
                    st.success("✅ " + t('success_report'))
                except Exception as e:
                    st.error(f"Analysis failed: {e}")

    if st.session_state.get("analysis_result"):
        show_analysis_result()

def show_analysis_result():
    result = st.session_state["analysis_result"]
    lang = st.session_state.get('lang', 'en')
    text_en = result.get("en", "")
    text = text_en
    if lang != 'en':
        from agribot.utils.translator import translate_text
        api_key = st.secrets.get('GOOGLE_API_KEY','')
        text = translate_text(text_en, lang, api_key)

    # --- Card style for raw output ---
    st.markdown("""
    <style>
    .agribot-output-card {
        background: linear-gradient(110deg, #c8f4e3 90%, #ace7ef 100%);
        border-radius: 18px;
        border: 2px solid #10b981;
        margin-bottom:2.1em;
        box-shadow:0 4px 16px #05966919;
        color: #134e31 !important;
        padding: 25px 30px 21px 34px;
        word-break:break-word
    }
    .agribot-output-card * {
        color: #134e31 !important;
    }
    .agribot-output-card pre {
        margin:1.1em 0 0 0;
        background: #f5f9f6 !important;
        color: #065535 !important;
        border-radius: 10px;
        font-size: 1.05em;
        padding: 14px;
        line-height: 1.55;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        f"""
        <div class="agribot-output-card">
        <div style='color: #134e31; font-weight:700; letter-spacing:.3px; font-size:1.18rem; margin-bottom: 10px;'>
            <span style='font-size:1.32rem;margin-right:8px;'>🌱</span>
            {t('analyze')} {t('result') if t('result') != 'result' else 'Result'}
        </div>
        <div style="font-size:15.6px;">
            <b style='color:#134e31'>{t('task_label')}:</b> {result['tasks']}<br>
            <b style='color:#134e31'>{t('timestamp')}:</b> {result['timestamp'][:19].replace("T"," ")}
        </div><hr style='margin:15px 0 15px 0;border:1.1px solid #b2dfdb' />
        <pre>{text}</pre>
        </div>
        """,
        unsafe_allow_html=True
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        output_fn = f'reports/{result["image_name"].replace(".","_")}_{result["timestamp"].replace(":","_")}.txt'
        with open(output_fn, "w", encoding="utf-8") as f:
            f.write(text)
        with open(output_fn, "rb") as f:
            st.download_button(
                label=f"💾 {t('save_report')}",
                data=f,
                file_name=output_fn.split("/")[-1],
                mime="text/plain"
            )
    with c2:
        if st.button(f"📋 {t('copy')}", key="copy_result"):
            st.code(text, language="markdown")
    with c3:
        if st.button(f"🗑 {t('clear_history')}", key="clear_result"):
            st.session_state["analysis_result"] = None
            st.rerun()
