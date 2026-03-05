from app.services.fipe_service import Fipeservice

if __name__ == "__main__":
    marcas = Fipeservice.get_marcas()
    print(f"Total de marcas: {len(marcas)}")
    print("Primeira marca:", marcas[0])