# start of simple calculator app 
import re
from calc_params import CalcParameters
from calc_methods import CalcMethods


while True:
   
    
    try: 
        first_num = input('Input first Number\n')
        first_num = int( first_num)
        
        second_num = input('Enter second Number\n')
        second_num = int(second_num)
        operation = input('input * / + - to  perfume the symbol corresponding math operation\n')
        params_object = CalcParameters(first_number=first_num,second_number=second_num,operation=operation)
        methods_obj = CalcMethods()
        # regex.compile can be used to get better regex strings
        if (not re.match('[\* \/ \- \+]',operation)):
            raise Exception('Please Enter Valid Operation symbol * or - or / or + ')
    except Exception as e :
        print('error: ',e)
        continue
    print(methods_obj.calculate(params_object.first_number,params_object.second_number,params_object.operation) )
    del params_object
    del methods_obj
    
