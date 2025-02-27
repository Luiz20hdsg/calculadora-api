import pytest
from src.main.python.com.example.calculadora.model.numbers import Numbers

def test_sum_numbers():
    numbers = Numbers()
    assert numbers.sum_numbers([1, 2, 3]) == 6
    with pytest.raises(ValueError):
        numbers.sum_numbers([])

def test_average_numbers():
    numbers = Numbers()
    assert numbers.average_numbers([1, 2, 3]) == 2.0
    with pytest.raises(ValueError):
        numbers.average_numbers([])