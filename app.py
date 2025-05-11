import streamlit as st
from analyzer.parser import extract_text_from_pdf
from analyzer.gemini import get_gemini_response
from dotenv import load_dotenv
import google.generativeai as genai

import os

load_dotenv()

st.title("🔍 Smart ATS Resume Analyzer")
st.markdown("Upload your resume and job description to get insights using Gemini AI.")

jd = st.text_area("📄 Paste the Job Description")
uploaded_file = st.file_uploader("📎 Upload Resume (PDF)", type="pdf")

if st.button("Analyze"):
    if uploaded_file and jd:
        with st.spinner("Analyzing resume..."):
            try:
                resume_text = extract_text_from_pdf(uploaded_file)
                response = get_gemini_response(resume_text, jd)
                st.json(response)
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("Please upload a resume and enter a job description.")

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise Exception("GOOGLE_API_KEY not found in environment")
genai.configure(api_key=api_key)
