import pathlib

from os.path import splitext
from urllib.parse import urlparse
from environs import Env
from pathlib import Path


env = Env()
env.read_env()
directory_path = env.str('DIRECTORY_PATH', default='images')


def save_images(contents, directory_path, name_photo):
    """Создает директорию {directory_path} в корне проекта и сохраняет туда переданные фотографии"""

    pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)
    for number_url, content in enumerate(contents):
        image, extension = content
        outpath = Path() / directory_path / f'{name_photo}{number_url}{extension}'
        with open(outpath, 'wb') as file:
            file.write(image)


def get_extension(url):
    parse_result = urlparse(url)
    url_path = parse_result.path
    only_path, extension = splitext(url_path)
    return extension

