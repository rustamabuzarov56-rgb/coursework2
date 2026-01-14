from dataclasses import dataclass
from typing import Optional


@dataclass
class Vacancy:
    """Класс для представления вакансии с возможностью её описания и сравнения по уровню зарплаты."""
    __slots__ = ("title", "salary_from", "salary_to", "employer")
    title: str
    salary_from: Optional[int]
    salary_to: Optional[int]
    employer: str

    def __post_init__(self):
        """Проверяет правильность введенных данных при создании объекта"""
        if not isinstance(self.title, str):
            raise ValueError("Название вакансии должно быть строкой.")

    def __lt__(self, other: 'Vacancy') -> bool:
        """Определяет порядок сортировки вакансий по минимальному значению зарплаты."""
        my_salary = self.salary_from if self.salary_from is not None else 0
        other_salary = other.salary_from if other.salary_from is not None else 0
        return my_salary < other_salary

    def __repr__(self) -> str:
        """Возвращает удобное для чтения строковое представление объекта вакансии"""
        return f'Vacancy(title="{self.title}", salary={self.salary_from}-{self.salary_to}, employer="{self.employer}")'
