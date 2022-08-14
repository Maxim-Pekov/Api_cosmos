from urllib.request import urlretrieve

url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

urlretrieve(url, 'hubble.jpeg')