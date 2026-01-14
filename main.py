from src.api_module import HhApiClient
from src.vacancy_module import Vacancy
from src.file_module import JsonFileHandler
from src.helper_module import clean_string


def main():
    client = HhApiClient()
    file_handler = JsonFileHandler('hh_data.json')

    while True:
        keyword = input("Введите ключевое слово для поиска вакансий (или введите 'exit'): ")
        if keyword.lower() == 'exit':
            break

        cleaned_keyword = clean_string(keyword)
        raw_data = client.fetch_data(cleaned_keyword)

        vacancies = [
            Vacancy(
                title=data['name'],
                salary_from=data['salary']['from'] if data['salary'] else None,
                salary_to=data['salary']['to'] if data['salary'] else None,
                employer=data['employer']['name']
            )
            for data in raw_data
        ]

        print("\nВакансии:")
        for v in sorted(vacancies):
            print(v)

        file_handler.write_data([
            {'title': v.title, 'salary_from': v.salary_from, 'salary_to': v.salary_to, 'employer': v.employer}
            for v in vacancies
        ])

        print("Вакансии успешно сохранены!")

if __name__ == "__main__":
    main()