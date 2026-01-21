import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash")


def generate_verified_doctors(hospital_name):
    prompt = f"""
Generate 1 dermatologist profile working at {hospital_name}.
Do NOT invent schedules.
Say availability depends on hospital working hours.
Return JSON only.
"""

    response = model.generate_content(prompt)
    return response.text
