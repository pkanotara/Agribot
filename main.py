# import os
# import json
# from datetime import datetime
# import streamlit as st
# from PIL import Image
# import io
# import mimetypes
# import google.generativeai as genai


# # ============ CONFIGURATION =============
# st.set_page_config(
#     page_title="AgriBot - AI Farming Assistant",
#     page_icon="🌱",
#     layout="wide"
# )


# # Color palette and custom CSS for cards/buttons/selections ("forest" + teal accessible)
# st.markdown("""
# <style>
# body, [class*="css"] { font-family: 'Inter', 'Segoe UI', Arial, sans-serif; }
# h1, h2, h3, h4, h5, h6 { color: #14532d; }

# .sidebar .sidebar-content { background-color: #effaf4 !important; }

# .analyse-card {
#     background: #f8fafc;
#     border: 1.5px solid #e0e9e5;
#     border-radius: 20px;
#     margin: 12px 0 24px 0;
#     box-shadow: 0 4px 8px 0 #e0e9e59c;
#     padding: 28px 30px 20px 30px;
# }

# .upload-box {
#     background: #ecfdf5;
#     border: 1.5px dashed #059669;
#     border-radius: 12px;
#     padding: 14px;
#     margin-bottom: 10px;
# }

# .task-selection-grid {
#     display: grid;
#     grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
#     gap: 15px;
#     margin: 20px 0;
# }

# .task-option {
#     display: flex;
#     align-items: center;
#     background: #f8fafc;
#     border: 2px solid #e0e9e5;
#     border-radius: 12px;
#     padding: 15px;
#     cursor: pointer;
#     transition: all 0.2s ease;
#     user-select: none;
# }

# .task-option:hover {
#     background: #ecfdf5;
#     border-color: #10b981;
# }

# .task-option.selected {
#     background: #14532d;
#     color: white;
#     border-color: #14532d;
# }

# .task-checkbox {
#     margin-right: 12px;
#     width: 20px;
#     height: 20px;
#     border-radius: 4px;
#     border: 2px solid #059669;
#     display: flex;
#     align-items: center;
#     justify-content: center;
#     font-size: 14px;
# }

# .task-option.selected .task-checkbox {
#     background: #059669;
#     color: white;
# }

# .task-content {
#     display: flex;
#     align-items: center;
#     gap: 10px;
#     flex: 1;
# }

# .task-icon {
#     font-size: 24px;
# }

# .task-label {
#     font-weight: 600;
#     font-size: 16px;
# }

# .upload-btn button, .stButton>button  {
#     background: #059669 !important;
#     color: #fff !important;
#     font-weight: 700; font-size: 17px;
#     border-radius: 6px; border: none;
#     padding: 10px 26px;
#     margin-top: 6px;
# }
# .upload-btn button:hover, .stButton>button:hover {
#     background: #14532d !important;
# }
# .stDownloadButton>button {
#     color:#fff;background:#10b981; border-radius:6px; font-weight:700;
# }
# .stDownloadButton>button:hover { background:#14532d; }

# .copy-button {
#     background: #059669 !important;
#     color: white !important;
#     border: none;
#     border-radius: 6px;
#     padding: 8px 16px;
#     cursor: pointer;
#     font-weight: 600;
#     margin-left: 10px;
#     transition: all 0.2s ease;
# }

# .copy-button:hover {
#     background: #14532d !important;
# }

# .input-label {
#     font-weight: 600; color: #14532d; font-size: 15px;
#     letter-spacing: .2px; margin-bottom: 3px;
# }

# .chip { display: inline-block; background:#d1fae5; color:#166534; font-weight:600; border-radius:8px; padding:1.5px 13px; margin-right: 9px; font-size:15px;}
# .response-section { margin-bottom:1.2em;}
# .response-box { background: #f0fdf4; border:1.5px solid #dcfce7; border-radius:12px; padding:16px 18px; color:#134e31;}
# .bot-message,.user-message { margin-top: 0.5em;}
# .stTextArea textarea { border:1.3px solid #10b981;}

# .copy-container {
#     position: relative;
#     display: flex;
#     align-items: flex-start;
#     gap: 10px;
# }

