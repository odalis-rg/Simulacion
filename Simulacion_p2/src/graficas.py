"""Visualización de resultados."""
import matplotlib.pyplot as plt


def graficar(resultados: dict, datos: list[float], guardar: str | None, mostrar: bool):
    fig, ax = plt.subplots(figsize=(10, 6))
    for nombre, (modelo, t, pob) in resultados.items():
        ax.plot(t, pob, modelo.estilo, label=nombre, markersize=5)
    ax.plot(range(len(datos)), datos, "k*", markersize=11, label="Datos reales")
    ax.set_title("Comparación de modelos de crecimiento poblacional")
    ax.set_xlabel("Tiempo")
    ax.set_ylabel("Población")
    ax.legend()
    ax.grid(True, alpha=0.4)
    fig.tight_layout()
    if guardar:
        fig.savefig(guardar, dpi=150)
        print(f"Gráfica guardada en: {guardar}")
    if mostrar:
        plt.show()
