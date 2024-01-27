#  Saiga_mistral_7b
import requests
from typing import List
from src.api.base_api import BaseApi


class SaigaApi(BaseApi):
    def completions(self,
                    messages: List[dict]
                    ) -> str:
        headers = {
            'Content-Type': 'application/json',
            'accept': 'application/json'
        }
        data = {
            "template": "{% for message in messages %}{{'<s>' ~ message.role ~ '\n' ~ message.content ~ '</s>'}}{% endfor %}<s>bot\n",
            "messages": messages,
            "config": {
                "temperature": 0.1,
                "top_p": 0.9,
                "top_k": 40,
                "repeat_penalty": 1.5,
                "max_tokens": -1
            }

        }
        response = requests.post(
            'https://m.ml.ocas.ai/api/text-generation/chat/completions',
            headers=headers,
            json=data
        )
        if response.status_code == 200:
            return response.json()["message"]["content"]
        raise Exception(f'Error[{response.status_code}]: {response.text}')
