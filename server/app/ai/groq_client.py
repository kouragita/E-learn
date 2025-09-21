from groq import Groq
from flask import current_app

class GroqClient:
    def __init__(self):
        self.api_key = current_app.config.get('GROQ_API_KEY')
        if not self.api_key:
            raise ValueError("GROQ_API_KEY is not set in the configuration.")
        self.client = Groq(api_key=self.api_key)

    def execute(self, prompt, model="llama3-8b-8192", temperature=0.5, json_mode=True):
        """Executes a prompt against the Groq API."""
        try:
            chat_completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=model,
                temperature=temperature,
                response_format={"type": "json_object"} if json_mode else None,
            )
            return chat_completion.choices[0].message.content
        except Exception as e:
            print(f"Groq API request failed: {e}")
            raise
