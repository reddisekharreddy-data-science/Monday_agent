from openai import OpenAI
import json
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI()

def interpret_query(question):

    prompt = f"""
    Convert this business question into JSON:

    {question}

    Return:
    {{
      "metric": "",
      "sector": "",
      "time_period": "",
      "board_required": ""
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return json.loads(response.choices[0].message.content)