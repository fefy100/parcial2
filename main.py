from country import CountryAPI

api = CountryAPI()

# Países
#sthefany
spain = api.by_name("spain")
thailand = api.by_name("thailand")
hungary = api.by_name("hungary")
egypt = api.by_name("egypt")
france = api.by_name("france")
argentina = api.by_name("argentina")
norway = api.by_name("norway")
yemen = api.by_name("yemen")
#cesar
colombia = api.by_name("colombia")
estonia = api.by_name("estonia")
sweden = api.by_name("sweden")
australia = api.by_name("australia")
romania = api.by_name("romania")

# Lista de comparación (filtrando None por seguridad)
paises = [
    p for p in [
        thailand, hungary, egypt, france, argentina,
        norway, yemen, colombia, estonia, sweden,
        australia, romania
    ]
    if p is not None
]

# Ejecutar comparación solo si España cargó bien
if spain:
    spain.comparar(paises)
else:
    print("No se pudo cargar España")