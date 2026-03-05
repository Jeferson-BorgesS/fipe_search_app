import requests
from app.core.exceptions import FipeConnectionError
from app.utils.logger import logger


BASE_URL = "https://parallelum.com.br/fipe/v2"
timeout = 10

class Fipeservice:
    @staticmethod
    def _get(endpoint: str):
        try:
            response = requests.get(f"{BASE_URL}{endpoint}", timeout=timeout)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            raise RuntimeError(f"Erro ao acessar API FIPE: {e}")
        
    @classmethod
    def get_marcas(cls):
        return cls._get("/carros/marcas")
    
    @classmethod
    def get_modelos(cls, codigo_marca):
        return cls._get(f"/carros/marcas/{codigo_marca}/modelos")
    
    @classmethod
    def get_anos(cls, codigo_marca, codigo_modelo):
        return cls._get(
            f"/carros/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos"
        )
    
    @classmethod
    def get_valor(cls, codigo_marca, codigo_modelo, codigo_ano):
        return cls._get(
            f"/carros/marcas/{codigo_marca}/modelos/{codigo_modelo}/anos/{codigo_ano}"
        )