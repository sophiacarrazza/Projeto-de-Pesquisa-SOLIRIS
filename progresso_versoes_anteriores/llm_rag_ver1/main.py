# Arquivo principal para iniciar o chatbot.

from chatbot.chatbot import ChatBot
from config import CONFIG

def main():
    chatbot = ChatBot(CONFIG)
    chatbot.start()

if __name__ == "__main__":
    main()