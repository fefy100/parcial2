import requests

BASE = "https://restcountries.com/v3.1"

def get_country(name: str) -> dict:
    url = f"{BASE}/name/{name}"
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    return r.json()[0]     # primer resultado


# probamos
arg = get_country("argentina")
print(arg["name"]["common"])
print(arg["capital"][0])
print(arg["population"])

def mostrar(p: dict):
    nombre    = p["name"]["common"]
    capital   = p.get("capital", ["—"])[0]
    region    = p.get("region", "—")
    poblacion = p.get("population", 0)
    area      = p.get("area", 0)
    densidad  = poblacion / area if area else 0

    print(f"{nombre} ({region})")
    print(f"  Capital:  {capital}")
    print(f"  Población: {poblacion:,}")
    print(f"  Densidad:  {densidad:.2f} hab/km²")

def get_region(region: str) -> list:
    url = f"{BASE}/region/{region}"
    r = requests.get(url, timeout=5)
    r.raise_for_status()
    return r.json()           # lista de dicts


# traer sudamérica
paises = get_region("south america")
print(f"Países encontrados: {len(paises)}")

# mostrar todos
for p in paises:
    mostrar(p)


paises = get_region("south america")

def get_poblacion(p):
    return p.get("population", 0)

ordenados = sorted(
    paises,
    key=get_poblacion,
    reverse=True,
)

print("Ranking por población:\n")
for i, p in enumerate(ordenados, 1):
    nombre    = p["name"]["common"]
    poblacion = p.get("population", 0)
    print(f"{i:2}. {nombre:20} {poblacion:>12,}")

def get_poblacion(p):
    return p.get("population", 0)

# 2) sorted la llama por cada elemento
#    internamente hace: get_poblacion(p)
#    para cada p de la lista
sorted(paises, key=get_poblacion, reverse=True)

from requests.exceptions import (
    HTTPError, ConnectionError, Timeout
)

def get_country(name):
    url = f"{BASE}/name/{name}"
    try:
        r = requests.get(url, timeout=5)
        r.raise_for_status()
        return r.json()[0]
    except Timeout:
        print("⏱ La API tardó demasiado")
    except ConnectionError:
        print("📡 Sin conexión a internet")
    except HTTPError as e:
        print(f"❌ Error {e.response.status_code}: no encontrado")
    return None

class Country:

    def __init__(self, data:dict):
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

        print("Nombre\t\tPoblación\tÁrea\t\tDensidad")

        for pais in paises:
            print(f"{pais.nombre}\t\t{pais.poblacion}\t\t{pais.area}\t\t{pais.density():.2f}")

        mayor_poblacion = max(paises, key=lambda x: x.poblacion)
        mayor_area = max(paises, key=lambda x: x.area)
        mayor_densidad = max(paises, key=lambda x: x.density())

        print("\nGANADORES")
        print("Mayor población:", mayor_poblacion.nombre)
        print("Mayor área:", mayor_area.nombre)
        print("Mayor densidad:", mayor_densidad.nombre)


        

    def __str__(self):
        return f"Nombre {self.nombre}\nCapital {self.capital}\nPoblacion {self.poblacion}\nArea {self.area} "

