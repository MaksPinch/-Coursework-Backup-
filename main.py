import configparser
import json
from tqdm import tqdm
import requests
from typing import List, Dict

class VKAPIClient:
    """
    Клиент для работы с API ВКонтакте, позволяющий получать фотографии профиля пользователя.

    Атрибуты:
        token (str): Токен доступа для API VK.
        user_id (int): ID пользователя VK, чьи данные необходимо получить.
    """

    API_BASE_URL = 'https://api.vk.com/method'

    def __init__(self, token: str, user_id: int) -> None:
        """
        Инициализирует клиент VK API.

        :param token: str - Токен доступа VK API.
        :param user_id: int - ID пользователя VK.
        """
        self.token = token
        self.user_id = user_id


    def get_common_params(self) -> Dict:
        """
        Возвращает базовые параметры для запросов к API VK.

        :return: dict - Словарь с параметрами 'access_token' и 'v' (версия API).
        """
        return {
            "access_token": self.token,
            "v": '5.199'
        }

    def _build_url(self, api_method: str) -> str:
        """
        Формирует URL для вызова метода API VK.

        :param api_method: str - Название метода API.
        :return: str - Полный URL запроса.
        """
        return f'{self.API_BASE_URL}/{api_method}'

    def get_profile_photo(self) -> dict:
        """
        Получает фотографии профиля пользователя.

        :return: dict - JSON-ответ от VK API с данными о фотографиях.
        """
        params = self.get_common_params()
        params.update({
            'owner_id': self.user_id,
            'album_id': 'profile',
            'rev': 1,  # Показывает фото в обратном порядке (новые первыми)
            'extended': 1,  # Включает дополнительные поля (количество лайков)
            'photo_sizes': 1  # Включает информацию о размерах фото
        })
        response = requests.get(self._build_url('photos.get'), params=params)
        return response.json()

    def get_largest_photo(self) -> List[Dict]:
        """
        Извлекает 5 самых больших фотографий профиля пользователя.

        :return: list - Список словарей с данными о фото (лайки, URL, дата).
        """
        photos = self.get_profile_photo()

        if 'response' in photos and 'items' in photos['response']:
            photo_items = photos['response']['items']
        else:
            return []

        max_size = []

        for photo in photo_items:
            sizes = photo.get('sizes', [])
            if not sizes:
                continue

            # Находим фото с наибольшей площадью
            max_photo_size = max(sizes, key=lambda size: size['height'] * size['width'])
            max_url = max_photo_size['url']
            likes = photo['likes']['count']
            date = photo['date']

            max_size.append({
                'likes': likes,
                'url': max_url,
                'date': date
            })

        # Сортируем по количеству лайков (при равных лайках можно сортировать по дате)
        sorted_max_size = sorted(max_size, key=lambda x: x['likes'], reverse=True)

        # Выбираем 5 самых популярных фото
        return sorted_max_size[:5]

class YD:
    """
    Клиент для работы с API Яндекс.Диска, позволяющий загружать фотографии.

    Атрибуты:
        token (str): OAuth-токен для Яндекс.Диска.
    """

    YD_URL = 'https://cloud-api.yandex.net'

    def __init__(self, token: str) -> None:
        """
        Инициализирует клиент API Яндекс.Диска.

        :param token: str - OAuth-токен для Яндекс.Диска.
        """
        self.token = token




class JSONSaver:
    """
    Класс для сохранения информации о фотографиях в JSON-файл.
    """