# .copy-success {
#     color: #059669;
#     font-weight: 600;
#     font-size: 14px;
#     margin-left: 10px;
# }

# </style>
# """, unsafe_allow_html=True)

# # JavaScript for copy to clipboard functionality
# st.markdown("""
# <script>
# function copyToClipboard(text) {
#     navigator.clipboard.writeText(text).then(function() {
#         // Show success message
#         const successMsg = document.querySelector('.copy-success');
#         if (successMsg) {
#             successMsg.style.display = 'inline';
#             setTimeout(() => {
#                 successMsg.style.display = 'none';
#             }, 2000);
#         }
#     }).catch(function(err) {
#         console.error('Failed to copy: ', err);
#     });
# }
# </script>
# """, unsafe_allow_html=True)


# # ============ TRANSLATIONS =============
# TRANSLATIONS = {
#     'en': {
#         'title': 'AI-Driven Farming Assistant',
#         'nav_analyze': 'Analyze',
#         'nav_history': 'History',
#         'nav_about': 'About',
#         'welcome': 'Welcome to AgriBot',
#         'upload': 'Upload Plant Image',
#         'select_task': 'Select Analysis Type',
#         'analyze': 'Analyze',
#         'detect_disease': 'Detect Disease',
#         'get_suggestions': 'Get Treatment Suggestions',
#         'preventive': 'Preventive Measures',
#         'general_tips': 'General Farming Tips',
#         'growth': 'Growth Analysis',
#         'fertilizer': 'Fertilizer Advice',
#         'pest': 'Pest Identification',
#         'irrigation': 'Irrigation Guidance',
#         'choose_tasks': 'Select the analyses you need:',
#         'choose_lang': 'Choose Language',
#         'logout': 'Logout',
#         'login': 'Login',
#         'guest_login': 'Guest Login',
#         'username': 'Username',
#         'password': 'Password',
#         'error_upload': 'Please upload an image and select at least one analysis type!',
#         'analyzing': 'AgriBot is analyzing your plant...',
#         'save_report': 'Save as TXT',
#         'success_report': 'Report saved',
#         'file': 'File',
#         'size': 'Size',
#         'dimensions': 'Dimensions',
#         'support': 'Support',
#         'support_text': 'For assistance, contact your local agricultural extension office.',
#         'task_label': 'Analysis Type',
#         'timestamp': 'Time',
#         'clear_history': 'Clear History',
#         'no_history': 'No conversation history yet',
#         'copy': 'Copy',
#         'copied': 'Copied!',
#         'download': 'Download',
#         'auto_login_notice': 'Auto-login enabled (You will not be logged out on page refresh).',
#         'select_all': 'Select All',
#         'clear_selection': 'Clear Selection'
#     },
#     'hi': {
#         'title': 'AI-संचालित कृषि सहायक',
#         'nav_analyze': 'विश्लेषण',
#         'nav_history': 'इतिहास',
#         'nav_about': 'के बारे में',
#         'welcome': 'AgriBot में आपका स्वागत है',
#         'upload': 'पौधे की तस्वीर अपलोड करें',
#         'select_task': 'विश्लेषण प्रकार चुनें',
#         'analyze': 'विश्लेषण करें',
#         'detect_disease': 'रोग पहचान',
#         'get_suggestions': 'उपचार सुझाव',
#         'preventive': 'बचाव के उपाय',
#         'general_tips': 'सामान्य खेती की सलाह',
#         'growth': 'वृद्धि विश्लेषण',
#         'fertilizer': 'उर्वरक सलाह',
#         'pest': 'कीट पहचान',
#         'irrigation': 'सिंचाई मार्गदर्शन',
#         'choose_tasks': 'आवश्यक विश्लेषण चुनें:',
#         'choose_lang': 'भाषा चुनें',
#         'logout': 'लॉगआउट',
#         'login': 'लॉगिन',
#         'guest_login': 'अतिथि लॉगिन',
#         'username': 'उपयोगकर्ता नाम',
#         'password': 'पासवर्ड',
#         'error_upload': 'कृपया एक छवि अपलोड करें और कम से कम एक विश्लेषण प्रकार चुनें!',
#         'analyzing': 'AgriBot आपके पौधे का विश्लेषण कर रहा है...',
#         'save_report': 'TXT के रूप में सेव करें',
#         'success_report': 'रिपोर्ट सेव हो गई',
#         'file': 'फाइल',
#         'size': 'आकार',
#         'dimensions': 'आयाम',
#         'support': 'सहायता',
#         'support_text': 'सहायता के लिए, अपने स्थानीय कृषि विस्तार कार्यालय से संपर्क करें।',
#         'task_label': 'विश्लेषण प्रकार',
#         'timestamp': 'समय',
#         'clear_history': 'इतिहास साफ़ करें',
#         'no_history': 'अभी तक कोई बातचीत का इतिहास नहीं',
#         'copy': 'कॉपी करें',
#         'copied': 'कॉपी हो गया!',
#         'download': 'डाउनलोड',
#         'auto_login_notice': 'ऑटो-लॉगिन सक्षम (पेज रीफ्रेश पर आप लॉगआउट नहीं होंगे)।',
#         'select_all': 'सभी चुनें',
#         'clear_selection': 'चयन साफ़ करें'
#     },
#     'gu': {
#         'title': 'AI-સંચાલિત ખેતી સહાયક',
#         'nav_analyze': 'વિશ્લેષણ',
#         'nav_history': 'ઇતિહાસ',
#         'nav_about': 'વિશે',
#         'welcome': 'AgriBot માં તમારું સ્વાગત છે',
#         'upload': 'છોડની તસવીર અપલોડ કરો',
#         'select_task': 'વિશ્લેષણ પ્રકાર પસંદ કરો',
#         'analyze': 'વિશ્લેષણ કરો',
#         'detect_disease': 'રોગ ઓળખ',
#         'get_suggestions': 'સારવાર સૂચનો',
#         'preventive': 'નિવારક પગલાં',
#         'general_tips': 'સામાન્ય ખેતીની સલાહ',
#         'growth': 'વૃદ્ધિ વિશ્લેષણ',
#         'fertilizer': 'ખાતર સલાહ',
#         'pest': 'કીટક ઓળખ',
#         'irrigation': 'સિંચાઈ માર્ગદર્શન',
#         'choose_tasks': 'જરૂરી વિશ્લેષણ પસંદ કરો:',
#         'choose_lang': 'ભાષા પસંદ કરો',
#         'logout': 'લૉગઆઉટ',
#         'login': 'લૉગિન',
#         'guest_login': 'મહેમાન લૉગિન',
#         'username': 'વપરાશકર્તા નામ',
#         'password': 'પાસવર્ડ',
#         'error_upload': 'કૃપા કરીને એક છબી અપલોડ કરો અને ઓછામાં ઓછો એક વિશ્લેષણ પ્રકાર પસંદ કરો!',
#         'analyzing': 'AgriBot તમારા છોડનું વિશ્લેષણ કરી રહ્યું છે...',
#         'save_report': 'TXT તરીકે સેવ કરો',
#         'success_report': 'રિપોર્ટ સેવ થઈ ગઈ',
#         'file': 'ફાઇલ',
#         'size': 'કદ',
#         'dimensions': 'પરિમાણો',
#         'support': 'સહાય',
#         'support_text': 'સહાય માટે, તમારા સ્થાનીય કૃષિ વિસ્તરણ કાર્યાલયનો સંપર્ક કરો।',
#         'task_label': 'વિશ્લેષણ પ્રકાર',
#         'timestamp': 'સમય',
#         'clear_history': 'ઇતિહાસ સાફ કરો',
#         'no_history': 'હજુ સુધી કોઈ વાર્તાલાપ ઇતિહાસ નથી',
#         'copy': 'કૉપિ કરો',
#         'copied': 'કૉપિ થઈ ગઈ!',
#         'download': 'ડાઉનલોડ',
#         'auto_login_notice': 'ઑટો-લૉગિન સક્ષમ (પેજ રીફ્રેશ પર તમે લૉગઆઉટ થશો નહીં)।',
#         'select_all': 'બધું પસંદ કરો',
#         'clear_selection': 'પસંદગી સાફ કરો'
#     }
# }


