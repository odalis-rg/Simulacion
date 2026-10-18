# 📈 Simulación de Crecimiento Poblacional

Práctica 02 – Simulación (UNL · Carrera de Computación).

## 1. Descripción del proyecto

**Propósito:** comparar cuatro paradigmas de simulación aplicados al crecimiento
poblacional: determinístico, discreto, estocástico y continuo (Euler).

**Problema que resuelve:** permite ver cómo cambian los resultados según el tipo de
modelo y cómo la aleatoriedad (σ) y la tasa de crecimiento (r) afectan la población,
usando los datos `[1000, 1100, 1250, 1400, 1600, 1850, 2100]`.

## 2. Tecnologías utilizadas

- Python 3.10+
- NumPy (cálculo y números aleatorios)
- Matplotlib (gráficas)
- Patrón de diseño **Strategy** (un modelo = una estrategia intercambiable)

## 3. Instalación (Arch Linux)

```bash
sudo pacman -S --needed python python-pip tk
cd simulacion
python -m venv .venv
source .venv/bin/activate          # fish: source .venv/bin/activate.fish
pip install -r requirements.txt
```

> Arch no permite `pip install` global (PEP 668), por eso se usa el entorno virtual.

## 4. Uso

```bash
python main.py                              # ejecución con valores por defecto
python main.py --r 0.15 --sigma 80          # cambiar tasa y ruido
python main.py --dt 0.5 --semilla 42        # paso de Euler y semilla fija
python main.py --no-mostrar                 # sin ventana (SSH / sin entorno gráfico)
python main.py --help
```

| Opción | Descripción | Default |
|---|---|---|
| `--r` | Tasa de crecimiento | estimada de los datos |
| `--sigma` | Nivel de aleatoriedad | 30 |
| `--dt` | Tamaño del paso (Euler) | 0.1 |
| `--semilla` | Semilla aleatoria | aleatoria |
| `--guardar` | PNG de salida | `comparacion.png` |
| `--no-mostrar` | No abre ventana | — |

## 5. Estructura del proyecto

```
simulacion/
├── main.py            # punto de entrada (CLI)
├── requirements.txt   # dependencias
└── src/
    ├── models.py      # Strategy: Deterministico, Discreto, Estocastico, ContinuoEuler + Simulador
    ├── datos.py       # datos de entrada y estimación de r
    └── graficas.py    # gráfica comparativa
```

## 6. Información adicional

- **Fórmulas:** `P(t)=P0·e^(rt)` · `Pt+1=Pt+r·Pt` · `Pt+1=Pt+r·Pt+ε, ε~N(0,σ²)` · `Pt+Δt=Pt+Δt·r·Pt`
- **Agregar un modelo nuevo:** crear una clase que herede de `ModeloCrecimiento`,
  implementar `simular()` y añadirla a la lista del `Simulador` en `main.py`.
- **Nota:** si el ruido genera una población negativa, se corrige a 0.
- **Autor / Licencia:** MIT.
