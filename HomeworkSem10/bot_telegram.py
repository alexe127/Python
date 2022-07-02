from telegram import  Bot
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
from task10 import start, message, cancel, couse_game
# from task10 import *



bot = Bot(token= '5599679578:AAEhvBVvBmPU6KWu1kX080WmRnIxmRI7AH4')
updater = Updater(token='5599679578:AAEhvBVvBmPU6KWu1kX080WmRnIxmRI7AH4', use_context=True)
dispatcher = updater.dispatcher


start_handler = CommandHandler('start', start)
cancel_handler = CommandHandler('cancel', cancel)
message_handler = CommandHandler('yes', message)

game_handler = MessageHandler(Filters.text, couse_game)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(cancel_handler)
dispatcher.add_handler(message_handler)
dispatcher.add_handler(game_handler)


print("Бот работает!")
updater.start_polling()
updater.idle()