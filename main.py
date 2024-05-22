# start of simple calculator app 
import re 
while True:
    x = input('Input first Number\n')
    y = input('Enter second Number\n')
    operation = input('input * / + - to  perfume the symbol corresponding math operation\n')
    try: 
        x = int(x)
        y = int(y)
        # regex.compile can be used to get better regex strings
        if (not re.match('[\* \/ \- \+]',operation)):
            raise Exception('Please Enter Valid Operation symbol * or - or / or + ')
    except Exception as e :
        print('error: ',e)
        continue
    
    if (operation == '*'):
        print( x * y)
        continue
    if (operation == '/'):
        print( x * y)
        continue
    if (operation == '-'):
        print( x * y)
        continue
    if (operation == '+'):
        print( x * y)
        continue