from country import CountryAPI

api = CountryAPI()

# Lista de países
nombres = [

    # Stefany
    "spain",
    "thailand",
    "hungary",
    "egypt",
    "france",
    "argentina",
    "norway",
    "yemen",

    # Cesar
    "colombia",
    "estonia",
    "sweden",
    "australia",
    "romania"
]

# Obtener países con concurrencia
paises = api.concurrentes(nombres)

# Comparar países
paises[0].comparar(paises[1:])