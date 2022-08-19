import telegram
import logging
from environs import Env
from telegram.ext import Updater
from telegram import Update
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler, MessageHandler, Filters

env = Env()
env.read_env()
token = env.str('TOKEN')


# def message_handler(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         text='Hi Max',
#     )
#
# def main():
#     print('Start')
#     updater = Updater(
#         token=token,
#         use_context=True
#     )
#     updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))
#
#     updater.start_polling()
#     updater.idle()
#
# if __name__ == '__main__':
#     main()
bot = telegram.Bot(token=token)
print(bot.get_me())
# updates = bot.get_updates()
# print(updates[0])

bot.send_message(text='Hi John!', chat_id=-1001626507075)
bot.send_document(chat_id=-1001626507075, document=open('images/nasa_0.jpg', 'rb'))


# bot.send_message(chat_id=chat_id, text="I'm sorry Dave I'm afraid I can't do that.")