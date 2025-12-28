
import unittest
from unittest.mock import patch, MagicMock
from src.headhunter_api import HeadHunterAPI



class TestHeadHunterAPI(unittest.TestCase):

    @patch("src.headhunter_api.requests")
    def test_get_vacancies_success(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {'vacancies': ['Job1', 'Job2']}


        mock_requests.get.return_value = mock_response

        api = HeadHunterAPI()
        result = api.get_vacancies()

        self.assertEqual(result, {'vacancies': ['Job1', 'Job2']})
        mock_requests.get.assert_called_once_with(
            'https://api.hh.ru/vacancies',
            headers={"User-Agent": "MyCourseWorkApp/1.0 (rustamabuzarov56@gmail.com)"}
        )

    @patch("src.headhunter_api.requests")
    def test_get_vacancies_failure(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 404
        mock_response.json.return_value = {"message": "Not found"}

        mock_requests.get.return_value = mock_response

        api = HeadHunterAPI()
        with self.assertRaises(Exception):
            api.get_vacancies()

        mock_requests.get.assert_called_once_with(
            'https://api.hh.ru/vacancies',
            headers={"User-Agent": "MyCourseWorkApp/1.0 (rustamabuzarov56@gmail.com)"}
                                                 )




