
import unittest
from unittest.mock import patch, MagicMock
from src.api_module import HeadHunterAPI
import pytest


class TestHeadHunterAPI(unittest.TestCase):

    @patch("src.headhunter_api.requests")
    def test_get_vacancies_success(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "items": [
                {"id": "1", "name": "Разработчик"},
                {"id": "2", "name": "QA инженер"}
            ]
        }

        mock_requests.get.return_value = mock_response

        api = HeadHunterAPI()
        result = api.get_vacancies(keyword="Developer")

        assert len(result) == 2
        assert result[0]["name"] == "Разработчик"
        assert result[1]["name"] == "QA инженер"

    @patch("src.headhunter_api.requests.get")
    def test_get_vacancies_failure(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.text = "Not Found"
        mock_get.return_value = mock_response


        hh_api = HeadHunterAPI()
        with pytest.raises(Exception) as excinfo:
            hh_api.get_vacancies(keyword="nonexistent_job")

        assert "Ошибка подключения 404 Not Found" in str(excinfo.value)



