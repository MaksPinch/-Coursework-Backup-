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