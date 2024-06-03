import ast
import operator as op

operators = {
    ast.Add:op.add,
    ast.Sub:op.sub,
    ast.Mult:op.mul,
    ast.Div: op.truediv,
    ast.Pow: op.pow,
    ast.BitXor: op.xor,
    ast.USub: op.neg
    
}
class ExpressionCalculator:
    def __init__(self,expression_string):
        self.expression_string = expression_string
    
    def astEval(self):
        
        def eval_(node):
            if isinstance(node,ast.Constant):
                return node.n
            elif isinstance(node,ast.BinOp):
                return operators[type(node.op)](eval_(node.left),eval_(node.right))
            elif isinstance(node,ast.UnaryOp):
                return operators[type(node.op)](eval_(node.operand))
            else:
                raise TypeError(node)
                
        
        
        return eval_(ast.parse(self.expression_string,mode='eval').body)
        
        
    def calculate(self):
        print(eval(self.expression_string))
        print(self.astEval())
         