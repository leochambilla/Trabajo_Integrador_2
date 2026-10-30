class Satelite:
    """Representa un satélite con su posición en un instante dado."""

    def __init__(self, nombre, numero_catalogo, latitud, longitud, altitud):
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío")
        if not isinstance(numero_catalogo, int) or isinstance(numero_catalogo, bool):
            raise ValueError("El número de catálogo debe ser un entero")
        if not -90 <= latitud <= 90:
            raise ValueError("La latitud debe estar entre -90 y 90")
        if not -180 <= longitud <= 180:
            raise ValueError("La longitud debe estar entre -180 y 180")
        if altitud < 100:
            raise ValueError("La altitud debe ser de al menos 100 km")

        self.nombre = nombre
        self.numero_catalogo = numero_catalogo
        self.latitud = latitud
        self.longitud = longitud
        self.altitud = altitud

    def tipo_orbita(self):
        if self.altitud < 2000:
            return "LEO"
        if self.altitud < 34000:
            return "MEO"
        if self.altitud <= 37000:
            return "GEO"
        return "HEO"

    def descripcion(self):
        return (f"{self.nombre} | {self.numero_catalogo} | "
                f"{self.tipo_orbita()} | {self.altitud:.1f} km")

    def esta_en_zona(self, lon_min, lat_min, lon_max, lat_max):
        return (lon_min <= self.longitud <= lon_max
                and lat_min <= self.latitud <= lat_max)