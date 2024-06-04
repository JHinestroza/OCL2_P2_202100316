from interfaces.expression import Expression
from environment.symbol import Symbol
from environment.types import ExpressionType
from environment.value import Value

class Return(Expression):
    def __init__(self, line, col, exp):
        self.line = line
        self.col = col
        self.exp = exp

    def ejecutar(self, ast, env, gen):
        if env.FunctionValidation():
            if self.exp == None:
                return Value(0, False, ExpressionType.NULL, [], [], [],0)
            sym = self.exp.ejecutar(ast, env,gen)
            return Value(sym.value, True, ExpressionType.RETURN, [], [], [],sym.valor)
        ast.setErrors('La sentencia de transferencia no se encuentra dentro de una función')
        return Value(0, False, ExpressionType.NULL, [], [], [],0)