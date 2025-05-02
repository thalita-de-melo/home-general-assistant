import os

from groq import Groq

from dotenv import load_dotenv

load_dotenv()

class GroqConnection:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = "llama-3.3-70b-versatile"
        self.client = Groq(
            api_key=self.api_key,
        )

    def make_request(self, user_input):
        chat_completion = self.client.chat.completions.create(
        messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente que deve responder as \
                    perguntas do usuário de forma clara e direta. Responda \
                    usando o português.",
                },
                {
                    "role": "user",
                    "content": user_input,
                }
            ],
            model=self.model,
        )

        return(chat_completion.choices[0].message.content)