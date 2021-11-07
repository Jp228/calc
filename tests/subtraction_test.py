"""Testing Addition class"""
from calc.operations.subtraction import Subtraction


def test_calculation_subtraction():
    """testing that our calculator has a static method for addition"""
    #Arrange
    subtraction = Subtraction(3,2)
    #Act
    #Assert
    assert subtraction.get_result() == 1
