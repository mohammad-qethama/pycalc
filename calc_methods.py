class CalcMethods:

    def calculate(self,first_num,second_num,operation):
        if (operation == '*'):
            return self.multiplication(first_num,second_num)
        
        if (operation == '/'):
            return self.division(first_num,second_num)
        
        if (operation == '-'):
            return self.difference(first_num,second_num)
        
        if (operation == '+'):
            return self.sum(first_num,second_num)
        
    def sum(self,first_num,second_num):
        return first_num+second_num
    def difference(self,first_num,second_num):
        return first_num-second_num
    def multiplication(self,first_num,second_num):
        return first_num*second_num
    def division(self,first_num,second_num):
        return first_num/second_num