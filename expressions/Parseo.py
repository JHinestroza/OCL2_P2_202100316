from interfaces.instruction import Instruction
from environment.types import ExpressionType
from environment.symbol import Symbol
from expressions.Errores import Errores,list_erroes
from expressions.primitive import Primitive

class Parseo(Instruction):
    def __init__(self, line, col, Exp, parseo):
        self.line = line
        self.col = col
        self.Exp = Exp
        self.parseo = parseo
        

    def ejecutar(self, ast, env,gen):
        outText = ""
        outText = self.Exp.ejecutar(ast, env,gen).valor
        print(outText)
        
            
        if self.parseo == "toLowerCase" and self.Exp.ejecutar(ast, env).type == ExpressionType.STRING:
            outText = outText.lower()
            #print(outText)
            symbol = Primitive(self.line, self.col, outText.lower(), ExpressionType.STRING)
                # print(symbol.value)
            return symbol

        if self.parseo == "toUpperCase" and self.Exp.ejecutar(ast, env).type == ExpressionType.STRING:
            outText = outText.upper()
            symbol = Primitive(self.line, self.col, outText.upper(), ExpressionType.STRING)
            return symbol
        
        if self.parseo == "toString":
            outText = str(outText)
            symbol = Primitive(self.line, self.col, str(outText), ExpressionType.STRING)
            return symbol
       
        ast.setErrors('Error: El tipo de dato '+ self.Exp.id +' no es String en la fila: '+ str(self.line))
        err = Errores(self.line, self.col,"Semantico",'Error: El tipo de dato '+ self.Exp.id +' no es String en la fila: '+ str(self.line))
        list_erroes.append(err)
        return  Primitive(self.line, self.col, 0, ExpressionType.NULL)