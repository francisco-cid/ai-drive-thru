import openai
import os
from dotenv import load_dotenv
import constants
import json

#  load API key 
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LLM_MODEL = os.getenv("LLM_MODEL", "gpt-4o")

# initialize OpenAI client
client = openai.OpenAI(api_key=OPENAI_API_KEY)

def query_openai(user_input: str):
    try: 
        response = client.chat.completions.create(
            model=LLM_MODEL,
            messages= constants.LLM_INSTRUCTION_MESSAGES + [ {
            "role": "user",
            "content": [
                {
                "type": "text",
                "text": user_input
                }
            ]
            }],
            response_format={
                "type": "json_object"
            },
            temperature=1,
            max_completion_tokens=2048,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        # extract first message content from the LLM response
        raw_response = response.choices[0].message.content
        # convert JSON string intp a python dictionary
        parsed_response = json.loads(raw_response)
        print("OPEN AI RESPONSE (Parsed):", parsed_response) 
        return parsed_response
    except Exception as e:
        print("OPEN AI ERROR", e)
        return {"error": e}
