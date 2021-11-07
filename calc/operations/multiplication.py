"""Multiplication Class"""
from calc.operations.calculation import Calculation

class Multiplication(Calculation): # pylint: disable=too-few-public-methods
    """subtraction calculation object"""
    def get_result(self):
        """get the multiplication results"""
        result = self.values[0]
        for value in self.values[1:]:
            result = result * value
        return result
