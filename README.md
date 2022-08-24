# Api_cosmos

This is a publishing cosmos photo script.

## How does he work:

1. You set in the environment the path to the folder with the photo and the delay time for posting the photo.
2. run
```python
python publishing_photos.py
```
3. The script will publish photos to the group with a given frequency through the telegram bot.
4. If you want to post only one photo, then use the command: 
```python
python telegram_bot.py -p nasa_4.jpg
```
If you do not specify an argument, then the photo will be random from the 'images' directory
5. If you need more photos, you can upload them manually or with built-in modules to the 'images' directory.
6. Download 5 random photos from the NASA website
```python
python fetch_nasa_images.py -i 5
```

7. Download 4 random epic photos from the NASA website
```python
python fetch_epic_images.py -i 4
```

8. Upload photos from SpaceX launch by flight id, if id is not set, it will select the last launch.

```python
python fetch_spacex_images.py -h
```

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)
---
## Installation
Use these commands to start a project on your hardware.
- [x] You can mark completed tasks with checkboxes 
1. Install
```python
git clone https://github.com/Maxim-Pekov/Api_cosmos
python -m venv venv
```
2. Activate venv    
```python
.\venv\Scripts\activate         #windows
source ./venv/bin/activate      #Linux, Mac  
```
3. Go to the `./Api_cosmos` directory
4. Install requirements
```python
pip install -r requirements.txt
```
5. Create `.env` directory
6. In the directory `.env` write the following lines:
```python
DIRECTORY_PATH = 'images'   # the name of the directory where the photos will be stored.
TELEGRAM_TOKEN = '123456789qwerty'
SECONDS_DELAY = 3600        # number of seconds to delay sending a photo to a telegram group.
TELEGRAM_CHAT_ID = 123456   # your group number, you can get it by forwarding a message from the group to Get My Id (bot)
```
5. Run this command
```python
python publishing_photos.py
```
---
## About me
[<img align="left" alt="maxim-pekov | LinkedIn" width="30px" src="https://img.icons8.com/color/48/000000/linkedin-circled--v3.png" />https://www.linkedin.com/in/maxim-pekov/](https://www.linkedin.com/in/maxim-pekov/)
</br>

<img align="left" alt="maxim-pekov" width="28px" src="https://upload.wikimedia.org/wikipedia/commons/5/5c/Telegram_Messenger.png" />@MaxPekov
</br>

[//]: # (Карточка профиля: )
![](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=Maxim-Pekov&theme=solarized_dark)

[//]: # (Статистика языков в коммитах:)
[//]: # (Статистика языков в репозиториях:)
![](https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=Maxim-Pekov&theme=solarized_dark)
![](https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=Maxim-Pekov&theme=solarized_dark)



[//]: # (Статистика профиля:)
[//]: # (Данные по коммитам за сутки:)
![](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=Maxim-Pekov&theme=solarized_dark)
![](https://github-profile-summary-cards.vercel.app/api/cards/productive-time?username=Maxim-Pekov&theme=solarized_dark)

[//]: # ([![trophy]&#40;https://github-profile-trophy.vercel.app/?username=Maxim-Pekov&#41;]&#40;https://github.com/ryo-ma/github-profile-trophy&#41;)

