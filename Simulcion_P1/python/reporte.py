CABECERA = ("Hora", "Humedad", "Nubosidad", "Temp.", "H", "N", "Tf", "Índice", "Estado")


def fila_a_tupla(f):
    return (f["hora"], f["humedad"], f["nubosidad"], f["temp"],
            f"{f['h']:.2f}", f"{f['n']:.2f}", f"{f['tf']:.2f}",
            f"{f['indice']:.2f}", f["estado"])


def imprimir_tabla(titulo, filas):
    print(f"\n{titulo}")
    formato = "{:<6} {:>8} {:>10} {:>6} {:>5} {:>5} {:>5} {:>7}  {}"
    print(formato.format(*CABECERA))
    print("-" * 72)
    for f in filas:
        print(formato.format(*fila_a_tupla(f)))
