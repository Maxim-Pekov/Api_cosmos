import argparse
from datetime import datetime

import requests

from main import get_extension, save_images, directory_path
from main import env


def create_parser():
    parser = argparse.ArgumentParser(
        description='Этот скрипт сохраняет фотографии в папку epic images, взятые с сайта Nasa. Если кол-во фото не задано, сохраняет одну фотографию')
    parser.add_argument('-i', '--images_count', help='кол-во скачиваемых фото', default=1)
    return parser


def get_epic_photos_information(images_count):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': env.str('NASA_TOKEN'),
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_photos_information = response.json()[:int(images_count)]

    return epic_photos_information


def get_epic_photos(images_count):
    params = {
        'api_key': env.str('NASA_TOKEN'),
    }
    epic_photos_information = get_epic_photos_information(images_count)
    nasa_epic_photos = []
    for i in epic_photos_information:
        date = i['date']
        d = datetime.fromisoformat(date)
        photo_id = i['image']
        e = f'https://api.nasa.gov/EPIC/archive/natural/{d.year}/{d.strftime("%m")}/{d.strftime("%d")}/png/{photo_id}.png'
        response = requests.get(e, params=params)
        response.raise_for_status()
        epic_photo = response.content
        photo_extension = []
        photo_extension.append(epic_photo)
        photo_extension.append(get_extension(e))
        nasa_epic_photos.append(photo_extension)
    return nasa_epic_photos


def main():
    parser = create_parser()
    args = parser.parse_args()
    images_count = args.images_count
    epic_photos = get_epic_photos(images_count)
    save_images(epic_photos, directory_path, 'epic_')


if __name__ == "__main__":
    main()