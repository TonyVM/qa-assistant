from openai import OpenAI
from prompts import PROMPTS
import os

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_test_artifacts(text, type_):
    prompt = PROMPTS.get(type_, "") + "\n" + text[:3000]  # limit to 3k chars
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )
    return response.choices[0].message.content
