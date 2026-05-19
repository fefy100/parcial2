import requests
from requests.exceptions import HTTPError, ConnectionError, Timeout
from concurrent.futures import ThreadPoolExecutor
import time


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

    BASE = "https://restcountries.com/v3.1"

    def by_name(self, name):

        url = f"{self.BASE}/name/{name}"

        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            data = r.json()[0]
            return Country(data)

        except Timeout:
            print("La API tardó demasiado")

        except ConnectionError:
            print("Sin conexión a internet")

        except HTTPError as e:
            print(f"Error {e.response.status_code}")

        return None

    def by_region(self, region):

        url = f"{self.BASE}/region/{region}"

        try:
            r = requests.get(url, timeout=5)
            r.raise_for_status()
            data = r.json()

            return [Country(p) for p in data]

        except Timeout:
            print("Timeout")

        except ConnectionError:
            print("Sin internet")

        except HTTPError as e:
            print(f"Error {e.response.status_code}")

        return []

    # CONCURRENCIA
    def concurrentes(self, nombres):

        inicio = time.time()

        with ThreadPoolExecutor() as executor:
            paises = list(executor.map(self.by_name, nombres))

        fin = time.time()

        paises = [p for p in paises if p]

        print(f"\nTiempo de ejecución: {fin - inicio:.2f} segundos")

        return paises