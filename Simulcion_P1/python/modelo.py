def normalizar(porcentaje):
    return porcentaje / 100


def factor_temperatura(temp):
    # Reproduce la tabla de la guía y interpola los valores intermedios
    return min(1.0, max(0.1, 1 - 0.05 * (temp - 10)))


def indice_base(h, n, tf):
    return 0.5 * h + 0.3 * n + 0.2 * tf


def indice_ajustado(h, n, tf):
    return 0.4 * h + 0.4 * n + 0.2 * tf


def clasificar(indice):
    if indice < 0.40:
        return "Sin lluvia"
    if indice < 0.60:
        return "Baja posibilidad"
    if indice < 0.75:
        return "Lluvia probable"
    return "Lluvia"


ESTRATEGIAS = {
    "base": indice_base,
    "ajustado": indice_ajustado,
}


def evaluar(registro, calcular_indice):
    hora, humedad, nubosidad, temp = registro
    h = normalizar(humedad)
    n = normalizar(nubosidad)
    tf = factor_temperatura(temp)
    indice = round(calcular_indice(h, n, tf), 4)
    return {
        "hora": hora, "humedad": humedad, "nubosidad": nubosidad, "temp": temp,
        "h": h, "n": n, "tf": round(tf, 2),
        "indice": indice, "estado": clasificar(indice),
    }


def simular(registros, calcular_indice):
    return [evaluar(r, calcular_indice) for r in registros]
