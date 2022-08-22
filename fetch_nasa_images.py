import argparse
import requests

from main import get_extension, save_images, directory_path
from main import env


def create_parser():
    parser = argparse.ArgumentParser(
        description='Этот скрипт сохраняет фотографии в папку images, взятые с сайта Nasa. Если кол-во фото не задано, сохраняет одну фотографию')
    parser.add_argument('-i', '--images_count', help='кол-во скачиваемых фото', default=1)
    return parser


def get_nasa_photos_content(number_of_contents):
    """Возвращает список фотографий в байтах с их разрешением полученных с nasa в кол-ве number_of_contents"""

    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': env.str('NASA_TOKEN'),
        'count': number_of_contents
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    info_photos = response.json()
    nasa_photos = []
    for info_photo in info_photos:
        nasa_photo_url = info_photo.get('hdurl')
        response = requests.get(nasa_photo_url)
        response.raise_for_status()
        nasa_photo = response.content, get_extension(nasa_photo_url)
        nasa_photos.append(nasa_photo)
    return nasa_photos


def main():
    parser = create_parser()
    args = parser.parse_args()
    images_count = args.images_count
    nasa_photos = get_nasa_photos_content(images_count)
    save_images(nasa_photos, directory_path, 'nasa_')


if __name__ == "__main__":
    main()
