from interfaces.instruction import Instruction
from environment.types import ExpressionType
from environment.value import Value
from expressions.primitive import Primitive

class Embebida(Instruction):
    def __init__(self, line, col, exp, parseo):
        self.line = line
        self.col = col
        self.exp = exp
        self.parseo = parseo
        

    def ejecutar(self, ast, env,gen):
   
        if self.parseo == "parseInt":
            parseo = float(self.exp.value)
            result = Primitive(self.line, self.col, int(parseo), ExpressionType.INTEGER)
            valor = result.ejecutar(ast, env, gen)
            return valor


        if self.parseo == "parseFloat":
            parseo = float(self.exp.value)
            result = Primitive(self.line, self.col, float(parseo), ExpressionType.FLOAT)
            valor = result.ejecutar(ast, env, gen)
            return valor
        
        if self.parseo == "typeof":
            
            if result.type== ExpressionType.STRING:
                result = Value(line=self.line, col=self.col, result="string", type=ExpressionType.STRING)
            if result.type== ExpressionType.INTEGER:
                result = Value(line=self.line, col=self.col, result="number", type=ExpressionType.STRING)
            if result.type== ExpressionType.FLOAT:
                result = Value(line=self.line, col=self.col, result="float", type=ExpressionType.STRING)
            if result.type== ExpressionType.BOOLEAN:
                result = Value(line=self.line, col=self.col, result="boolean", type=ExpressionType.STRING)
            if result.type== ExpressionType.ARRAY:
                result = Value(line=self.line, col=self.col, result="array", type=ExpressionType.STRING)
            return result