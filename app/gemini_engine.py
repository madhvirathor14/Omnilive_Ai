from google import genai
import os
from dotenv import load_dotenv

# load env file
load_dotenv()

# get api key
api_key = os.getenv("GEMINI_API_KEY")

# create client
client = genai.Client(api_key=api_key)


def generate_response(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"Error: {str(e)}"