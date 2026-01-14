import json
import os
import tempfile

import pytest

from src.file_module import JsonFileHandler


@pytest.fixture
def temp_json_file():
    fd, path = tempfile.mkstemp(suffix=".json")
    yield path
    os.close(fd)
    os.unlink(path)


def test_read_data(temp_json_file):
    handler = JsonFileHandler(temp_json_file)

    assert handler.read_data() == [], "Метод должен вернуть пустой список при отсутствии файла."

    example_data = [{"title": "Article One"}, {"title": "Article Two"}]
    with open(temp_json_file, "w", encoding="UTF-8") as f:
        json.dump(example_data, f)

    loaded_data = handler.read_data()
    assert loaded_data == example_data, "Чтение данных прошло некорректно."


def test_write_data(temp_json_file):
    handler = JsonFileHandler(temp_json_file)

    new_data = [{"title": "Article Three"}, {"title": "Article Four"}]

    handler.write_data(new_data)
    written_data = handler.read_data()
    assert len(written_data) == len(new_data), "Количество записанных данных не соответствует ожиданиям."
    assert sorted(written_data, key=lambda x: x["title"]) == sorted(
        new_data, key=lambda x: x["title"]
    ), "Неверно сохранены данные."

    additional_data = [{"title": "Article Three"}, {"title": "Article Five"}]
    handler.write_data(additional_data)
    updated_data = handler.read_data()
    assert len(updated_data) == 3, "Некорректно удаляются дубликаты."
    expected_titles = ["Article Three", "Article Four", "Article Five"]
    actual_titles = [entry["title"] for entry in updated_data]
    assert sorted(actual_titles) == sorted(expected_titles), "Несоответствие заголовков статей."
