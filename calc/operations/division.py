"""Division Class"""
from calc.operations.calculation import Calculation


class Division(Calculation): # pylint: disable=too-few-public-methods
    """Division class"""

    def get_result(self):
        """Returns division result of two numbers"""
        result = self.values[0]
        for value in self.values[1:]:
            result = result / value
        return result
