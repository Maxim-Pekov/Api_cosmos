import os
import time
import random

from environs import Env
from Api_cosmos import telegram_bot

env = Env()
env.read_env()
four_hours = 14400
secs = env.int('SECONDS_DELAY', default=four_hours)
count = 0




while True:
    images = os.listdir("images")
    print(images)
    random.shuffle(images)
    print(images)
    for number_img, image in enumerate(images):
        print(number_img)
        print(images)
        telegram_bot.publish_photo(image)
        time.sleep(secs)

