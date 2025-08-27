
import google.generativeai as genai

def get_model(api_key):
    system_prompt = """
You are AgriBot, an intelligent AI farming assistant.
ALWAYS answer in 'Target Language' below, and in bullet points (max 5 per section).
"""
    genai.configure(api_key=api_key)
    return genai.GenerativeModel("gemini-1.5-flash", system_instruction=system_prompt.strip())
