"""Datos de entrada y estimación de parámetros."""
import math

DATOS = [1000, 1100, 1250, 1400, 1600, 1850, 2100]


def estimar_r(datos: list[float]) -> float:
    """Tasa continua promedio: r = ln(Pn / P0) / n."""
    n = len(datos) - 1
    return math.log(datos[-1] / datos[0]) / n
