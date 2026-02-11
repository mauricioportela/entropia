"""Demonstração de uso da classe Entropia."""

from entropia import Entropia


if __name__ == "__main__":
    amostra = ["A", "B", "A", "C", "A", "B", "D", "A"]

    calculadora = Entropia(amostra)

    print("1) Amostra:", amostra)
    print("Frequências:", calculadora.frequencias)
    print("Probabilidades:", calculadora.probabilidades)
    print("Entropia (base 2):", round(calculadora.calcular(base=2), 4), "bits")
