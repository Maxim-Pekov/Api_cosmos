import os
import time
import random

from environs import Env
from telegram_bot import publish_photo


env = Env()
env.read_env()
four_hours = 14400
secs = env.int('SECONDS_DELAY', default=four_hours)
count = 0


while True:
    images = os.listdir("images")
    random.shuffle(images)
    for image in images:
        publish_photo(image)
        time.sleep(secs)

