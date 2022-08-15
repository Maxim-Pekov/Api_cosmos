import pathlib
from pprint import pprint

import requests
from urllib.request import urlretrieve
from environs import Env

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
directory_path = 'images'


def download_images(url, directory_path, name_photo=None):
    if name_photo is None:
        name_photo = url.split("/")[-1]
    pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)
    urlretrieve(url, f'{directory_path}/{name_photo}.jpeg')


def fetch_spacex_launch_by_id(flight_id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{flight_id}')
    spacex_photo_urls = response.json()['links']['flickr']['original']
    return spacex_photo_urls


def main():
    spacex_photo_urls = fetch_spacex_launch_by_id('61e048ffbe8d8b66799018d1')
    for number_url, url in enumerate(spacex_photo_urls):
        download_images(url, directory_path, f'spacex_{number_url}')


if __name__ == "__main__":
    main()
    env = Env()
    env.read_env()
    urll = 'https://api.nasa.gov/planetary/apod'
    params = {
        'api_key': env.str('NASA_TOKEN'),
    }
    resp = requests.get(urll, params=params)
    pprint(resp.json()['hdurl'])
