from interfaces.expression import Expression
from environment.value import Value
from environment.types import ExpressionType

class Access(Expression):
    def __init__(self, line, col, id):
        self.line = line
        self.col = col
        self.id = id

    def ejecutar(self, ast, env, gen):
        # Realizar busqueda en entorno
        sym = env.getVariable(ast, self.id)
        print(sym.valor)
        if(sym.type != ExpressionType.NULL):
            if isinstance(sym,Value):
                position = sym.value
                return Value(position, False, sym.type, [], [], [],sym.valor)      
            else:
                return Value(sym.position, False, sym.type, [], [], [],sym.valor)
 
        return Value('', False, ExpressionType.NULL, [], [], [],"")

