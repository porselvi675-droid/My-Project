import os
import google.generativeai as genai
from dotenv import load_dotenv

# Environment variables load panna
load_dotenv()

# Gemini API setup
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

# Gemini Model initialize panna
model = genai.GenerativeModel("gemini-1.5-flash")

def get_gemini_response(prompt):
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"