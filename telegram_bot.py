import telegram
from environs import Env

env = Env()
env.read_env()
token = env.str('TOKEN')


def publish_photo(path):
    bot = telegram.Bot(token=token)
    # bot.send_message(text='Hi John!', chat_id=-1001626507075)
    bot.send_document(chat_id=-1001626507075, document=open(f'images/{path}', 'rb'))


