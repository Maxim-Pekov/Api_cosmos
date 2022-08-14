import pathlib

from urllib.request import urlretrieve


def dunload_images(url, directory_path):
    name_photo = url.split("/")[-1]
    pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)
    urlretrieve(url, f'{directory_path}/{name_photo}')


url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

dunload_images(url, directory_path='images')

