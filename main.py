import pathlib

from os.path import splitext
from urllib.parse import urlparse
from environs import Env


env = Env()
env.read_env()
directory_path = env.str('DIRECTORY_PATH', default='images')


def save_images(contents, directory_path, name_photo):
    """Создает директорию {directory_path} в корне проекта и сохраняет туда переданные фотографии"""

    pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)
    for number_url, content in enumerate(contents):
        pathlib.Path(directory_path).mkdir(parents=True, exist_ok=True)
        with open(f'{directory_path}/{name_photo}{number_url}{content[1]}', 'wb') as file:
            file.write(content[0])


def get_extension(url):
    parse_result = urlparse(url)
    url_path = parse_result.path
    extension = splitext(url_path)[1]
    return extension

