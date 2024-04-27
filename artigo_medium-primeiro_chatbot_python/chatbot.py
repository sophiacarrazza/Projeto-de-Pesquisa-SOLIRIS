from chatterbot import ChatBot #importando o chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer #importando o treinador do chatbot

chatbot = ChatBot('Draei', read_only=True) #criando o chatbot (o read_only=True é para que ele aprenda só com o treinamento, e nao com as conversas/com o usuario)
trainer = ChatterBotCorpusTrainer(chatbot) #criando o treinador do chatbot

trainer.train(
    'chatterbot.corpus.portuguese', 
    #utilização de dados padrão que a biblioteca nos disponibiliza (os dados estao em portugues) - essa linha pode ser removida para trabalhar com outro BD
    
    './data' 
    #diretorio/caminho onde estão os arquivos de treinamento
)

if __name__ == '__main__':
    while True:
        try:
            user_input = input('Usuário: ') #recebendo a solicitação do usuário
            bot_response = chatbot.get_response(user_input)

            print('Draei:', bot_response)
        except(KeyboardInterrupt, EOFError, SystemExit): #o laco fecha quando o usuário inserir CTRL + C ou CTRL + D
            break