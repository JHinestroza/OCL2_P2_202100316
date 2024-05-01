from interfaces.expression import Expression
from environment.types import ExpressionType
from environment.symbol import Symbol
from expressions.primitive import Primitive
from expressions.operation import Operation

dominant_table = [
    [ExpressionType.INTEGER, ExpressionType.FLOAT,  ExpressionType.STRING, ExpressionType.NULL,    ExpressionType.NULL],
    [ExpressionType.FLOAT,   ExpressionType.FLOAT,  ExpressionType.STRING, ExpressionType.NULL,    ExpressionType.NULL],
    [ExpressionType.STRING,  ExpressionType.STRING, ExpressionType.STRING, ExpressionType.STRING,  ExpressionType.NULL],
    [ExpressionType.NULL,    ExpressionType.NULL,   ExpressionType.STRING, ExpressionType.BOOLEAN, ExpressionType.NULL],
    [ExpressionType.NULL,    ExpressionType.NULL,   ExpressionType.NULL,   ExpressionType.NULL,    ExpressionType.NULL],
]

class Operadores(Expression):
    def __init__(self, line, col, operador, id, exp):
        self.line = line
        self.col = col
        self.operador = operador
        self.id = id
        self.exp = exp

    def ejecutar(self, ast, env,gen):
        gen.comment('Asignacion de variable')
        sym = env.getVariable(ast, self.id)
        
        op1 = Primitive(self.line, self.col, sym.valor, ExpressionType.INTEGER)
        op2 = Primitive(self.line, self.col, 1, ExpressionType.INTEGER)
        result = Operation(self.line, self.col, "+", op1, op2)
        # Obtener valor
        result = result.ejecutar(ast, env, gen)
        print(result.valor)
        
        # Sustituyendo valor
        if 't' in str(result.value):
            gen.add_move('t0', str(result.value))
        else:
            gen.add_li('t0', str(result.value))
        gen.add_lw('t1', '0(t0)')
        gen.add_li('t3', str(sym.position))
        gen.add_sw('t1', '0(t3)')
        gen.comment('Fin asignacion')
        return None