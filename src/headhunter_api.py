from abc import ABC, abstractmethod

import requests
import json
class AbstractHHService(ABC):
        """Aбстрактный класс для работы с API сервиса с вакансиями"""
        @abstractmethod
        def get_vacancies(self):
            pass


class HeadHunterAPI(AbstractHHService):
        """Kласс, наследующийся от абстрактного класса, для работы с платформой hh.ru"""
        BASE_URL = 'https://api.hh.ru/vacancies'
        def get_vacancies(self, params=None):
                """Метод для получения вакансий с использованием API HeadHunter"""
                headers = {"User-Agent": "MyCourseWorkApp/1.0 (rustamabuzarov56@gmail.com)"}
                try:
                        response = requests.get(self.BASE_URL, headers=headers)
                        if response.status_code != 200:
                                raise Exception(f"Ошибка запроса: {response.status_code} {response.text}")
                        return response.json()
                except requests.RequestException as e:
                        print(f"Ошибка связи с сервером {e}")

