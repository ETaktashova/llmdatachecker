import requests
from typing import List
from src.api.base_api import BaseApi


class LlamaCppApi(BaseApi):

    def completions(self,
                    messages: List[dict]
                    ) -> str:

        headers = {
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }
        data = {
            'messages': messages
        }
        response = requests.post(
            # 'http://llama-gpt-api:8000/v1/chat/completions',
            'http://localhost:3001/v1/chat/completions',
            headers=headers,
            json=data
        )
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        raise Exception(f'Error[{response.status_code}]: {response.text}')
