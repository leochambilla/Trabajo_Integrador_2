
import json

from catalogo import (
    cargar_registros,
    crear_catalogo,
    resumir_por_orbita,
    satelites_en_zona
)
from satelite import Satelite


def test_cargar_registros(tmp_path):
    ruta = tmp_path / "satelites.json"

    registros = [
        {
            "OBJECT_NAME": "ISS",
            "NORAD_CAT_ID": 25544
        }
    ]

    with open(ruta, "w") as archivo:
        json.dump(registros, archivo)

    resultado = cargar_registros(ruta)

    assert len(resultado) == 1
    assert resultado[0]["OBJECT_NAME"] == "ISS"


def test_crear_catalogo(monkeypatch):
    def posicion_falsa(registro):
        return (-34.6, -58.4, 419.7)

    monkeypatch.setattr("catalogo.obtener_posicion", posicion_falsa)

    registros = [
        {
            "OBJECT_NAME": "ISS",
            "NORAD_CAT_ID": 25544
        }
    ]

    resultado = crear_catalogo(registros)

    assert len(resultado) == 1
    assert isinstance(resultado[0], Satelite)
    assert resultado[0].nombre == "ISS"


def test_resumir_por_orbita():
    catalogo = [
        Satelite("ISS", 25544, -34.6, -58.4, 400),
        Satelite("GPS", 12345, 10, 20, 20000)
    ]

    resultado = resumir_por_orbita(catalogo)

    assert resultado["LEO"]["cantidad"] == 1
    assert resultado["LEO"]["minimo"] == 400
    assert resultado["MEO"]["cantidad"] == 1
    assert resultado["MEO"]["promedio"] == 20000


def test_satelites_en_zona():
    dentro = Satelite("ISS", 25544, -40, -70, 419.7)
    fuera = Satelite("GPS", 12345, 10, 20, 20000)

    resultado = satelites_en_zona(
        [dentro, fuera],
        -76.30, -46.13, -66.30, -36.13
    )

    assert len(resultado) == 1
    assert resultado[0].nombre == "ISS"
