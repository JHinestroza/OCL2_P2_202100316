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
            print(parseo)
            result = Primitive(self.line, self.col, int(parseo), ExpressionType.INTEGER)
            result = result.ejecutar(ast,env,gen)
            return result


        if self.parseo == "parseFloat":
            parseo = float(self.exp.value)
            result = Primitive(self.line, self.col, float(parseo), ExpressionType.FLOAT)
            valor = result.ejecutar(ast, env, gen)
            return valor
        
        if self.parseo == "typeof":
            result = self.exp.ejecutar(ast,env,gen)
            temp = gen.new_temp()
            if result.type== ExpressionType.STRING:
                valor = Primitive(self.line, self.col, "string", ExpressionType.STRING)
                result = valor.ejecutar(ast,env,gen)
                return  result
            if result.type== ExpressionType.INTEGER:
                valor = Primitive(self.line, self.col, "integer", ExpressionType.STRING)
                result = valor.ejecutar(ast,env,gen)
                return  result
            if result.type== ExpressionType.FLOAT:
                valor = Primitive(self.line, self.col, "float", ExpressionType.STRING)
                result = valor.ejecutar(ast,env,gen)
                return  result
            if result.type== ExpressionType.BOOLEAN:
                valor = Primitive(self.line, self.col, "boolean",ExpressionType.STRING)
                result = valor.ejecutar(ast,env,gen)
                return  result
            if result.type== ExpressionType.ARRAY:
                valor = Primitive(self.line, self.col, "array", ExpressionType.STRING)
                result = valor.ejecutar(ast,env,gen)
                return  result
            return result