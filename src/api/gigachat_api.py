import time
import os
import uuid
import requests
from typing import List, Optional
from src.api.base_api import BaseApi

rquid = str(uuid.uuid4())
AUTORIZATION_DATA = os.getenv('AUTORIZATION_DATA')
# assert AUTORIZATION_DATA, "AUTORIZATION_DATA is None"
# assert isinstance(AUTORIZATION_DATA,
#                   str), "AUTORIZATION_DATA must have a string type"


class GigaChatApi(BaseApi):
    _token: Optional[str] = None
    _token_time: float = 0

    def __init__(self,
                 scope: str = 'GIGACHAT_API_PERS'
                 ) -> None:
        self.scope = scope

    def _get_token(self) -> str:

        if (
            self._token and
            self._token_time and
            (time.monotonic() - self._token_time < 1000)
        ):
            return self._token
        headers = {
            'Authorization': f'Bearer {AUTORIZATION_DATA}',
            'RqUID': str(uuid.uuid4()),
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {'scope': self.scope}
        response = requests.post(
            "https://ngw.devices.sberbank.ru:9443/api/v2/oauth",
            headers=headers,
            data=data,
            verify=False
        )
        if response.status_code == 200:
            self._token_time = time.monotonic()
            self._token = response.json()["access_token"]
            if isinstance(self._token, str):
                return self._token
        raise Exception(f'Error[{response.status_code}]: {response.text}')

    def completions(self,
                    messages: List[dict],
                    model: str = 'GigaChat:latest',
                    temperature: int = 1
                    ) -> str:
        token = self._get_token()
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {token}'
        }
        data = {
            'messages': messages,
            'model': model,
            'temperature': temperature,
        }
        response = requests.post(
            'https://gigachat.devices.sberbank.ru/api/v1/chat/completions',
            headers=headers,
            json=data,
            verify=False
        )
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        raise Exception(f'Error[{response.status_code}]: {response.text}')
    
  
