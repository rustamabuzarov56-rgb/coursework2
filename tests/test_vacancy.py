import pytest

from src.vacancy_module import Vacancy


def test_vacancy_creation():
    vacancy = Vacancy(title="Программист", salary_from=50000, salary_to=None, employer="ООО Рога и Копыта")
    assert vacancy.title == "Программист"
    assert vacancy.salary_from == 50000
    assert vacancy.salary_to is None
    assert vacancy.employer == "ООО Рога и Копыта"


def test_slots():
    vacancy = Vacancy(title="Менеджер проекта", salary_from=60000, salary_to=80000, employer="Google")
    with pytest.raises(AttributeError):
        vacancy.new_field = "some value"


def test_comparison():
    vacancy_1 = Vacancy(title="Разработчик", salary_from=70000, salary_to=90000, employer="Яндекс")
    vacancy_2 = Vacancy(title="Аналитик", salary_from=60000, salary_to=80000, employer="Сбербанк")
    assert vacancy_2 < vacancy_1
    assert not (vacancy_1 < vacancy_2)


def test_repr():
    vacancy = Vacancy(title="SMM специалист", salary_from=40000, salary_to=60000, employer="Красотка Media")
    expected_repr = 'Vacancy(title="SMM специалист", salary=40000-60000, employer="Красотка Media")'
    assert repr(vacancy) == expected_repr


def test_invalid_title_type():
    with pytest.raises(ValueError):
        Vacancy(title=123, salary_from=50000, salary_to=70000, employer="Facebook")
