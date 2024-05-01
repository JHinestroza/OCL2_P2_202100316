from interfaces.instruction import Instruction
from environment.environment import Environment


class Cases(Instruction):
    def __init__(self, line, col, opcion, block):
        self.line = line
        self.col = col
        self.opcion = opcion
        self.block = block

    def ejecutar(self, ast, env,gen):
        # Variables de iteración
        pass