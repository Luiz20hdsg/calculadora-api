class Number:
    def sum(self, a: int, b: int) -> int:
        return a + b

    def divide(self, a: int, b: int) -> float:
        if b == 0:
            raise ValueError("Divisão por zero não permitida")
        return float(a) / b