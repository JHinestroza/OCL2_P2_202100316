from interfaces.instruction import Instruction
from environment.types import ExpressionType

class Print(Instruction):
    def __init__(self, line, col, Exp):
        self.line = line
        self.col = col
        self.Exp = Exp

    def ejecutar(self, ast, env, gen):
        for exp in self.Exp:
            val = exp.ejecutar(ast, env, gen)
            if (val.type == ExpressionType.INTEGER):
                # Imprimiendo expresion
                gen.add_br()
                if 't' in str(val.value):
                    gen.add_move('t3', str(val.value))
                else:
                    gen.add_li('t3', str(val.value))
                gen.add_lw('a0', '0(t3)')
                gen.add_li('a7', '1')
                gen.add_system_call()
            elif (val.type == ExpressionType.STRING):
                gen.add_br()
                if 't' in str(val.value) and len(str(val.value)) < 2:
                    gen.add_move('a0', str(val.value))
                else:
                    gen.add_la('a0', str(val.value))
                gen.add_li('a7', '4')
                gen.add_system_call()
            elif (val.type == ExpressionType.FLOAT):
                gen.add_br()
                if 't' in str(val.value) and len(str(val.value)) < 2:
                    gen.add_move('a0', str(val.value))
                else:
                    gen.add_la('a0', str(val.value))
                gen.add_li('a7', '4')
                gen.add_system_call()
            elif (val.type == ExpressionType.BOOLEAN):
                print("soy val", val.value)
                if not val.truelvl:
                    gen.add_br()
                    if 't' in str(val.value):
                        gen.add_move('t3', str(val.value))
                    else:
                        gen.add_li('t3', str(val.value))
                    gen.add_lw('a0', '0(t3)')
                    gen.add_li('a7', '1')
                    gen.add_system_call()
                else:
                    salto = gen.new_label_continuar()
                    gen.add_code( f"{val.truelvl[-1]}:\n")
                    gen.print_true()
                    gen.add_jump(salto)
                    gen.add_code( f"{val.falselvl[-1]}:\n")
                    gen.print_false()
                    gen.add_jump(salto)
                    gen.add_code(salto +":")
                    
                
                
        gen.add_br()
        gen.add_li('a0', '10')
        gen.add_li('a7', '11')
        gen.add_system_call()

        return None