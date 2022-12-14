import argparse
import requests

from datetime import datetime
from environs import Env
from general_functions import get_extension, save_images, directory_path


def create_parser():
    parser = argparse.ArgumentParser(
        description='Этот скрипт сохраняет фотографии в папку epic images, взятые с сайта Nasa. Если кол-во фото не задано, сохраняет одну фотографию')
    parser.add_argument('-i', '--images_count', help='кол-во скачиваемых фото', default=1, type=int)
    return parser


def get_epic_photos_information(images_count, nasa_token):
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': nasa_token,
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_photos_information = response.json()[:images_count]
    return epic_photos_information


def get_epic_photos(images_count, nasa_token):
    params = {
        'api_key': nasa_token,
    }
    epic_photos_information = get_epic_photos_information(images_count, nasa_token)
    nasa_epic_photos = []
    for photo_information in epic_photos_information:
        date_str = photo_information.get('date')
        photo_id = photo_information.get('image')
        if date_str and photo_id:
            date = datetime.fromisoformat(date_str)
            epic_photo_url = f'https://api.nasa.gov/EPIC/archive/natural/{date.strftime("%Y/%m/%d")}/png/{photo_id}.png'
            response = requests.get(epic_photo_url, params=params)
            response.raise_for_status()
            photo_and_extension = response.content, get_extension(epic_photo_url)
            nasa_epic_photos.append(photo_and_extension)
    return nasa_epic_photos


def main():
    env = Env()
    env.read_env()
    nasa_token = env.str('NASA_TOKEN')
    parser = create_parser()
    args = parser.parse_args()
    images_count = args.images_count
    epic_photos = get_epic_photos(images_count, nasa_token)
    save_images(epic_photos, directory_path, 'epic_')


if __name__ == "__main__":
    main()