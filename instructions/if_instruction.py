from interfaces.instruction import Instruction
from environment.execute import StatementExecuter
from environment.environment import Environment


class If(Instruction):
    def __init__(self, line, col, exp, block_if, block_else=None):
        self.line = line
        self.col = col
        self.exp = exp
        self.block_if = block_if
        self.block_else = block_else

    def ejecutar(self, ast, env, gen):
        validate = self.exp.ejecutar(ast,env,gen)
        validate = self.Busqueda(gen,validate.value)
        print(validate)
        if validate:
            # Crear entorno del If
            if_env = Environment(env, "IF")
            returnValue = StatementExecuter(self.block_if, ast, if_env,gen)
            if returnValue is not None:
                return returnValue
        elif self.block_else is not None:
            # Crear entorno del Else
            else_env = Environment(env, "ELSE")
            returnValue = StatementExecuter(self.block_else, ast, else_env,gen)
            if returnValue is not None:
                return returnValue
        return None
    
     


    def Busqueda(self, gen,val):
        while True:
            result = gen.get_temp(int(val))
            if result is True or result is False:
                return result
            val = result