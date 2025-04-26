import openai
import os
from dotenv import load_dotenv

load_dotenv()

def call_openai(prompt):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an emotional interpreter AI, mystical and cyberpunk in style."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=500,
    )

    emotional_text = response.choices[0].message.content.strip()
    return emotional_text
