from abc import ABC, abstractmethod, ABCMeta
from http.client import responses

import requests
import json

from mypy.strconv import indent


class AbstractHhService(ABC):
        """Aбстрактный класс для работы с API сервиса с вакансиями"""
        @abstractmethod
        def _AbstractHhService__connect(self):
            """"Метод подключения к API сервиса"""
            pass

        @abstractmethod
        def get_vacancies(self, keyword: str) -> None:
            """Метод получения вакансий по ключевому слову"""
            pass

class HeadHunterAPI(AbstractHhService):

        """Kласс для работы с платформой hh.ru"""
        __BASE_URL = 'https://api.hh.ru/vacancies'
        def _AbstractHhService__connect(self) -> None:
            """Приватный метод для подключения к API hh.ru"""
            headers = {
                "User-Agent": "coursework/2.0 (rustamabuzarov56@gmail.com)"
            }
            try:
                response = requests.get(self.__BASE_URL, headers=headers)
                if response.status_code != 200:
                    raise Exception (f"Ошибка подключения {response.status_code} {response.text}")
            except requests.RequestException as e:
                print(f"Ошибка соединения: {e}")

        def get_vacancies(self, keyword: str) -> dict[list]:
            """Метод получения вакансий по ключевому слову"""
            self._AbstractHhService__connect()
            params = {
                "text": keyword,
                "per_page": 10
            }
            try:
                response = requests.get(self.__BASE_URL, params=params)
                if response.status_code != 200:
                    raise Exception (f"Ошибка подключения {response.status_code} {response.text}")
                vacancies = response.json().get("items", [])
                return vacancies
            except requests.RequestException as e:
                print(f"Ошибка отправки запроса: {e}")

hh_api = HeadHunterAPI()
print(hh_api.get_vacancies(keyword="токарь"))