# def t(k): return TRANSLATIONS.get(st.session_state.get('lang','en'), TRANSLATIONS['en']).get(k,k)
# def page_label(key): return t(f'nav_{key}')


# def init_session():
#     defaults = {
#         'lang': 'en','page':'analyze','logged_in':False,'role':None,'username':None,'current_analysis':None,
#         'selected_tasks': []
#     }
#     for k,v in defaults.items():
#         if k not in st.session_state:
#             st.session_state[k] = v


# TASKS = [
#     ('🦠', 'detect_disease'),
#     ('💊', 'get_suggestions'),
#     ('🛡', 'preventive'),
#     ('📚', 'general_tips'),
#     ('📈', 'growth'),
#     ('🌾', 'fertilizer'),
#     ('🐛', 'pest'),
#     ('💧', 'irrigation')
# ]
# USERS = { 'user001': {'password': '1234', 'role': 'admin'}, 'farmer1': {'password': 'farm123', 'role': 'user'}, 'demo': {'password': 'demo', 'role': 'user'}}
# DATABASE = "conversations.json"
# REPORTS_FOLDER = "reports"
# os.makedirs(REPORTS_FOLDER, exist_ok=True)


# def sidebar():
#     with st.sidebar:
#         st.markdown("### "+t('choose_lang'))
#         langs = {'English': 'en', 'हिंदी': 'hi', 'ગુજરાતી': 'gu'}
#         sel = st.selectbox("", list(langs.keys()), index=list(langs.values()).index(st.session_state['lang']))
#         ln = langs[sel]
#         if ln != st.session_state['lang']:
#             st.session_state['lang'] = ln
#             st.rerun()
#         st.info(f"User: {st.session_state.get('username','-')} | Role: {st.session_state.get('role','-')}")
#         st.caption(t('auto_login_notice'))
#         if st.button(t('logout')):
#             for k in list(st.session_state.keys()):
#                 del st.session_state[k]
#             st.query_params.clear()
#             st.rerun()


