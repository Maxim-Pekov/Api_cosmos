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


def message_handler(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Hi Max',
    )

def main():
    print('Start')
    updater = Updater(
        token=token,
        use_context=True
    )
    updater.dispatcher.add_handler(MessageHandler(filters=Filters.all, callback=message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
