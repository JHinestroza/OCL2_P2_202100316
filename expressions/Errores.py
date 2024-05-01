from interfaces.expression import Expression
from environment.types import ExpressionType

list_erroes = []
class Errores(Expression):
    def __init__(self,line,colum,tipo, error) :
        self.line = line
        self.colum = colum
        self.type = tipo
        self.error = error
        
    def ejecutar(self, ast, env, gen):
        pass