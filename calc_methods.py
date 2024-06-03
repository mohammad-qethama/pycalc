
from calc_params import CalcParameters
from abc import ABC, abstractmethod

class Calculator(ABC):

    @abstractmethod
    def calculate(self, params: CalcParameters):
        pass

    def print_result(self, result):
        print(result)



class CalcMethods(Calculator):

    def calculate(self, params: CalcParameters):
        if params.operation == '*':
            return self.multiplication(params)

        if params.operation == '/':
            return self.division(params)

        if params.operation == '-':
            return self.difference(params)

        if params.operation == '+':
            return self.sum(params)

    def sum(self, params: CalcParameters):
        return params.first_number + params.second_number

    def difference(self, params: CalcParameters):
        return params.first_number - params.second_number

    def multiplication(self, params: CalcParameters):
        return params.first_number * params.second_number

    def division(self, params: CalcParameters):
        return params.first_number / params.second_number
