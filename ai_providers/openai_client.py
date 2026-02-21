from openai import OpenAI
import os

client = OpenAI(api_key=os.getenv("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"))

def ask_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
