import os
import time
import random
import requests
import telegram

from environs import Env
from telegram_bot import publish_photo


env = Env()
env.read_env()
four_hours = 14400
sending_delay_time = env.int('SECONDS_DELAY', default=four_hours)
attempt = 0
reconnection_time = 60


while True:
    images = os.listdir("images")
    random.shuffle(images)
    for image in images:
        try:
            publish_photo(image)
        except telegram.error.NetworkError:
            attempt += 1
            if attempt == 1:
                continue
            time.sleep(reconnection_time)
            continue
        time.sleep(sending_delay_time)

