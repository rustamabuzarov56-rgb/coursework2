import json
from abc import ABCMeta, abstractmethod
from typing import Any, Dict, List


class FileHandler(metaclass=ABCMeta):
    """
    Абстрактный класс для работы с файлами
    """

    def __init__(self, filename: str):
        self._filename = filename

    @abstractmethod
    def read_data(self) -> List[Any]:
        """Читает данные из файла"""
        pass

    @abstractmethod
    def write_data(self, data: List[Any]) -> None:
        """Записывает данные в файл"""
        pass


class JsonFileHandler(FileHandler):
    """
    Класс для работы с JSON файлами
    """

    def __init__(self, filename: str = "data.json"):
        super().__init__(filename)

    def read_data(self) -> List[Dict]:
        try:
            with open(self._filename, "r", encoding="UTF-8") as f:
                content = f.read().strip()
                if not content:
                    return []  # Возвращаем пустой список, если файл пуст
                return json.loads(content)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as e:
            print(f"Ошибка парсинга JSON: {e}")
            return []

    def write_data(self, data: List[Dict]) -> None:
        existing_data = self.read_data()
        unique_data = {d["title"]: d for d in existing_data + data}.values()
        with open(self._filename, "w", encoding="UTF-8") as f:
            json.dump(list(unique_data), f, indent=4)
