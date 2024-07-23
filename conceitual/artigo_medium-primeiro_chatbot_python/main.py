
import time
import telebot
from rasa.shared.nlu.interpreter import Interpreter

# Initialize the Rasa interpreter
interpreter = Interpreter.load("models/nlu")
#    

bot = telebot.TeleBot('7179547712:AAFbm9laRQUnymy8fBGKp7SpxEjdyE3yTqE')

@bot.message_handler(func=lambda message: True)
def handle_telegram_message(message):
    if message.content_type == 'text':
        user_input = message.text
        # Get Rasa response
        response = interpreter.parse(user_input)
        chatbot_response = response['text']
        bot.send_message(message.chat.id, chatbot_response)

if __name__ == '__main__':
    print('Escutando mensagens do Telegram...')
    bot.polling(none_stop=True)
