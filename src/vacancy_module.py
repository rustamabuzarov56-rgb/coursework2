from dataclasses import dataclass
from typing import Optional


@dataclass
class Vacancy:
    __slots__ = ('title', 'salary_from', 'salary_to', 'employer')
    title: str
    salary_from: Optional[int]
    salary_to: Optional[int]
    employer: str


    def __post_init__(self):
        if not isinstance(self.title, str):
            raise ValueError("Название вакансии должно быть строкой.")

    def __lt__(self, other):
        return self.salary_from or 0 < other.salary_from or 0

    def __repr__(self):
        return f'Vacancy(title="{self.title}", salary={self.salary_from}-{self.salary_to}, employer="{self.employer}")'

v = Vacancy('Менеджер проектов', 60000, 80000, 'ООО Яблоко')
print(v)