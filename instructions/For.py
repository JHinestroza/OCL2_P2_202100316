from interfaces.instruction import Instruction
from environment.environment import Environment
from expressions.access import Access
from environment.execute import StatementExecuter

class For(Instruction):
    def __init__(self, line, col, Ran1,Ran2,block,suma):
        self.line = line
        self.col = col
        self.Ran1 = Ran1
        self.Ran2 = Ran2
        self.block = block
        self.suma = suma    
        
        
    def ejecutar(self, ast, env,gen):
        self.Ran1.ejecutar(ast, env,gen)
        gen.comment('Generando un ciclo for')
        # Agregando etiqueta de retorno
        newLabel = gen.new_label()
        gen.new_body_label(newLabel)
        # Se imprime el "if" en el código de la expresion
        condition = self.Ran2.ejecutar(ast, env, gen)
        # Se agregan las etiquetas verdaderas
        for lvl in condition.truelvl:
            gen.new_body_label(lvl)
        # Instrucciones While
        FOR_env = Environment(env, "FOR")
        StatementExecuter(self.block, ast, FOR_env, gen)

        self.suma.ejecutar(ast,env,gen)


        
        gen.add_jump(newLabel)
        # Se agregan las etiquetas falsas
        for lvl in condition.falselvl:
            gen.new_body_label(lvl)
            print("FOR",lvl)
        return None