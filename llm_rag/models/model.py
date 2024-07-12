# Definição do modelo.

from langchain_openai import ChatOpenAI

class ChatBotModel:
    def __init__(self, model_name, api_key):
       self.model = ChatOpenAI(model_name='gpt-3.5-turbo', api_key='asst_s0T4b2nrtK1mOL2103kEc6GY')

    def get_response(self, messages):
        response = self.model(messages)
        return response