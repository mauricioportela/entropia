"""Módulo com classe para cálculo de entropia de Shannon."""

from __future__ import annotations

import math
from collections import Counter
from typing import Iterable, Hashable


class Entropia:
    """Calcula a entropia de Shannon para uma sequência de símbolos."""

    def __init__(self, dados: Iterable[Hashable]):
        self._dados = list(dados)
        if not self._dados:
            raise ValueError("A sequência de dados não pode ser vazia.")

    @property
    def frequencias(self) -> dict[Hashable, int]:
        """Retorna a frequência absoluta de cada símbolo."""
        return dict(Counter(self._dados))

    @property
    def probabilidades(self) -> dict[Hashable, float]:
        """Retorna a probabilidade de cada símbolo."""
        total = len(self._dados)
        return {simbolo: freq / total for simbolo, freq in self.frequencias.items()}

    def calcular(self, base: float = 2.0) -> float:
        """Calcula a entropia usando a base logarítmica informada."""
        if base <= 0 or base == 1:
            raise ValueError("A base do logaritmo deve ser positiva e diferente de 1.")

        entropia = 0.0
        for probabilidade in self.probabilidades.values():
            entropia -= probabilidade * (math.log(probabilidade) / math.log(base))

        return entropia
