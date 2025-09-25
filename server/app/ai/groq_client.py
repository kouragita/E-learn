import os
import requests
from flask import current_app

class GroqClient:
    def __init__(self):
        self.api_key = current_app.config.get('GROQ_API_KEY')
        self.api_url = "https://api.groq.com/openai/v1/chat/completions"

    def generate(self, prompt, model="llama3-8b-8192"):
        if not self.api_key:
            raise ValueError("GROQ_API_KEY is not set in the environment.")

        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": model,
            "messages": [
                {
                    "role": "system",
                    "content": "You are a helpful assistant for an e-learning platform."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        }

        try:
            response = requests.post(self.api_url, headers=headers, json=payload)
            response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
            return response.json()['choices'][0]['message']['content']
        except requests.exceptions.RequestException as e:
            # Handle network errors, timeouts, etc.
            print(f"Error connecting to Groq API: {e}")
            return None
        except (KeyError, IndexError) as e:
            # Handle unexpected response structure
            print(f"Error parsing Groq API response: {e}")
            return None