# def navbar():
#     tabs = ['analyze','history','about']
#     labels = [page_label(k) for k in tabs]
#     current_key = st.session_state.get('page','analyze')
#     idx = tabs.index(current_key) if current_key in tabs else 0
#     sel = st.radio(" ", labels, index=idx, horizontal=True)
#     st.session_state['page'] = tabs[labels.index(sel)]


# def all_task_options(): 
#     # Returns [(icon, key, label)]
#     return [(icon, key, t(key)) for icon, key in TASKS]


# def task_multiselect():
#     """Custom checkbox-style multi-select for tasks"""
#     st.markdown(f"<p style='font-weight: 600; margin-bottom: 10px;'>{t('choose_tasks')}</p>", unsafe_allow_html=True)
    
#     # Select All / Clear Selection buttons
#     col1, col2 = st.columns([1, 1])
#     with col1:
#         if st.button(t('select_all'), key="select_all_tasks"):
#             st.session_state['selected_tasks'] = [key for _, key in TASKS]
#             st.rerun()
#     with col2:
#         if st.button(t('clear_selection'), key="clear_all_tasks"):
#             st.session_state['selected_tasks'] = []
#             st.rerun()
    
#     # Task grid
#     tasks = all_task_options()
    
#     # Create grid layout
#     cols_per_row = 2
#     for i in range(0, len(tasks), cols_per_row):
#         cols = st.columns(cols_per_row)
#         for j, col in enumerate(cols):
#             if i + j < len(tasks):
#                 icon, key, label = tasks[i + j]
#                 is_selected = key in st.session_state['selected_tasks']
                
#                 # Create clickable task option
#                 with col:
#                     checkbox_symbol = "✓" if is_selected else ""
#                     selected_class = "selected" if is_selected else ""
                    
#                     if st.button(
#                         f"{icon} {label}",
#                         key=f"task_{key}",
#                         help=f"Click to {'deselect' if is_selected else 'select'} {label}",
#                         use_container_width=True
#                     ):
#                         if is_selected:
#                             st.session_state['selected_tasks'].remove(key)
#                         else:
#                             st.session_state['selected_tasks'].append(key)
#                         st.rerun()
                    
#                     # Show selection indicator
#                     if is_selected:
#                         st.success(f"✓ Selected")
#                     else:
#                         st.write("")


