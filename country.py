import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout
class Country:

    def __init__(self, data: dict):
        self.nombre = data["name"]["common"]
        self.capital = data["capital"]
        self.poblacion = data["population"]
        self.area = data["area"]
        self.region = data["region"]

    def density(self):
        if self.area == 0:
            return 0
        return self.poblacion / self.area

    def comparar(self, otros: list):

        paises = [self] + otros

        # Encabezados
        print(f"{'Nombre':<20}{'Población':>15}{'Área':>18}{'Densidad':>15}")
        print("-" * 70)

        # Tabla
        for pais in paises:
            print(
                f"{pais.nombre:<20}"
                f"{pais.poblacion:>15,}"
                f"{pais.area:>18,.2f}"
                f"{pais.density():>15.2f}"
            )

        # Ganadores
        mayor_poblacion = max(paises, key=lambda x: x.poblacion)
        mayor_area = max(paises, key=lambda x: x.area)
        mayor_densidad = max(paises, key=lambda x: x.density())

        print("\nGANADORES")
        print("Mayor población:", mayor_poblacion.nombre)
        print("Mayor área:", mayor_area.nombre)
        print("Mayor densidad:", mayor_densidad.nombre)

    

# CLASE API (CONEXIÓN WEB)
class CountryAPI:

    BASE = "https://restcountries.com/v3.1"  # URL base de la API

    def by_name(self, name):
        # Busca un país por nombre
        url = f"{self.BASE}/name/{name}"  # construye URL
        try:
            r = requests.get(url, timeout=5)  # petición a la API
            r.raise_for_status()  # lanza error si la respuesta falla
            data = r.json()[0]  # toma el primer resultado
            return Country(data)  # convierte dict en objeto Country
        except Timeout:
            print("La API tardó demasiado")  # error de tiempo
        except ConnectionError:
            print("Sin conexión a internet")  # sin internet
        except HTTPError as e:
            print(f"Error {e.response.status_code}")  # error HTTP
        return None  # si falla, no devuelve país

    def by_region(self, region):
        # Busca todos los países de una región
        url = f"{self.BASE}/region/{region}"  # URL por región

        try:
            r = requests.get(url, timeout=5)  # petición
            r.raise_for_status()  # valida respuesta
            data = r.json()  # lista de países
            return [Country(p) for p in data]  # convierte todo a objetos

        except Timeout:
            print("Timeout")
        except ConnectionError:
            print("Sin internet")
        except HTTPError as e:
            print(f"Error {e.response.status_code}")
        return []  # si falla devuelve lista vacía