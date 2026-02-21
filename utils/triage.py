import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def triage_symptoms(symptoms):
    """
    Uses OpenAI to score urgency and recommend visit time.
    """
    prompt = f"""
    You are an AI triage assistant.
    Patient reports the following symptoms: "{symptoms}".
    Classify urgency as one of: Low, Medium, High.
    Recommend the best visit time (e.g., 'NOW', 'in 30 mins', 'later today').
    Respond in JSON format: {{ "urgency": "...", "recommended_time": "..." }}
    """

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role":"user","content":prompt}],
        temperature=0.2
    )

    # Parse JSON
    import json
    try:
        result_text = response.choices[0].message.content.strip()
        result = json.loads(result_text)
        urgency = result.get("urgency", "Medium")
        recommended_time = result.get("recommended_time", "in 30 mins")
    except:
        urgency, recommended_time = "Medium", "in 30 mins"

    return urgency, recommended_time