# def copy_to_clipboard_component(text, button_id):
#     """Create a copy to clipboard button with JavaScript functionality"""
#     # Clean the text for JavaScript
#     clean_text = text.replace("'", "\\'").replace('"', '\\"').replace('\n', '\\n')
    
#     copy_button_html = f"""
#     <div class="copy-container">
#         <button class="copy-button" onclick="copyToClipboard({clean_text}); showCopySuccess('{button_id}');">
#             📋 {t('copy')}
#         </button>
#         <span id="copy-success-{button_id}" class="copy-success" style="display: none;">
#             ✅ {t('copied')}
#         </span>
#     </div>
    
#     <script>
#     function copyToClipboard(text) {{
#         navigator.clipboard.writeText(text).then(function() {{
#             console.log('Text copied successfully');
#         }}).catch(function(err) {{
#             console.error('Failed to copy text: ', err);
#             // Fallback for older browsers
#             const textArea = document.createElement('textarea');
#             textArea.value = text;
#             document.body.appendChild(textArea);
#             textArea.select();
#             document.execCommand('copy');
#             document.body.removeChild(textArea);
#         }});
#     }}
    
#     function showCopySuccess(buttonId) {{
#         const successElement = document.getElementById('copy-success-' + buttonId);
#         if (successElement) {{
#             successElement.style.display = 'inline';
#             setTimeout(() => {{
#                 successElement.style.display = 'none';
#             }}, 2000);
#         }}
#     }}
#     </script>
#     """
    
#     st.components.v1.html(copy_button_html, height=60)


# def translate_text(text, target_lang, api_key):
#     if not text or target_lang == 'en': return text
#     lang_name = {'en': 'English','hi':'Hindi','gu':'Gujarati'}[target_lang]
#     genai.configure(api_key=api_key)
#     model = genai.GenerativeModel("gemini-1.5-flash")
#     prompt = (
#         f"Translate the following text to {lang_name}, preserving ALL content and sections. "
#         f"Do NOT make it shorter, do NOT summarize, just translate faithfully, keep all bullet points and sections as in English:\n\n{text}"
#     )
#     try:
#         resp = model.generate_content(prompt)
#         translated = resp.text.strip()
#         if len(translated.splitlines()) < 0.7 * len(text.splitlines()):
#             translated = translated + "\n\n[Original English for reference below:]\n" + text
#         return translated
#     except Exception: return text


# def login_page():
#     st.title(t('title')); st.subheader(t('login'))
#     username = st.text_input(t('username'), placeholder="username")
#     password = st.text_input(t('password'), type='password', placeholder="••••••••")
#     c1, c2 = st.columns([1,1])
#     with c1:
#         if st.button(t('login'),use_container_width=True):
#             if username in USERS and USERS[username]['password']==password:
#                 st.session_state['logged_in'] = True
#                 st.session_state['role'] = USERS[username]['role']
#                 st.session_state['username'] = username
#                 st.query_params["user"] = username
#                 st.query_params["token"] = "STATIC_TOKEN"
#                 st.rerun()
#             else: st.error("Invalid credentials!")
#     with c2:
#         if st.button(t('guest_login'),use_container_width=True):
#             st.session_state['logged_in'] = True
#             st.session_state['role'] = 'guest'
#             st.session_state['username'] = 'guest_user'
#             st.query_params["user"] = "guest_user"
#             st.query_params["token"] = "STATIC_TOKEN"
#             st.rerun()


# def get_model(api_key):
#     system_prompt = """
# You are AgriBot, an intelligent AI farming assistant.
# ALWAYS answer in 'Target Language' below, and in bullet points (max 5 per section, no long text).
# """
#     genai.configure(api_key=api_key)
#     return genai.GenerativeModel("gemini-1.5-flash", system_instruction=system_prompt.strip())


# def load_conversations():
#     if not os.path.exists(DATABASE): open(DATABASE,"w").write("{}")
#     with open(DATABASE,"r") as f: return json.load(f)
# def save_conversations(d): open(DATABASE,"w").write(json.dumps(d,indent=2))
# def save_report(user_id, analysis_type, response_text):
#     timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#     fn = f"{REPORTS_FOLDER}/{user_id}{analysis_type.replace(' ','')}_{timestamp}.txt"
#     open(fn,"w",encoding="utf-8").write(response_text)
#     return fn


