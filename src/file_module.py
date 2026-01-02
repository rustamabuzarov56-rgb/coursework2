
class Vacancy:
    """Класс для работы с вакансиями"""
    __slots__ = ("title", "salary", "description", "company")

    def __init__(self, title, salary, description, company):
        """Конструктор класса Vacancy"""
        self.title = self.__validate_title(title)
        self.salary = self.__validate_salary(salary)
        self.description = self.__validate_description(description)
        self.company = self.__validate_company(company)

    def __str__(self):
        """Возвращает читаемое представление объекта"""
        return f"Вакансия {self.title}, {self.salary}"

    # Магические методы для сравнения вакансий по зарплате
    def __lt__(self, other):
        """Определяет порядок следования вакансий по размеру зарплаты"""
        return self.salary < other.salary

    def __le__(self, other):
        """Определяет отношение "меньше или равно" для вакансий по зарплате"""
        return self.salary <= other.salary

    def __ge__(self, other):
        """Определяет отношение "больше или равно" для вакансий по зарплате"""
        return self.salary >= other.salary

    def __eq__(self, other):
        """Определяет равенство вакансий по зарплате"""
        return self.salary == other.salary

    def __ne__(self, other):
        """Определяет неравенство вакансий по зарплате"""
        return self.salary != other.salary

    # Приватные методы валидации данных
    def __validate_title(self, value):
        """Приватный метод валидации названия вакансии.
           Проверяет, что оно является непустой строкой"""
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Название вакансии должно быть строкой и не пустым")
        return value

    def __validate_salary(self, value):
        """Приватный метод валидации зарплаты.
           Проверяет, что зарплата является неотрицательным числом"""
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Зарплата должна быть неотрицательным числом")
        return value

    def __validate_description(self, value):
        """Приватный метод валидации описания вакансии.
           Проверяет, что описание является непустой строкой"""
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Описание вакансии должно быть строкой и не пустым")
        return value

    def __validate_company(self, value):
        """Приватный метод валидации компании.
           Проверяет, что название компании является непустой строкой"""
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Название компании должно быть строкой и не пустым")
        return value

try:
    vak1 = Vacancy(
        title="Разработчик",
        salary=80000,
        description="Создание веб-сайтов",
        company="Интернет-сервисы"
    )
except ValueError as err:
    print(err)

try:
    vak2 = Vacancy(
        title="Дизайнер",
        salary=-50000,  # Некорректное значение зарплаты
        description="Графический дизайн",
        company="Студия дизайна"
    )
except ValueError as err:
    print(err)

# Попытка сравнения вакансий
if vak2 is not None:
    print(vak1 < vak2)
else:
    print("Вторая вакансия не создана из-за ошибки валидации")