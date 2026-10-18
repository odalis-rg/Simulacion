#!/usr/bin/env python3
"""Práctica 02 - Simulación: modelos determinístico, discreto, estocástico y continuo."""
import argparse

import matplotlib

from src.datos import DATOS, estimar_r
from src.models import (ContinuoEuler, Deterministico, Discreto, Estocastico,
                        Parametros, Simulador)


def leer_argumentos():
    ap = argparse.ArgumentParser(description="Comparación de modelos de simulación")
    ap.add_argument("--r", type=float, help="tasa de crecimiento (por defecto se estima de los datos)")
    ap.add_argument("--sigma", type=float, default=30, help="nivel de ruido (default 30)")
    ap.add_argument("--dt", type=float, default=0.1, help="paso de Euler (default 0.1)")
    ap.add_argument("--semilla", type=int, help="semilla aleatoria para reproducir resultados")
    ap.add_argument("--guardar", default="comparacion.png", help="archivo PNG de salida")
    ap.add_argument("--no-mostrar", action="store_true", help="no abrir ventana (modo consola/SSH)")
    return ap.parse_args()


def main():
    args = leer_argumentos()
    if args.no_mostrar:
        matplotlib.use("Agg")
    from src.graficas import graficar  # import tras fijar el backend

    r = args.r if args.r is not None else estimar_r(DATOS)
    params = Parametros(p0=DATOS[0], r=r, tiempo=len(DATOS) - 1,
                        sigma=args.sigma, dt=args.dt, semilla=args.semilla)

    print(f"Datos: {DATOS}")
    print(f"P0={params.p0}  r={r:.4f}  sigma={params.sigma}  dt={params.dt}  periodos={params.tiempo}\n")

    simulador = Simulador([Deterministico(), Discreto(), Estocastico(), ContinuoEuler()])
    resultados = simulador.ejecutar(params)

    for nombre, (_, t, pob) in resultados.items():
        print(f"{nombre:<34} P final = {pob[-1]:10.2f}")

    graficar(resultados, DATOS, args.guardar, mostrar=not args.no_mostrar)


if __name__ == "__main__":
    main()
