import argparse
import os
import random

import telegram
from environs import Env
from pathlib import Path


env = Env()
env.read_env()
telegram_token = env.str('TELEGRAM_TOKEN')
telegram_chat_id = int(env.int('TELEGRAM_CHAT_ID'))
images_directory = env.str('DIRECTORY_PATH', default='images')


def create_parser():
    parser = argparse.ArgumentParser(
        description='публикует фотографии в группу телеграмм')
    parser.add_argument('-p', '--photo_name', help='Передаваемое имя фотографии')
    return parser


def publish_photo(path):
    bot = telegram.Bot(token=telegram_token)
    image_path = Path() / images_directory / path
    with open(image_path, 'rb') as img_path:
        bot.send_document(chat_id=telegram_chat_id, document=img_path)


def main():
    parser = create_parser()
    args = parser.parse_args()
    photo_name = args.photo_name
    random_photo = random.choice(os.listdir(images_directory))
    publish_photo(photo_name) if photo_name else publish_photo(random_photo)


if __name__ == '__main__':
    main()


