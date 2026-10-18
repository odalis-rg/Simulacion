from datos import REGISTROS
from modelo import ESTRATEGIAS, simular
from reporte import imprimir_tabla
import graficas


def main():
    resultados = {}
    for nombre, estrategia in ESTRATEGIAS.items():
        filas = simular(REGISTROS, estrategia)
        resultados[nombre] = filas
        imprimir_tabla(f"Modelo {nombre}", filas)
        graficas.grafica_variables(nombre, filas)
        graficas.grafica_indice(nombre, filas)
    graficas.grafica_comparacion(resultados)
    print("\nGráficas guardadas en la carpeta salida/")


if __name__ == "__main__":
    main()
