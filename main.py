# start of simple calculator app 
import re
from typing import List

from calc_params import CalcParameters
from calc_methods import CalcMethods, Calculator
from expression_calc import ExpressionCalculator

while True:
    try:
        calculators: List[Calculator] = [CalcMethods(), ExpressionCalculator("5+5")]
        for calculator in calculators:
            calculator.print_result("result")

        params = CalcParameters
        first_num = input('Input first Number\n')
        params.first_number = int(first_num)

        second_num = input('Enter second Number\n')
        params.second_number = int(second_num)
        params.operation = input('input * / + - to  perfume the symbol corresponding math operation\n')

        methods_obj = CalcMethods()
        # regex.compile can be used to get better regex strings
        if (not re.match('[\* \/ \- \+]', params.operation)):
            raise Exception('Please Enter Valid Operation symbol * or - or / or + ')

    except Exception as e:
        print('error: ', e)
        continue
    try:
        print(methods_obj.calculate(params))
    except ZeroDivisionError:
        print('Math Error:Cant divide by 0 ')
    except:
        print('Error', e)

    del params
    del methods_obj
