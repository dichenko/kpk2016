import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])

def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе

    a = message.text
    try:
        a = int(a)
        s = '2 в степени ' + str(a) + ' = ' + str(2**a)
        bot.send_message(message.chat.id, (s))

    except:
        bot.send_message(message.chat.id, ("Введите целое число"))



if __name__ == '__main__':

     bot.polling(none_stop=True)

