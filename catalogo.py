
import json

from funciones_base import obtener_posicion
from satelite import Satelite


def cargar_registros(ruta_archivo):

    with open(ruta_archivo, "r") as archivo:
        registros = json.load(archivo)

    return registros


def crear_catalogo(registros):
    

    catalogo = []

    for registro in registros:
        nombre = registro["OBJECT_NAME"]
        numero_catalogo = registro["NORAD_CAT_ID"]

        latitud, longitud, altitud = obtener_posicion(registro)
        
        if altitud < 100:
            continue
        satelite = Satelite(
            nombre,
            numero_catalogo,
            latitud,
            longitud,
            altitud
        )

        catalogo.append(satelite)

    return catalogo


def resumir_por_orbita(catalogo):


    altitudes_por_orbita = {
        "LEO": [],
        "MEO": [],
        "GEO": [],
        "HEO": []
    }

    for satelite in catalogo:
        tipo = satelite.tipo_orbita()
        altitudes_por_orbita[tipo].append(satelite.altitud)

    resumen = {}

    for tipo in altitudes_por_orbita:
        altitudes = altitudes_por_orbita[tipo]

        if len(altitudes) > 0:
            cantidad = len(altitudes)
            minimo = min(altitudes)
            maximo = max(altitudes)
            promedio = sum(altitudes) / cantidad

            resumen[tipo] = {
                "cantidad": cantidad,
                "minimo": minimo,
                "maximo": maximo,
                "promedio": promedio
            }

    return resumen


def satelites_en_zona(catalogo, lon_min, lat_min, lon_max, lat_max):


    resultado = []

    for satelite in catalogo:
        if satelite.esta_en_zona(
            lon_min,
            lat_min,
            lon_max,
            lat_max
        ):
            resultado.append(satelite)

    return resultado
