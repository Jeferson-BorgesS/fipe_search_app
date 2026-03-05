from app.services.fipe_service import Fipeservice
from app.models.vehicle  import Marca,Modelo, Ano, VeiculosFipe

class FipeController:

    def listar_marcas(self):
        data = Fipeservice.get_marcas()
        return [
            Marca(codigo=item["codigo"], nome=item["nome"])
            for item in data
        ]

    def listar_modelos(self, codigo_marca):
        data = Fipeservice.get_modelos(codigo_marca)
        return [
            Modelo(codigo=item["codigo"], nome=item["nome"])
            for item in data["modelos"]
        ]

    def listar_anos(self, codigo_marca, codigo_modelo):
        data = Fipeservice.get_anos(codigo_marca, codigo_modelo)
        return [
            Ano(codigo=item["codigo"], nome=item["nome"])
            for item in data
        ]

    def consultar_valor(self, codigo_marca, codigo_modelo, codigo_ano):
        data = Fipeservice.get_valor(
            codigo_marca,
            codigo_modelo,
            codigo_ano
        )

        return VeiculosFipe(
            valor=data["Valor"],
            marca=data["Marca"],
            modelo=data["Modelo"],
            ano_modelo=data["AnoModelo"],
            combustivel=data["Combustivel"],
            codigo_fipe=data["CodigoFipe"]
        )
    
