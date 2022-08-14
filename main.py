import pathlib

from urllib.request import urlretrieve


url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'


def download_images(url, directory_path):
    name_photo = url.split("/")[-1]
    pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)
    urlretrieve(url, f'{directory_path}/{name_photo}')


if __name__ == "__main__":
    download_images(url, directory_path='images')
