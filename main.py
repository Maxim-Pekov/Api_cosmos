import os.path
import pathlib
from os.path import splitext
from pprint import pprint
from urllib.parse import urlparse

import requests
from urllib.request import urlretrieve
from environs import Env


url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
directory_path = 'images'
env = Env()
env.read_env()


def save_images(photos, directory_path, name_photo=None):
    """Создает директорию {directory_path} в корне проекта и сохраняет туда фотографии из переданных списком ссылок"""
    for number_url, url in enumerate(photos):
        extension = get_extension(url)
        pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)
        urlretrieve(url, f'{directory_path}/{name_photo}{number_url}{extension}')


def get_spacex_photo_launch_by_id(flight_id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{flight_id}')
    response.raise_for_status()
    spacex_photo_urls = response.json()['links']['flickr']['original']
    return spacex_photo_urls


def get_extension(url):
    parse_result = urlparse(url)
    url_path = parse_result.path
    extension = splitext(url_path)[1]
    return extension


def get_nasa_photos_urls(number_of_urls):
    url = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': env.str('NASA_TOKEN'),
        'count': number_of_urls
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    info_photos = response.json()
    nasa_photos_urls = []
    for info_photo in info_photos:
        nasa_photos_urls.append(info_photo['hdurl'])
    return nasa_photos_urls


def main():
    nasa_photo_urls = get_nasa_photos_urls(5)
    spacex_photo_urls = get_spacex_photo_launch_by_id('61e048ffbe8d8b66799018d1')
    save_images(nasa_photo_urls, directory_path, 'nasa')
    save_images(spacex_photo_urls, directory_path, 'spacex')


if __name__ == "__main__":
    main()


