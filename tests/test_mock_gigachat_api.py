import pytest
import os
import sys
from src.api.gigachat_api import GigaChatApi
from pytest_mock import MockerFixture

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


def test_get_token(mocker: MockerFixture):
    resp_mock = mocker.Mock()
    resp_mock.status_code = 200
    resp_mock.json = lambda: {"access_token": "asdasd"}
    mocker.patch(
        'requests.post',
        return_value=resp_mock,
    )

    api = GigaChatApi("...")
    assert api._get_token() == 'asdasd'


def test_raise_get_token(mocker: MockerFixture):
    resp_mock = mocker.Mock()
    resp_mock.status_code = 404
    mocker.patch(
        'requests.post',
        return_value=resp_mock,
    )
    api = GigaChatApi("...")
    with pytest.raises(Exception) as exp:
        api._get_token()
    assert 'Error' in str(exp.value)


def test_completions(mocker: MockerFixture):
    mocker.patch.object(
        GigaChatApi,
        '_get_token',
        return_value='mock_token'
    )
    resp_mock = mocker.Mock()
    resp_mock.status_code = 200
    resp_mock.json = lambda: {
        "choices":
        [
            {
                "message": {"content": 'Test content'}
            }
        ]
    }

    mocker.patch(
        'requests.post',
        return_value=resp_mock,
    )

    api = GigaChatApi("...")
    assert api.completions(
        [
            {
                "role": "system",
                "content": "Test content"
            }
        ]
    ) == 'Test content'


def test_raise_completions(mocker: MockerFixture):
    resp_mock = mocker.Mock()
    resp_mock.status_code = 404
    mocker.patch(
        'requests.post',
        return_value=resp_mock,
    )

    api = GigaChatApi("...")
    with pytest.raises(Exception) as exp:
        api.completions(
            [
                {
                    "role": "system",
                    "content": "Test content"
                }
            ]
        )
    assert 'Error' in str(exp.value)
