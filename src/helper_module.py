def clean_string(text: str) -> str:
    """
    Преобразует строку в нижний регистр и удаляет лишние пробелы
    :param text: исходная строка
    :return: очищенная строка
    """
    return text.strip().lower()