# Funções para interagir com o Groq.

import os
from groq import Groq
from config import CONFIG

curl -X POST "https://api.groq.com/openai/v1/chat/completions" \
     -H "Authorization: Bearer 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" \
     -H "Content-Type: application/json" \
     -d '{"messages": [{"role": "user", "content": "Be an HR interview assistant"}], "model": "mixtral-8x7b-32768"}'

{
    "id": "chatcmpl-abc123",
    "object": "chat.completion",
    "created": 1677858242,
    "model": "gpt-3.5-turbo-0613",
    "usage": {
        "prompt_tokens": 13,
        "completion_tokens": 7,
        "total_tokens": 20
    },
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "\n\nThis is a test!"
            },
            "logprobs": null,
            "finish_reason": "stop",
            "index": 0
        }
    ]
}

groq_api_key = CONFIG.chat("groq_api_key")
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
