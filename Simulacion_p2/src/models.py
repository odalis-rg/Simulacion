"""Modelos de crecimiento poblacional (patrón Strategy).

Cada modelo implementa la misma interfaz `simular(params)` y devuelve
(tiempo, poblacion). Así se pueden intercambiar sin tocar el resto del código.
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass

import numpy as np


@dataclass
class Parametros:
    p0: float          # población inicial
    r: float           # tasa de crecimiento
    tiempo: int        # tiempo total (períodos)
    sigma: float = 30  # nivel de aleatoriedad (modelo estocástico)
    dt: float = 0.1    # tamaño del paso (modelo continuo)
    semilla: int | None = None


class ModeloCrecimiento(ABC):
    nombre: str = "Modelo"
    estilo: str = "-"

    @abstractmethod
    def simular(self, p: Parametros) -> tuple[np.ndarray, np.ndarray]:
        """Retorna (tiempo, poblacion)."""


class Deterministico(ModeloCrecimiento):
    nombre = "Determinístico  P0·e^(rt)"
    estilo = "-"

    def simular(self, p):
        t = np.linspace(0, p.tiempo, 200)
        return t, p.p0 * np.exp(p.r * t)


class Discreto(ModeloCrecimiento):
    nombre = "Discreto  Pt+1 = Pt + r·Pt"
    estilo = "o--"

    def simular(self, p):
        poblacion = [p.p0]
        for _ in range(1, p.tiempo + 1):
            actual = poblacion[-1]
            poblacion.append(actual + p.r * actual)
        return np.arange(p.tiempo + 1), np.array(poblacion)


class Estocastico(ModeloCrecimiento):
    nombre = "Estocástico  + ε~N(0,σ²)"
    estilo = "s-"

    def simular(self, p):
        rng = np.random.default_rng(p.semilla)
        poblacion = [p.p0]
        for _ in range(1, p.tiempo + 1):
            actual = poblacion[-1]
            ruido = rng.normal(0, p.sigma)
            nueva = actual + p.r * actual + ruido
            poblacion.append(max(nueva, 0))
        return np.arange(p.tiempo + 1), np.array(poblacion)


class ContinuoEuler(ModeloCrecimiento):
    nombre = "Continuo (Euler)  dP/dt = rP"
    estilo = "-."

    def simular(self, p):
        t = np.arange(0, p.tiempo + p.dt, p.dt)
        poblacion = [p.p0]
        for _ in range(1, len(t)):
            actual = poblacion[-1]
            cambio = p.r * actual
            poblacion.append(actual + p.dt * cambio)
        return t, np.array(poblacion)


class Simulador:
    """Contexto: recibe una lista de estrategias y las ejecuta."""

    def __init__(self, modelos: list[ModeloCrecimiento]):
        self.modelos = modelos

    def ejecutar(self, p: Parametros) -> dict:
        return {m.nombre: (m, *m.simular(p)) for m in self.modelos}
