# TP2 - Siguiendo satélites

**Integrante:** Leo Chambilla

## Descripción del proyecto

Este trabajo va consisitir en desarrollar un programa en Python que permite consultar información sobre satélites a partir de un archivo JSON,
el programa obtiene la posición de los satélites utilizando la biblioteca Skyfield y permite realizar diferentes consultas desde la terminal.

Las consultas disponibles son:

- **Resumen:** muestra la cantidad de satélites por tipo de órbita y las altitudes mínima, máxima y promedio.
- **Zona:** permite buscar los satélites que se encuentran dentro de una zona geográfica determinada.

## Estructura del proyecto

```text
Tp_integrador2/
│
├── datos/
│   └── satelites.json
│
├── catalogo.py
├── consultar_satelites.py
├── funciones_base.py
├── satelite.py
│
├── test_catalogo.py
├── test_satelite.py
│
├── requirements.txt
├── README.md
└── .gitignore
```

## Requisitos

Para utilizar el proyecto  se necesita tener instalado Python y Las bibliotecas utilizadas se encuentran en el archivo `requirements.txt`:

- Skyfield
- Pytest
- Pytest-cov

## Instalación

### 1. Descargar el proyecto

Descargar o clonar el repositorio y abrir la carpeta del proyecto en Visual Studio Code.

### 2. Crear un entorno virtual

Desde la terminal, ejecutar:

```powershell
python -m venv .venv
```

### 3. Activar el entorno virtual

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Instalar las dependencias

Con el entorno virtual activado, ejecutar:

```powershell
pip install -r requirements.txt
```

## Ejecución del programa

Los comandos deben ejecutarse desde la carpeta principal del proyecto.

### Consulta de resumen

Para mostrar las estadísticas de los satélites según su tipo de órbita:

```powershell
python consultar_satelites.py datos/satelites.json resumen
```

El programa muestra:

- Tipo de órbita.
- Cantidad de satélites.
- Altitud mínima.
- Altitud máxima.
- Altitud promedio.

### Consulta por zona geográfica

Para buscar satélites dentro de una zona se deben indicar cuatro coordenadas:

```powershell
python consultar_satelites.py datos/satelites.json zona lon_min lat_min lon_max lat_max
```

Por ejemplo, para consultar una zona de Bariloche:

```powershell
python consultar_satelites.py datos/satelites.json zona -76.30 -46.13 -66.30 -36.13
```

El programa muestra la cantidad de satélites encontrados y la descripción de cada uno.

## Ejecución de los tests

El proyecto cuenta con pruebas automáticas para verificar el funcionamiento de la clase `Satelite` y las funciones del catálogo.
Para ejecutar todos los tests:

```powershell
python -m pytest -v
```

Para ejecutar los tests y medir la cobertura del código:

```powershell
python -m pytest --cov=satelite --cov=catalogo --cov-report=term-missing
```

## Archivos principales del trabajo 

- `satelite.py`: contiene la clase `Satelite`, sus validaciones y sus métodos.
- `catalogo.py`: permite cargar los registros, crear el catálogo, calcular estadísticas y filtrar satélites por zona.
- `consultar_satelites.py`: es el programa principal que recibe los argumentos de la terminal y ejecuta las consultas.
- `funciones_base.py`: contiene la función provista para calcular la posición de los satélites utilizando Skyfield.
- `test_satelite.py`: contiene las pruebas de la clase `Satelite`.
- `test_catalogo.py`: contiene las pruebas de las funciones del catálogo.
