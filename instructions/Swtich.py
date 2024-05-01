
from interfaces.instruction import Instruction
from environment.environment import Environment
from environment.execute import StatementExecuter

class Switch(Instruction):
    def __init__(self, line, col, opcion, cases,default):
        self.line = line
        self.col = col
        self.opcion = opcion
        self.cases = cases
        self.default = default

    def ejecutar(self, ast, env,gen):
        # Variables de iteración
        bandera = True
        bloque = None
        returnValue = None
        opcion_valida = self.opcion.ejecutar(ast, env,gen)
        
        for opcion in self.cases:
            if opcion_valida.valor == opcion.opcion.value:
                bloque = opcion.block
                bandera = False

          
        if bandera and self.default is not None:
            bloque = self.default.block
        
        if_env = Environment(env, "SWITCH")
        if bloque != None:
            returnValue = StatementExecuter(bloque, ast, if_env,gen)
        if returnValue is not None:
                return returnValue
        
        return None
