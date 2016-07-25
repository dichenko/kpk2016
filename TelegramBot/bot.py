# -*- coding: utf-8 -*-
import config
import telebot

def listener(messages):
    print(messages)
    #messages = int(messages)
    bot.send_message(m.chat.id, m.text)

if __name__ == '__main__':
     bot = telebot.TeleBot(config.token)
     bot.set_update_listener(listener)
     bot.polling(none_stop=True)



def nameGen(namesCount):

    slogi = ['мур', 'ма', 'ко', 'ля', 'ва', 'ры', 'ле', 'до', 'де',
         'ка', 'му', 'мю', 'рю', 'лю', 'бе', 'би', 'ко', ]
    okonch = ['чка', 'чик', 'ка', 'а', 'рик', 'шка', 'сик',  ]
    name = ''
    for i in range(namesCount):
        slogCount = randrange(1,4)
        for k in range(slogCount):
            name += choice(slogi)
        name += choice(okonch)
        print (name, )
        name = ''



