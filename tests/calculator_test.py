"""Testing the Calculator"""
from calc.calculator import Calculator


def test_calculator_add_static():
    """testing that our calculator has a static method for addition"""
    # pylint: disable=unused-argument,redefined-outer-name
    assert Calculator.add_numbers(2,5) == 7


def test_calculator_subtract_static():
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    assert Calculator.subtract_numbers(3,2) == 1

def test_calculator_multiply_static():
    """Testing the subtract method of the calc"""
    # pylint: disable=unused-argument,redefined-outer-name
    #using Tuple instead of args because we can pack as much data as we need into the tuple
    assert Calculator.multiply_numbers(1,2) == 2


def test_calculator_divide_static():
    """Testing """
    assert Calculator.divide_numbers(6,2) == 3

def test_add_calculation_to_history():
    """Testing Calculator history length"""
    assert len(Calculator.history) == 4

def test_calculator_history_get_first_obj():
    """Testing method getting first object from history"""
    assert Calculator.get_first_history_obj() == Calculator.history[0]

def test_calculator_history_get_last_obj():
    """Testing method getting last object from history"""
    assert Calculator.get_last_history_obj() == Calculator.history[Calculator.history_length() - 1]

def test_calculator_history_remove_calculation():
    """Testing method to remove single calculation from history"""
    length = Calculator.history_length()
    Calculator.history_remove_one_item(0)
    assert Calculator.history_length() == length - 1

def test_calculator_clear_history():
    """Testing clear history method"""
    Calculator.clear_history()
    assert Calculator.history_length() == 0
