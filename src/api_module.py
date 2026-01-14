from abc import ABCMeta, abstractmethod
from typing import Dict, Any, Union

import requests


class BaseAPIClient(metaclass=ABCMeta):
    """
    Абстрактный класс для взаимодействия с API
    """

    def __init__(self, base_url: str) -> None:
        self._base_url = base_url

    @abstractmethod
    def _connect(self) -> bool:
        """Подключается к API"""
        pass

    @abstractmethod
    def fetch_data(self, keyword: str) -> list[Dict]:
        """Получает данные из API"""
        pass


class HhApiClient(BaseAPIClient):
    """
    Конкретная реализация клиента для работы с API HeadHunter
    """

    def __init__(self, base_url: str = "https://api.hh.ru") -> None:
        super().__init__(base_url)

    def _connect(self) -> bool:
        response = requests.get(f"{self._base_url}/areas")
        return True if response.status_code == 200 else False

    def fetch_data(self, keyword: str) -> Any:
        params: Dict[str, Union[str, int]] = {"text": keyword, "per_page": 10}
        response = requests.get(f"{self._base_url}/vacancies", params=params)
        data = response.json()
        return data["items"]


api = HhApiClient()
print(api.fetch_data(keyword="developer"))
