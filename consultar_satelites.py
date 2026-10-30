
import sys
import json

from catalogo import (
    cargar_registros,
    crear_catalogo,
    resumir_por_orbita,
    satelites_en_zona
)


def mostrar_resumen(catalogo):
    """Muestra un resumen de los satélites por tipo de órbita."""

    resumen = resumir_por_orbita(catalogo)

    for tipo in resumen:
        datos = resumen[tipo]

        print(f"Tipo de órbita: {tipo}")
        print(f"Cantidad: {datos['cantidad']}")
        print(f"Altitud mínima: {datos['minimo']:.2f} km")
        print(f"Altitud máxima: {datos['maximo']:.2f} km")
        print(f"Altitud promedio: {datos['promedio']:.2f} km")
        print()


def mostrar_zona(catalogo, lon_min, lat_min, lon_max, lat_max):
    """Muestra los satélites que están dentro de una zona."""

    resultado = satelites_en_zona(
        catalogo,
        lon_min,
        lat_min,
        lon_max,
        lat_max
    )

    print(f"Satélites encontrados: {len(resultado)}")

    for satelite in resultado:
        print(satelite.descripcion())


def main():
    """Procesa los argumentos y ejecuta la consulta solicitada."""

    if len(sys.argv) < 3:
        print("Uso: python consultar_satelites.py archivo.json resumen")
        print("O: python consultar_satelites.py archivo.json zona lon_min lat_min lon_max lat_max")
        return

    ruta_archivo = sys.argv[1]
    consulta = sys.argv[2]

    try:
        registros = cargar_registros(ruta_archivo)
        catalogo = crear_catalogo(registros)

        if consulta == "resumen":
            mostrar_resumen(catalogo)

        elif consulta == "zona":
            if len(sys.argv) != 7:
                print("La consulta zona requiere cuatro coordenadas.")
                return

            lon_min = float(sys.argv[3])
            lat_min = float(sys.argv[4])
            lon_max = float(sys.argv[5])
            lat_max = float(sys.argv[6])

            if lon_min > lon_max or lat_min > lat_max:
                print("Error: los límites mínimos no pueden superar los máximos.")
                return

            mostrar_zona(
                catalogo,
                lon_min,
                lat_min,
                lon_max,
                lat_max
            )

        else:
            print("Consulta no válida. Usá resumen o zona.")

    except FileNotFoundError:
        print("Error: no se encontró el archivo JSON.")

    except json.JSONDecodeError:
        print("Error: el archivo no contiene un JSON válido.")

    except ValueError as error:
        print(f"Error en los datos o argumentos: {error}")


if __name__ == "__main__":
    main()
