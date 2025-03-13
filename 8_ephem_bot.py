"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')
import ephem


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Called /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def process_planet(update, context):
    
    tokenized = update.message.text.split(' ')
    if len(tokenized) < 2:
        update.message.reply_text('Choose a planet. Type it after /planet with space.')
    planet_name = ' '.join(tokenized[1:])

    observer = ephem.Observer()
    observer.date = ephem.now()

    try:
        planet = getattr(ephem, planet_name)()
    except AttributeError:
        update.message.reply_text(f'Sorry, no {planet_name} planet in database. Try another one.')
        return

    planet.compute(observer)
    constellation = ephem.constellation(planet)

    update.message.reply_text(f'{planet_name} today is in {constellation[1]} constellation')

    
def main():
    mybot = Updater('7933775141:AAF9TqkaGQyu-adu-38pHonxCKNvVDLKy28', use_context = True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", process_planet))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
