from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings
#Логгирование
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
                    )
#Функция обработки команды /start
def greet_user(bot, update):
    text = 'Вызван /start'
    logging.info(text)
    update.message.reply_text(text)

#Функция обработки сообщений пользователя с ответом и логированием
def talk_to_me(bot, update):
    user_text = "Привет {}! Ты написал: {}".format(update.message.chat.first_name, update.message.text)
    logging.info("User: %s, Chat id: %s, Message: %s", update.message.chat.username, 
                update.message.chat.id, update.message.text)
    update.message.reply_text(user_text)

#Функция коннекта с ботом и вызов функции greet_user
def main():
    mybot = Updater(settings.API_KEY)
    logging.info('Бот запускается')
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()

main()