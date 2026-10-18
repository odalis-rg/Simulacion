import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SALIDA = "salida"


def _guardar(nombre):
    os.makedirs(SALIDA, exist_ok=True)
    plt.tight_layout()
    plt.savefig(os.path.join(SALIDA, nombre), dpi=150)
    plt.close()


def grafica_variables(nombre, filas):
    horas = [f["hora"] for f in filas]
    plt.figure(figsize=(8, 4))
    plt.plot(horas, [f["h"] for f in filas], marker="o", label="H")
    plt.plot(horas, [f["n"] for f in filas], marker="s", label="N")
    plt.plot(horas, [f["tf"] for f in filas], marker="^", label="Tf")
    plt.title(f"Variables normalizadas ({nombre})")
    plt.xlabel("Hora")
    plt.ylabel("Valor")
    plt.legend()
    plt.grid(alpha=0.3)
    _guardar(f"variables_{nombre}.png")


def grafica_indice(nombre, filas):
    horas = [f["hora"] for f in filas]
    plt.figure(figsize=(8, 4))
    plt.plot(horas, [f["indice"] for f in filas], marker="o", color="tab:blue")
    for umbral, etiqueta in ((0.40, "0.40"), (0.60, "0.60"), (0.75, "0.75")):
        plt.axhline(umbral, linestyle="--", color="gray", linewidth=0.8)
        plt.text(len(horas) - 0.9, umbral + 0.01, etiqueta, fontsize=8)
    plt.title(f"Índice de lluvia ({nombre})")
    plt.xlabel("Hora")
    plt.ylabel("I")
    plt.ylim(0, 1)
    plt.grid(alpha=0.3)
    _guardar(f"indice_{nombre}.png")


def grafica_comparacion(resultados):
    plt.figure(figsize=(8, 4))
    for nombre, filas in resultados.items():
        plt.plot([f["hora"] for f in filas], [f["indice"] for f in filas],
                 marker="o", label=nombre)
    plt.axhline(0.75, linestyle="--", color="gray", linewidth=0.8)
    plt.title("Comparación de modelos")
    plt.xlabel("Hora")
    plt.ylabel("I")
    plt.legend()
    plt.grid(alpha=0.3)
    _guardar("comparacion.png")
