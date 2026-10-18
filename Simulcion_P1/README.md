# Guía de Actividades Práctico-Experimentales Nro. 001

## 1. Datos Generales

| Campo | Detalle |
|---|---|
| Asignatura | Simulación |
| Ciclo | 5 |
| Unidad | U1: Introducción a la Simulación |
| Práctica Nro. | 01 |
| Título de la Práctica | Construcción y simulación computacional de un modelo matemático |
| Docente | José O. Guamán Q. |
| Fecha | 01 y 02 de octubre de 2026 |

## 2. Objetivos

Comprender el proceso de construcción de un modelo matemático y analizar su comportamiento mediante Python.

1. Identificar variables, parámetros y relaciones matemáticas de un sistema.
2. Implementar un modelo matemático en Python.
3. Analizar gráficamente la influencia de los parámetros.

## 3. Materiales y herramientas

- Python 3, NumPy, Matplotlib
- Terminal en Linux (Arch)

Instalación en Arch:

```
sudo pacman -S python python-numpy python-matplotlib
```

## 4. Estructura

```
simulacion_lluvia/
└── python/
    ├── main.py        punto de entrada
    ├── datos.py       registros horarios
    ├── modelo.py      funciones del modelo y estrategias
    ├── reporte.py     tabla en consola
    └── graficas.py    gráficas (PNG en salida/)
```

## 5. Procedimiento / Metodología

Modelo base: I = 0.5H + 0.3N + 0.2Tf

Modelo ajustado: I = 0.4H + 0.4N + 0.2Tf

- H y N se normalizan dividiendo el porcentaje entre 100.
- Tf = 1 - 0.05(T - 10), limitado entre 0.10 y 1.00. Reproduce la tabla de la guía e interpola valores intermedios (15 °C, 17 °C).
- Estados: I < 0.40 sin lluvia, 0.40 a 0.60 baja posibilidad, 0.60 a 0.75 lluvia probable, I >= 0.75 lluvia.

Patrón de diseño: Strategy. Cada fórmula del índice es una estrategia intercambiable; el resto del programa no cambia al ajustar el modelo.

## 6. Ejecución

```
cd python
python main.py
```

Imprime las tablas en consola y guarda las gráficas en `salida/`.

## 7. Resultados esperados

- Tabla completa de H, N, Tf, índice y estado para ambos modelos.
- Gráficas de variables normalizadas, índice por hora y comparación entre modelos.
- Interpretación: el índice crece por la tarde (14:00 a 18:00) por el aumento de humedad y nubosidad, y supera 0.75 desde las 16:00.
