"""Testing Addition class"""
from calc.operations.addition import Addition

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    addition = Addition(2,5)
    assert addition.get_result() == 7
