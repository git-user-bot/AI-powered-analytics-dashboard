import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.5-flash")


def generate_ai_insights(kpis, correlations):

    prompt = f"""
    You are a professional data analyst.

    Analyze these KPIs and correlations.

    KPIs:
    {kpis}

    Correlations:
    {correlations}

    Provide:
    1. Key trends
    2. Important anomalies
    3. Business recommendations
    4. Performance summary
    """

    response = model.generate_content(prompt)

    return response.text