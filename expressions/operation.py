
from interfaces.expression import Expression
from environment.types import ExpressionType
from environment.symbol import Symbol
from environment.value import Value
from expressions.Errores import Errores,list_erroes

class Operation(Expression):
    def __init__(self, line, col, operador, opL, opR):
        self.line = line
        self.col = col
        self.operador = operador
        self.opL = opL
        self.opR = opR

    def ejecutar(self, ast, env, gen):

        temp = gen.new_temp()

        if self.operador == "+":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)
            
            result = int(op1.valor)+int(op2.valor)

            gen.add_br()

            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')

            # Traducción de suma
            gen.add_operation('add', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [],result)
    
        if self.operador == "-":
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)
            
            print("exd",op1.valor)
            result = int(op1.valor)-int(op2.valor)

            gen.add_br()
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            elif op2 == None:
                gen.add_li('t3', str(0)) 
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            # Traducción de resta
            gen.add_operation('sub', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [],result)
        
        if self.operador == "*":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)
            
            result = int(op1.valor)*int(op2.valor)

            gen.add_br()
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')

            gen.add_operation('mul', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [],result)
        
        if self.operador == "/":
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)
            
            result = int(op1.valor)/int(op2.valor)

            gen.add_br()
            gen.comment('Realizando operacion division')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            gen.add_operation('div', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [],result)
        
        if self.operador == "%":
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)
            result = int(op1.valor)%int(op2.valor)

            gen.add_br()
            gen.comment('Realizando operacion modular')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            # Traducción de división
            gen.add_operation('rem', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [],result)
        
        
        if self.operador == "<":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)
            print(op1.valor)
            print(op2.valor)
            result = int(op1.valor)<int(op2.valor)

            gen.add_br()
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            # Traducción de menor qué
            # Generando etiquetas
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            # Agregando condición
            gen.add_blt('t1', 't2', trueLvl)
            # Agregando salto
            gen.add_jump(falseLvl)
            # Result
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [],result)
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result

        if self.operador == ">":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)
            
            
            print(op1.valor)
            print(op2.valor)
            
            result = int(op1.valor)>int(op2.valor)
            

            gen.add_br()
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            gen.add_bgt('t1', 't2', trueLvl)
            gen.add_jump(falseLvl)
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [],result)
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result
        
        
        if self.operador == ">=":
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)
            
            result = int(op1.valor)>=int(op2.valor)

            gen.add_br()
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            gen.add_bge('t1', 't2', trueLvl)
            gen.add_jump(falseLvl)
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [],result)
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result

        if self.operador == "<=":
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)
            
            result = int(op1.valor) <= int(op2.valor)

            gen.add_br()
            gen.comment('Realizando operacion menor o igual que')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            gen.add_operation('sub','t2','t1','t0')
            gen.add_blez('t2', trueLvl)
            gen.add_jump(falseLvl)
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [],result)
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result
        
        if self.operador == "==":
            # Ejecución de operandos
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)
            result = int(op1.valor) ==  int(op2.valor)

            gen.add_br()
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            gen.add_beq('t1', 't2', trueLvl)
            gen.add_jump(falseLvl)
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [],result)
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result
        
        if self.operador == "!=":
            op1 = self.opL.ejecutar(ast, env, gen)
            op2 = self.opR.ejecutar(ast, env, gen)
            
            result = int(op1.valor)!=int(op2.valor)

            gen.add_br()
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            if 't' in str(op2.value):
                gen.add_move('t3', str(op2.value))
            else:
                gen.add_li('t3', str(op2.value)) 
            gen.add_lw('t2', '0(t3)')
            trueLvl = gen.new_label()
            falseLvl = gen.new_label()
            gen.add_bne('t1', 't2', trueLvl)
            gen.add_jump(falseLvl)
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [],result)
            result.truelvl.append(trueLvl)
            result.falselvl.append(falseLvl)
            return result
    
        if self.operador == "&&":
            gen.add_br()
            op1 = self.opL.ejecutar(ast, env, gen)
            for lvl in op1.truelvl:
                gen.new_body_label(lvl)
            op2 = self.opR.ejecutar(ast, env, gen)
            
            result = int(op1.valor) and int(op2.valor)
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [],result)

            result.truelvl.extend(op2.truelvl)
            result.falselvl.extend(op1.falselvl)
            result.falselvl.extend(op2.falselvl)

            return result
        
        if self.operador == "||":
            gen.add_br()
            op1 = self.opL.ejecutar(ast, env, gen)
            for lvl in op1.falselvl:
                gen.new_body_label(lvl)
            for lvl in op1.truelvl:
                gen.new_body_label(lvl)
            op2 = self.opR.ejecutar(ast, env, gen)
            
            result = (op1.valor) or (op2.valor)
            result = Value("", False, ExpressionType.BOOLEAN, [], [], [],result)

            result.truelvl.extend(op1.truelvl)
            result.truelvl.extend(op2.truelvl)
            result.falselvl.extend(op2.falselvl)

            return result
        
        if self.operador == "!":
            op1 = self.opL.ejecutar(ast, env, gen)
            
            result = not (op1.valor)

            gen.add_br()
            gen.comment('Realizando operacion not')
            if 't' in str(op1.value):
                gen.add_move('t3', str(op1.value))
            elif op1.value == None:
                gen.add_li('t3', str(op1.value))
            else:
                gen.add_li('t3', str(op1.value))
            gen.add_lw('t1', '0(t3)')
            
            gen.add_li('t2', str(-1))
            gen.add_operation('xor', 't0', 't1', 't2')
            gen.add_operation('andi', 't0', 't0', '1')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')
            

    
            return  Value(str(temp), True, ExpressionType.BOOLEAN, [], [], [],result)
        
        err = Errores(self.line, self.col,"Semantico", 'No se puedden operar los valores')
        list_erroes.append(err)
        return None
