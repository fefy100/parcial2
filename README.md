APIs Parcial 
Integrantes
Stefany González
César

Descripción
Aplicación en Python que consume la API de REST Countries para buscar información de países.

El proyecto utiliza:

Programación Orientada a Objetos (POO)
Consumo de APIs con requests
Manejo de excepciones
Comparación de países por:
población
área
densidad
Archivos del proyecto
country.py

Contiene:
Clase Country
Clase CountryAPI

Funciones principales:

Buscar países por nombre
Buscar países por región
Comparar países
Calcular densidad poblacional
main.py

Archivo principal donde:
se crean los objetos
se consultan países
se muestran comparaciones
Requisitos

Instalar la librería:
pip install requests
O usando el archivo requirements:
pip install -r requirements.txt

Cómo ejecutar
Desde la terminal:

python main.py
Ejemplo de salida
Nombre                    Población              Área      Densidad
----------------------------------------------------------------------
Spain                      49,315,949       505,992.00          97.46
Thailand                   65,859,640       513,120.00         128.35
Hungary                     9,539,502        93,028.00         102.54

GANADORES
Mayor población: Egypt
Mayor área: Australia
Mayor densidad: Thailand
Tecnologías utilizadas
Python
Requests
REST Countries API
API utilizada

REST Countries API