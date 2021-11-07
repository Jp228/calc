"""Addition Class"""
from calc.operations.calculation import Calculation


class Addition(Calculation): # pylint: disable=too-few-public-methods
    """ calculation addition class"""

    def get_result(self):
        """get the addition results"""
        sum_of_values = self.values[0]
        for val in self.values[1:]:
            sum_of_values = sum_of_values + val
        return sum_of_values
