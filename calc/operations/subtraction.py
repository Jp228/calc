"""Subtraction Class"""
from calc.operations.calculation import Calculation


class Subtraction(Calculation): # pylint: disable=too-few-public-methods
    """subtraction calculation object"""
    def get_result(self):
        """get the subtraction results"""
        difference_of_values = self.values[0]
        for value in self.values[1:]:
            difference_of_values =   difference_of_values - value
        return difference_of_values
