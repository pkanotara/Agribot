import google.generativeai as genai

def translate_text(text, target_lang, api_key):
    if not text or target_lang == 'en': return text
    lang_name = {'en': 'English','hi':'Hindi','gu':'Gujarati'}[target_lang]
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-1.5-flash")
    prompt = (
        f"Translate the following text to {lang_name}, preserving ALL content.\n\n{text}"
    )
    try:
        resp = model.generate_content(prompt)
        return resp.text.strip()
    except Exception:
        return text
