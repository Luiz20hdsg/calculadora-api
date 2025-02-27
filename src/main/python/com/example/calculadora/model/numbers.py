from .number import Number

class Numbers:
    def __init__(self):
        self.number = Number()

    def sum_numbers(self, vec: list) -> int:
        if not vec or not all(isinstance(x, int) for x in vec):
            raise ValueError("Vetor vazio ou contém valores inválidos")
        return sum(vec)  # Usa a soma nativa do Python, mas poderia chamar self.number.sum

    def average_numbers(self, vec: list) -> float:
        if not vec or not all(isinstance(x, int) for x in vec):
            raise ValueError("Vetor vazio ou contém valores inválidos")
        return self.number.divide(self.sum_numbers(vec), len(vec))