import pathlib
import requests
from urllib.request import urlretrieve

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
directory_path = 'images'


def download_images(url, directory_path, name_photo=None):
    if name_photo is None:
        name_photo = url.split("/")[-1]
    pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)
    urlretrieve(url, f'{directory_path}/{name_photo}.jpeg')


def get_photo_links(flight_id):
    response = requests.get(f'https://api.spacexdata.com/v5/launches/{flight_id}')
    spacex_photo_urls = response.json()['links']['flickr']['original']
    return spacex_photo_urls


def main():
    spacex_photo_urls = get_photo_links('61e048ffbe8d8b66799018d1')
    for number_url, url in enumerate(spacex_photo_urls):
        download_images(url, directory_path, f'spacex_{number_url}')


if __name__ == "__main__":
    main()