# def analyze_page():
#     sidebar()
#     st.markdown(f"<h2 style='margin-top:8px'>{t('title')}</h2>", unsafe_allow_html=True)
#     st.markdown(f"<div class='analyse-card'>", unsafe_allow_html=True)
    
#     # Step 1: Upload
#     st.markdown(f"#### 1️⃣ {t('upload')}")
#     file = st.file_uploader("", type=['png','jpg','jpeg'], help="JPG or PNG, clear full-plant picture")
#     if file:
#         image = Image.open(file)
#         st.image(image, caption=t('upload'), use_container_width=True)
#         with st.expander(t('file')):
#             st.write(f"{t('file')}: {file.name}")
#             st.write(f"{t('size')}: {file.size/1024:.2f} KB")
#             st.write(f"{t('dimensions')}: {image.size[0]} x {image.size} px")
    
#     # Step 2: Task Selection
#     st.markdown(f"#### 2️⃣ {t('select_task')}")
#     task_multiselect()
    
#     # Show selected tasks
#     if st.session_state['selected_tasks']:
#         selected_labels = [t(key) for key in st.session_state['selected_tasks']]
#         st.success(f"*Selected:* {', '.join(selected_labels)}")

#     # Step 3: Additional Details
#     st.markdown("#### 3️⃣ Additional Details (optional)")
#     crop = st.text_input("Crop/Plant Type", placeholder="e.g. Tomato, Wheat, Cotton")
#     age = st.text_input("Plant Age", placeholder="e.g. 2 weeks, 1 month")
#     symp = st.text_area("Symptoms", placeholder="e.g., Spots, yellow leaves, etc.")

#     # Step 4: Action
#     st.markdown("---")
#     analyze_btn = st.button(f"🔬 {t('analyze')}", use_container_width=True, key="analyze_btn")
#     st.markdown("</div>", unsafe_allow_html=True)

#     # On analyze
#     if analyze_btn:
#         selected = st.session_state['selected_tasks']
#         if not (file and selected):
#             st.error(t('error_upload')); return
        
#         st.session_state['current_analysis'] = None
#         st.info(t('analyzing'))
#         api_key = st.secrets["GOOGLE_API_KEY"]
#         model=get_model(api_key)
#         user_id = st.session_state.username or "guest_user"
#         conversations = load_conversations()
#         user_history = conversations.get(user_id,[])
#         image_bytes=file.getvalue()
#         context = []
#         if crop: context.append(f"Crop: {crop}")
#         if age: context.append(f"Age: {age}")
#         if symp: context.append(f"Symptoms: {symp}")
#         context_str = "\n".join(context)
#         lang = st.session_state['lang']
#         prompt = (
#             f"Target Language: English.\n"
#             f"Tasks: {', '.join([t(key) for key in selected])}\n"
#             f"Context:\n{context_str}\n"
#             "Respond in short, clear bullet points (max 5 per section)."
#         )
#         mime_type, _ = mimetypes.guess_type(file.name)
#         image_file = genai.upload_file(path=io.BytesIO(image_bytes), display_name=file.name, mime_type=mime_type or "image/jpeg")
#         response = model.generate_content([prompt, image_file])
#         resp_en = response.text.strip()
#         if lang != 'en': resp_local = translate_text(resp_en, lang, api_key)
#         else: resp_local = resp_en
#         st.session_state.current_analysis = {
#             "en": resp_en, 
#             lang: resp_local, 
#             "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
#             "task": ", ".join([t(key) for key in selected])
#         }
#         user_history.append({ 
#             "role":"user", 
#             "parts":[f"Request: {', '.join([t(key) for key in selected])} | {context_str}"], 
#             "timestamp": datetime.now().isoformat() 
#         })
#         user_history.append({ 
#             "role":"model", 
#             "parts":[resp_en], 
#             "timestamp": datetime.now().isoformat() 
#         })
#         conversations[user_id] = user_history
#         save_conversations(conversations)
#         genai.delete_file(image_file.name)
#         st.success("✅ Analysis complete!")
    
