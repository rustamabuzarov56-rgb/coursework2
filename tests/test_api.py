from unittest.mock import Mock, patch

import pytest

from src.api_module import HhApiClient


def test_connect():
    client = HhApiClient()

    with patch("requests.get") as mocked_get:
        mocked_response = Mock()
        mocked_response.status_code = 200
        mocked_get.return_value = mocked_response

        result = client._connect()
        assert result is True

    with patch("requests.get") as mocked_get:
        mocked_response = Mock()
        mocked_response.status_code = 404
        mocked_get.return_value = mocked_response

        result = client._connect()
        assert result is False


@patch("requests.get")
def test_fetch_data(mocked_get):
    client = HhApiClient()

    mocked_response = Mock()
    mocked_response.json.return_value = {"items": [{"name": "Python Developer"}, {"name": "JavaScript Developer"}]}
    mocked_get.return_value = mocked_response

    results = client.fetch_data("developer")
    expected_results = [{"name": "Python Developer"}, {"name": "JavaScript Developer"}]
    assert len(results) == 2
    assert results == expected_results


@patch("requests.get")
def test_fetch_data_error(mocked_get):
    client = HhApiClient()

    mocked_response = Mock()
    mocked_response.status_code = 500
    mocked_response.json.side_effect = Exception("API error")
    mocked_get.return_value = mocked_response

    with pytest.raises(Exception):
        client.fetch_data("developer")
