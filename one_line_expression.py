import re
from expression_calc import ExpressionCalculator

try:
    expression = input('Enter your expression\n')
    expression = expression.replace(" ","")
    pattern = r'^[0-9+\-*/]+$'
    if (not re.fullmatch(pattern,expression)):
        raise Exception('invalid expression please enter only numbers and mathematical operations')

    calculation_obj = ExpressionCalculator(expression)
    calculation_obj.calculate()

except Exception as e:
    print('error: ',e)