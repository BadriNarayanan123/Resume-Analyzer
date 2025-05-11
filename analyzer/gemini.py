import google.generativeai as genai
import os
from analyzer.prompt_template import prompt_template
from dotenv import load_dotenv
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise Exception("GOOGLE_API_KEY not found in environment")
genai.configure(api_key=api_key)

def get_gemini_response(resume, job_desc):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = prompt_template.format(resume=resume, job_desc=job_desc)
    response = model.generate_content(prompt)
    # Expecting a JSON-like response — parse if needed
    return try_parse_response(response.text)

def try_parse_response(text):
    import json
    try:
        return json.loads(text)
    except:
        # Fallback: use basic formatting
        return {"Raw Response": text}
