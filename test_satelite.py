
from satelite import Satelite
import pytest

def test_crear_satelite():
    satelite = Satelite("ISS", 25544, -34.6, -58.4, 419.7)

    assert satelite.nombre == "ISS"
    assert satelite.numero_catalogo == 25544
    assert satelite.latitud == -34.6
    assert satelite.longitud == -58.4
    assert satelite.altitud == 419.7


def test_nombre_vacio():
    with pytest.raises(ValueError):
        Satelite("", 25544, -34.6, -58.4, 419.7)


def test_latitud_fuera_de_rango():
    with pytest.raises(ValueError):
        Satelite("ISS", 25544, 95, -58.4, 419.7)


def test_longitud_fuera_de_rango():
    with pytest.raises(ValueError):
        Satelite("ISS", 25544, -34.6, 190, 419.7)


def test_altitud_menor_a_100():
    with pytest.raises(ValueError):
        Satelite("ISS", 25544, -34.6, -58.4, 50)


def test_numero_catalogo_no_entero():
    with pytest.raises(ValueError):
        Satelite("ISS", 25544.5, -34.6, -58.4, 419.7)

def test_tipo_orbita_leo():
    satelite = Satelite("ISS", 25544, -34.6, -58.4, 419.7)

    assert satelite.tipo_orbita() == "LEO"


def test_tipo_orbita_meo():
    satelite = Satelite("GPS", 12345, 10, 20, 20000)

    assert satelite.tipo_orbita() == "MEO"


def test_tipo_orbita_geo():
    satelite = Satelite("GEO SAT", 12346, 10, 20, 36000)

    assert satelite.tipo_orbita() == "GEO"


def test_tipo_orbita_heo():
    satelite = Satelite("HEO SAT", 12347, 10, 20, 40000)

    assert satelite.tipo_orbita() == "HEO"


def test_descripcion():
    satelite = Satelite("ISS", 25544, -34.6, -58.4, 419.7)

    assert satelite.descripcion() == "ISS | 25544 | LEO | 419.7 km"


def test_esta_en_zona():
    satelite = Satelite("ISS", 25544, -40, -70, 419.7)

    assert satelite.esta_en_zona(-76.30, -46.13, -66.30, -36.13)


def test_no_esta_en_zona():
    satelite = Satelite("ISS", 25544, 10, 20, 419.7)

    assert not satelite.esta_en_zona(-76.30, -46.13, -66.30, -36.13)
