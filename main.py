import pathlib
import requests

from datetime import datetime
from os.path import splitext
from urllib.parse import urlparse
from environs import Env


# url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
directory_path = 'images'
env = Env()
env.read_env()


def save_images(contents, directory_path, name_photo):
    """Создает директорию {directory_path} в корне проекта и сохраняет туда переданные фотографии"""

    pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)
    for number_url, content in enumerate(contents):
        pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)
        with open(f'{directory_path}/{name_photo}{number_url}{content[1]}', 'wb') as file:
            file.write(content[0])


def get_spacex_photos_launch_by_id(flight_id):
    """Возвращает список фотографий в байтах с их разрешением полученных с spacex используя flight_id"""

    response = requests.get(f'https://api.spacexdata.com/v5/launches/{flight_id}')
    response.raise_for_status()
    spacex_photo_urls = response.json()['links']['flickr']['original']
    spacex_photos = []
    for spacex_photo_url in spacex_photo_urls:
        response = requests.get(spacex_photo_url)
        response.raise_for_status()
        spacex_photo = []
        spacex_photo.append(response.content)
        spacex_photo.append(get_extension(spacex_photo_url))
        spacex_photos.append(spacex_photo)
    return spacex_photos


def get_extension(url):
    parse_result = urlparse(url)
    url_path = parse_result.path
    extension = splitext(url_path)[1]
    return extension


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
        nasa_photo_url = info_photo['hdurl']
        response = requests.get(nasa_photo_url)
        response.raise_for_status()
        nasa_photo = []
        nasa_photo.append(response.content)
        nasa_photo.append(get_extension(nasa_photo_url))
        nasa_photos.append(nasa_photo)
    return nasa_photos


def get_epic_photos_information():
    url = 'https://api.nasa.gov/EPIC/api/natural/images'
    params = {
        'api_key': env.str('NASA_TOKEN'),
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    epic_photos_information = response.json()[:3]
    epic_photos_information[:5]
    return epic_photos_information


def get_epic_photos():
    params = {
        'api_key': env.str('NASA_TOKEN'),
    }
    epic_photos_information = get_epic_photos_information()
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
    launch_id = '61e048ffbe8d8b66799018d1'
    nasa_photo_urls = get_nasa_photos_content(5)
    spacex_photos = get_spacex_photos_launch_by_id(launch_id)
    nasa_epic_photos = get_epic_photos()
    save_images(nasa_photo_urls, directory_path, 'nasa_')
    save_images(spacex_photos, directory_path, 'spacex_')
    save_images(nasa_epic_photos, directory_path, 'epic_')


if __name__ == "__main__":
    main()


