
import os
from groq import Groq

#groq_api_key = os.getenv("-")
groq_api_key = os.getenv("GROQ_API_KEY")
client = Groq(
    api_key=groq_api_key
)

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "Explain the importance of fast language models",
        }
    ],
    model="mixtral-8x7b-32768",
)

print(chat_completion.choices[0].message.content)
