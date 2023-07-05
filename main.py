import telebot, wikipedia

token = '6005673959:AAHHunjNmhVpHT7UUsksttiKHdeAqIiK6sM'

bot = telebot.TeleBot(token)

wikipedia.set_lang('ru')

def get_wiki(s):
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]
        wikimas = wikitext.split('.')
        wikimas = wikimas[:-1]
        res = ''
        for i in wikimas:
            if not('==' in i):
                if (len((i.strip()))>3):
                    res = wikitext+i+'.'
            else:
                break
        return res
    except Exception as e:
        return 'В wikipedia нету данных об этом слове'


@bot.message_handler(commands=['start'])
def start(m):
    bot.send_message(m.chat.id, 'отпрвь любое слово я найду его на wikipedia')

@bot.message_handler(content_types=['text'])
def handle_text(message):
    bot.send_message(message.chat.id, get_wiki(message.text))

bot.polling(none_stop=True, interval = 0)