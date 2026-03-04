from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME
import json

client = Groq(api_key=GROQ_API_KEY)
def classify_intent(text):
    text = text.lower()

    if "not working" in text or "not charging" in text or "problem" in text:
        return "report_issue"

    if "working now" in text or "fixed" in text or "resolved" in text:
        return "confirm_resolution"

    if "still not working" in text or "did not work" in text:
        return "reject_solution"

    if "hello" in text or "hi" in text:
        return "greeting"

    return "provide_information"

def extract_issue(text):
    try:
        prompt = f"""
Extract product and issue from this support message.
Return JSON only:
{{
  "product": "",
  "issue": ""
}}

Message: {text}
"""
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )

        content = response.choices[0].message.content
        return json.loads(content)

    except Exception as e:
        print("Groq Error:", e)
        return {}
    
    