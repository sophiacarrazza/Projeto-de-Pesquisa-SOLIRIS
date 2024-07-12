# Classe principal do chatbot.
from langchain.schema import SystemMessage, HumanMessage, AIMessage
from chatbot.rag import RAGRetriever
from utils.chromadb_client import query_documents

class ChatBot:
    def __init__(self, config):
        self.model = config['chat']
        self.rag = RAGRetriever(config['rag_retriever'])
        self.messages = [
            SystemMessage(content="You are a helpful assistant."),
            AIMessage(content="Olá, candidato, como você está se sentindo hoje?"),
            HumanMessage(content="Estou bem, obrigado por perguntar. Animado para esta entrevista."),
            AIMessage(content="Ótimo! Vamos começar. Você poderia me contar um pouco sobre sua experiência com machine learning?"),
            HumanMessage(content="Claro! Tenho trabalhado com machine learning nos últimos três anos em projetos de análise de dados e previsão de demanda."),
            AIMessage(content="Interessante! Quais frameworks e linguagens de programação você está mais familiarizado?"),
            HumanMessage(content="Principalmente Python, e tenho experiência com TensorFlow e scikit-learn."),
            AIMessage(content="Excelente. Como você lida com desafios durante o desenvolvimento de modelos de machine learning?"),
            HumanMessage(content="Costumo quebrar os problemas em etapas menores e iterar nas soluções. Além disso, estou sempre buscando aprender com meus erros e experiências."),
            AIMessage(content="Isso é muito importante. E quanto à comunicação de resultados técnicos para uma equipe não técnica?"),
            HumanMessage(content="Eu me esforço para explicar conceitos complexos de forma simples e acessível, utilizando visualizações quando necessário."),
            AIMessage(content="Ótimo saber disso. Obrigado por compartilhar sua experiência conosco. Você tem alguma pergunta para mim sobre a posição?"),
            HumanMessage(content="Sim, gostaria de saber mais sobre as oportunidades de crescimento dentro da empresa."),
            AIMessage(content="Certamente, podemos discutir isso mais detalhadamente na próxima etapa do processo. Muito obrigado pela sua participação hoje. Entraremos em contato em breve."),
        ]

    def start(self):
        while True:
            user_input = input("You: ")
            self.messages.append(HumanMessage(content=user_input))
            
            # Use o RAG para buscar informações relevantes
            retrieved_docs = query_documents(user_input)
            context = "\n".join([f"Question: {doc.payload['question']}\nAnswer: {doc.payload['answer']}" for doc in retrieved_docs])
            
            # Adicione o contexto aos messages
            self.messages.append(SystemMessage(content=f"Relevant context: {context}"))
            
            response = self.model.get_response(self.messages)
            print(f"Bot: {response}")

