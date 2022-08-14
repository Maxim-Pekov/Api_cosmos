import pathlib

from urllib.request import urlretrieve


url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

pathlib.Path('images').mkdir(parents=True, exist_ok=True)

urlretrieve(url, 'images/hubble.jpeg')