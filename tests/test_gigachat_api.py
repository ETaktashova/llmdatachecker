from src.api.gigachat_api import GigaChatApi
import pytest
import os
import sys
a_data = os.getenv('AUTORIZATION_DATA')
assert a_data, "AUTORIZATION_DATA is None"

current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)


@pytest.fixture
def api():
    user = GigaChatApi(a_data)
    return user


def test_get_token(api: GigaChatApi):
    token = api._get_token()
    assert isinstance(token, str)
    assert len(token) > 0


@pytest.mark.parametrize(
    "line1,line2",
    [
        ("I love you", "Копать картошку хорошо"),
        ("I hate you", "Мать устраняла грязь на раме"),
        ("кушать это хорошо", "питаться это полезно")
    ]
)
def test_completions(api: GigaChatApi, line1: str, line2: str):
    messages = [
        {
            'role': 'system',
            'content': (
                'Ты филолог, помогающий пользователю сравнить '
                'два предложения по его смысловому содержанию.'
                'Ты проводишь семантический анализ этих предложений и стараешься '
                'быть максимально точным.Ты отвечаешь только Да и Нет на вопрос: '
                '"Касается ли тема одного предложения темы другого предложения?" '
                'либо на вопрос:'
                '"Раскрывает ли одно предложение смысл другого предложения?"'
            )
        },
        {
            'role': 'user',
            'content': (
                'предложение 1: "Мама мыла раму"\n'
                'предложение 2: "Копать картошку хорошо"'
            )
        },
        {
            'role': 'assistant',
            'content': 'Нет'
        },
        {
            'role': 'user',
            'content': (
                'предложение 1: "Мама мыла раму"\n'
                'предложение 2: "Мать устраняла грязь на раме"'
            )
        },
        {
            'role': 'assistant',
            'content': 'Да'
        },
        {
            'role': 'user',
            'content': (
                f'предложение 1: "{line1}"\n'
                f'предложение 2: "{line2}"'
            )
        }
    ]
    response = api.completions(messages)
    assert isinstance(response, str)
