import pathlib, requests

from pprint import pprint
from urllib.request import urlretrieve


url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'
directory_path='images'


def download_images(url, directory_path):
    name_photo = url.split("/")[-1]
    pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)
    urlretrieve(url, f'{directory_path}/{name_photo}')


def main():
    response = requests.get('https://api.spacexdata.com/v5/launches/61e048ffbe8d8b66799018d1')
    space_urls = response.json()['links']['flickr']['original']
    for url in space_urls:
        print(url)
        download_images(url, directory_path)


if __name__ == "__main__":
    main()
