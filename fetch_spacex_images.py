import argparse
import requests

from main import get_extension, save_images, directory_path


def create_parser():
    parser = argparse.ArgumentParser(
        description='Этот скрипт сохраняет фотографии в папку images, взятые с сайта Spacex по id полета. Если id не задан сохраняет фото с последнего полета')
    parser.add_argument('-id', '--launch_id', help='Передаваемый id полета', default='latest')
    return parser


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


def main():
    parser = create_parser()
    args = parser.parse_args()
    launch_id = args.launch_id
    # launch_id = '61e048ffbe8d8b66799018d1'
    spacex_photos = get_spacex_photos_launch_by_id(launch_id)
    save_images(spacex_photos, directory_path, 'spacex_')


if __name__ == "__main__":
    main()