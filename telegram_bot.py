import argparse
import os
import random

import telegram
from environs import Env
from pathlib import Path


env = Env()
env.read_env()
token = env.str('TOKEN')
chat_id = env.int('CHAT_ID')


def create_parser():
    parser = argparse.ArgumentParser(
        description='публикует фотографии в группу телеграмм')
    parser.add_argument('-p', '--photo_name', help='Передаваемое имя фотографии')
    return parser


def publish_photo(path):
    bot = telegram.Bot(token=token)
    image_path = Path() / 'images' / path
    bot.send_document(chat_id=-chat_id, document=open(image_path, 'rb'))


parser = create_parser()
args = parser.parse_args()
photo_name = args.photo_name
photos = os.listdir(env.str('DIRECTORY_PATH'))
random_photo = random.choice(photos)
publish_photo(photo_name) if photo_name else publish_photo(random_photo)




