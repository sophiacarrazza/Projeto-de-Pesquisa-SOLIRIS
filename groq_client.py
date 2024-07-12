
""""
# Funções para interagir com o Groq.
import os
from groq import Groq
from chromadb_client import query_documents

os.environ["GROQ_API_KEY"] = "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"

def get_chat_completion(prompt, model):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"), 
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model=model,
    )

    return chat_completion.choices[0].message.content

def get_chat_completion_with_context(prompt, context, model):
    client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
    
    # Concatena o contexto com o prompt
    full_prompt = f"{context}\n\n{prompt}"
    
    chat_completion = client.chat.completions.create(
        messages=[{"role": "user", "content": full_prompt}],
        model=model,
    )
    return chat_completion.choices[0].message.content

{
  "id": "34a9110d-c39d-423b-9ab9-9c748747b204",
  "object": "chat.completion",
  "created": 1708045122,
  "model": "mixtral-8x7b-32768",
  "system_fingerprint": None,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant", 
        "content": "Low latency Large Language Models (LLMs) are important in the field of artificial intelligence and natural language processing (NLP) for several reasons:\n\n1. Real-time applications: Low latency LLMs are essential for real-time applications such as chatbots, voice assistants, and real-time translation services. These applications require immediate responses, and high latency can lead to a poor user experience.\n\n2. Improved user experience: Low latency LLMs provide a more seamless and responsive user experience. Users are more likely to continue using a service that provides quick and accurate responses, leading to higher user engagement and satisfaction.\n\n3. Competitive advantage: In today's fast-paced digital world, businesses that can provide quick and accurate responses to customer inquiries have a competitive advantage. Low latency LLMs can help businesses respond to customer inquiries more quickly, potentially leading to increased sales and customer loyalty.\n\n4. Better decision-making: Low latency LLMs can provide real-time insights and recommendations, enabling businesses to make better decisions more quickly. This can be particularly important in industries such as finance, healthcare, and logistics, where quick decision-making can have a significant impact on business outcomes.\n\n5. Scalability: Low latency LLMs can handle a higher volume of requests, making them more scalable than high-latency models. This is particularly important for businesses that experience spikes in traffic or have a large user base.\n\nIn summary, low latency LLMs are essential for real-time applications, providing a better user experience, enabling quick decision-making, and improving scalability. As the demand for real-time NLP applications continues to grow, the importance of low latency LLMs will only become more critical."
      },
      "finish_reason": "stop",
      "logprobs": None
    }
  ],
  "usage": {
    "prompt_tokens": 24,
    "completion_tokens": 377,
    "total_tokens": 401,
    "prompt_time": 0.009,
    "completion_time": 0.774,
    "total_time": 0.783
  }
}

def main():
    prompt = "Explain the importance of fast language models"
    model = "mixtral-8x7b-32768"
    response = get_chat_completion(prompt, model)
    print(response)

    print("Com contexto: \n\n") 

    documents = query_documents(prompt) # Consulta o ChromaDB pra pegar documentos relevantes
    # o qroq que deve consultar o chroma db e pegar os documentos relevantes
    context = "\n\n".join([doc['document'] for doc in documents['results']]) # formata o contexto a partir dos documentos recuperados 
    response = get_chat_completion_with_context(prompt, context, model) # resposta do Groq usando o contexto dos documentos
    #o groq deve buscar a resposta com o chroma db e o contexto
    #ele nao esta usando o texto em si pra buscar a resposta, ele esta usando o contexto, o que eh errado
    #ele deve usar o llm para buscar a resposta
    print(response)

if __name__ == "__main__":
    main()

"""