import argparse
import requests

from general_functions import get_extension, save_images, directory_path


def create_parser():
    parser = argparse.ArgumentParser(
        description='Этот скрипт сохраняет фотографии в папку images, взятые с сайта Spacex по id полета. Если id не задан сохраняет фото с последнего полета')
    parser.add_argument('-id', '--launch_id', help='Передаваемый id полета', default='latest')
    return parser


def get_spacex_photos(flight_id):
    """Возвращает список фотографий в байтах с их разрешением полученных с spacex используя flight_id"""

    response = requests.get(f'https://api.spacexdata.com/v5/launches/{flight_id}')
    response.raise_for_status()
    spacex_photo_links = response.json().get('links')
    spacex_photo_flickr = spacex_photo_links.get('flickr')
    spacex_photo_urls = spacex_photo_flickr.get('original')
    spacex_photos = []
    if spacex_photo_links and spacex_photo_flickr and spacex_photo_urls:
        for spacex_photo_url in spacex_photo_urls:
            response = requests.get(spacex_photo_url)
            response.raise_for_status()
            spacex_photo = response.content, get_extension(spacex_photo_url)
            spacex_photos.append(spacex_photo)
    return spacex_photos


def main():
    parser = create_parser()
    args = parser.parse_args()
    launch_id = args.launch_id
    spacex_photos = get_spacex_photos(launch_id)
    save_images(spacex_photos, directory_path, 'spacex_')


if __name__ == "__main__":
    main()