#     if st.session_state.get('current_analysis'):
#         show_analysis_result()


# def show_analysis_result():
#     result = st.session_state.get("current_analysis")
#     if not result: return
#     lang = st.session_state['lang']
#     api_key = st.secrets.get('GOOGLE_API_KEY','')
#     text = result.get(lang) or translate_text(result["en"], lang, api_key)
    
#     st.markdown("---")
#     st.markdown(f"<div class='response-box'>", unsafe_allow_html=True)
#     for section in text.strip().split('\n\n'):
#         if section:
#             lines = section.strip().split('\n')
#             if lines:
#                 header = lines[0]
#                 content = '\n'.join(lines[1:])
#                 st.markdown(f"<span class='chip'>{header.strip()}</span>", unsafe_allow_html=True)
#                 st.markdown(content)
#     st.markdown("</div>", unsafe_allow_html=True)
    
#     # Action buttons
#     c1, c2, c3 = st.columns(3)
#     with c1:
#         txtf = save_report(st.session_state.username, result['task'], text)
#         with open(txtf, "rb") as file:
#             st.download_button(
#                 label=f"💾 {t('save_report')}", 
#                 data=file, 
#                 file_name=txtf.split("/")[-1], 
#                 mime="text/plain"
#             )
    
#     with c2:
#         # Copy to clipboard functionality
#         copy_to_clipboard_component(text, "analysis_result")
    
#     with c3:
#         if st.button("🗑 Clear Result"):
#             st.session_state.current_analysis = None
#             st.rerun()


# def history_page():
#     sidebar()
#     st.title(t('history'))
#     conversations = load_conversations()
#     user_id = st.session_state.username or "guest_user"
#     user_history = conversations.get(user_id, [])
#     lang = st.session_state['lang']
#     api_key = st.secrets.get("GOOGLE_API_KEY", "")
    
#     if st.button(f"🗑 {t('clear_history')}"):
#         conversations[user_id] = []
#         save_conversations(conversations)
#         st.success("History cleared!"); st.rerun()
    
#     if not user_history: 
#         st.info(t("no_history")); 
#         return
    
#     msg_pairs = []
#     temp_pair = []
#     for entry in user_history:
#         temp_pair.append(entry)
#         if len(temp_pair) == 2:
#             msg_pairs.append(temp_pair)
#             temp_pair = []
#     if temp_pair: msg_pairs.append(temp_pair)
    
#     for idx, pair in enumerate(reversed(msg_pairs)):
#         with st.expander(f"{t('timestamp')}: {pair[-1].get('timestamp','')[:16]}", expanded=False):
#             for entry in pair:
#                 if entry["role"] == "model":
#                     msg = entry["parts"][0]
#                     display_msg = msg if lang == "en" else translate_text(msg, lang, api_key)
#                     st.markdown(f"<div class='bot-message'>{display_msg}</div>", unsafe_allow_html=True)
                    
#                     # Add copy button for each response
#                     copy_to_clipboard_component(display_msg, f"history_{idx}_{entry.get('timestamp', '')}")
#                 else:
#                     st.markdown(f"<div class='user-message'>{entry['parts'][0]}</div>", unsafe_allow_html=True)


# def about_page():
#     sidebar()
#     st.title(t("about"))
#     st.markdown("### Available Analysis Types:")
#     for icon, key in TASKS:
#         st.write(f"{icon} *{t(key)}*")
#     st.success(f"{t('support')}\n{t('support_text')}")


# def main():
#     init_session()
#     query = st.query_params
#     if not st.session_state.get('logged_in', False):
#         user = query.get('user', None)
#         token = query.get('token', None)
#         if user in USERS and token == "STATIC_TOKEN":
#             st.session_state['logged_in'] = True
#             st.session_state['role'] = USERS[user]['role']
#             st.session_state['username'] = user
    
#     if not st.session_state.get('logged_in', False): 
#         login_page(); 
#         return
    
#     navbar()
#     pg = st.session_state['page']
#     if pg == 'analyze': analyze_page()
#     elif pg == 'history': history_page()
#     elif pg == 'about': about_page()
#     else: analyze_page()


# if __name__ == "__main__":
#     main()
