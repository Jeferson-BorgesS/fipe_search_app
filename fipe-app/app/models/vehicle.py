from dataclasses import dataclass

@dataclass
class Marca:
    codigo: str
    nome: str

@dataclass
class Modelo:
    codigo: str
    nome: str

@dataclass
class Ano:
    codigo: str
    nome: str

@dataclass
class VeiculosFipe:
    valor: str
    marca: str
    modelo: str
    ano_modelo: int
    combustivel: str
    codigo_fipe: str