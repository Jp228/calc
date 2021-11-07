"""Testing Multiplication class"""
from calc.operations.multiplication import Multiplication


def test_calculator_multiply_static():
    """Tests multiplication"""
    multiplication = Multiplication(1,2)
    assert multiplication.get_result() == 2
