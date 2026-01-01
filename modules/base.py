"""Base Llama client for educational AI applications"""
import requests
import json
from typing import Generator

class LlamaClient:
    def __init__(self, base_url: str = "http://localhost:11434", model: str = "llama3.2"):
        self.base_url = base_url
        self.model = model
    
    def generate(self, prompt: str, system_prompt: str = "", stream: bool = False) -> str | Generator:
        url = f"{self.base_url}/api/generate"
        payload = {"model": self.model, "prompt": prompt, "system": system_prompt, "stream": stream}
        if stream:
            return self._stream_response(url, payload)
        response = requests.post(url, json=payload)
        response.raise_for_status()
        return response.json().get("response", "")
    
    def _stream_response(self, url: str, payload: dict) -> Generator:
        with requests.post(url, json=payload, stream=True) as response:
            response.raise_for_status()
            for line in response.iter_lines():
                if line:
                    data = json.loads(line)
                    if "response" in data: yield data["response"]
                    if data.get("done", False): break
