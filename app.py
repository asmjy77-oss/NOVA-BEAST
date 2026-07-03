import streamlit as st
import google.generativeai as genai

# إعداد الـ AP
# تذكر: هذا الكود سيعمل عندما ترفعه على Streamlit Cloud
# استبدل "YOUR_API_KEY" بمفتاحك الحقيقي
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-2.0-flash')

st.title("NOVA-BEAST App")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("أهلاً بك.. اسألني أي شيء!"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    response = model.generate_content(prompt)
    with st.chat_message("assistant"):
        st.markdown(response.text)
    st.session_state.messages.append({"role": "assistant", "content": response.text})
