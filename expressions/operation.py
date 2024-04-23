from interfaces.expression import Expression
from environment.types import ExpressionType
from environment.symbol import Symbol
from environment.value import Value

contador = 0

class Operation(Expression):
    
    def __init__(self, line, col, operador, opL, opR):
        self.line = line
        self.col = col
        self.operador = operador
        self.opL = opL
        self.opR = opR

    def ejecutar(self, ast, env, gen):
        global contador
        # Ejecución de operandos
        op1 = self.opL.ejecutar(ast, env, gen)
        op2 = self.opR.ejecutar(ast, env, gen)

        gen.add_br()
        gen.comment('Realizando operacion')
        if 't' in str(op1.value):
            gen.add_move('t3', str(op1.value))
        else:
            gen.add_li('t3', str(op1.value))
        #gen.add_li('t3', str(op1.value))
        gen.add_lw('t1', '0(t3)')
        if 't' in str(op2.value):
            gen.add_move('t3', str(op2.value))
        else:
            gen.add_li('t3', str(op2.value)) 
        #gen.add_li('t3', str(op2.value))
        gen.add_lw('t2', '0(t3)')
        

        if self.operador == "+":
            result = gen.get_temp(int(op1.value)) +  gen.get_temp(int(op2.value))
            temp = gen.new_temp(result)
            gen.add_operation('add', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')
            
            
            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
    
        if self.operador == "-":
            result = gen.get_temp(int(op1.value)) -  gen.get_temp(int(op2.value))
            temp = gen.new_temp(result)
            gen.add_operation('sub', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
        
        if self.operador == "*":
            result = gen.get_temp(int(op1.value)) *  gen.get_temp(int(op2.value))
            temp = gen.new_temp(result)
            gen.add_operation('mul', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
        
        if self.operador == "/":
            result = gen.get_temp(int(op1.value)) /  gen.get_temp(int(op2.value))
            temp = gen.new_temp(result)
            gen.add_operation('div', 't0', 't1', 't2')
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')

            return  Value(str(temp), True, ExpressionType.INTEGER, [], [], [])
        
        if self.operador == "<":
            gen.comment('Realizando operacion menor que que')
            gen.variable_data("true_msg", 'string', '\"true\"')
            gen.variable_data("false_msg", 'string', '\"false\"')
            result = gen.get_temp(int(op1.value)) <  gen.get_temp(int(op2.value))
            contador +=1
        
            return  Value(str(temp), True, ExpressionType.BOOLEAN, [], [], [])
        
        if self.operador == ">":
            
            gen.comment('Realizando operacion mayor que')
            gen.variable_data("true_msg", 'string', '\"true\"')
            gen.variable_data("false_msg", 'string', '\"false\"')
            result = gen.get_temp(int(op1.value)) >  gen.get_temp(int(op2.value))
            temp = gen.new_temp(result)
            contador +=1
        
            return  Value(str(temp), True, ExpressionType.BOOLEAN, [], [], [])
        
        if self.operador == "==":
            gen.comment('Realizando operacion igual')
            gen.variable_data("true_msg", 'string', '\"true\"')
            gen.variable_data("false_msg", 'string', '\"false\"')
            result = gen.get_temp(int(op1.value)) ==  gen.get_temp(int(op2.value))
            temp = gen.new_temp(result)
            contador +=1
        
            return  Value(str(temp), True, ExpressionType.BOOLEAN, [], [], [])
        
        if self.operador == "!=":
            gen.comment('Realizando operacion diferente')
            gen.variable_data("true_msg", 'string', '\"true\"')
            gen.variable_data("false_msg", 'string', '\"false\"')
            result = gen.get_temp(int(op1.value)) !=  gen.get_temp(int(op2.value))
            temp = gen.new_temp(result)
            contador +=1
        
            return  Value(str(temp), True, ExpressionType.BOOLEAN, [], [], [])

        if self.operador == "||":
            gen.comment('Realizando operacion mayor que')
            gen.variable_data("true_msg", 'string', '\"true\"')
            gen.variable_data("false_msg", 'string', '\"false\"')
            result,result2 = self.Busqueda(gen, op1.value, op2.value)
            op = result or result2
            temp = gen.new_temp(op)
            contador +=1

            return  Value(str(temp), True, ExpressionType.BOOLEAN, [], [], [])
        
        if self.operador == "&&":
            gen.comment('Realizando operacion mayor que')
            gen.variable_data("true_msg", 'string', '\"true\"')
            gen.variable_data("false_msg", 'string', '\"false\"')
            result,result2 = self.Busqueda(gen, op1.value, op2.value)
            op = result and result2
            temp = gen.new_temp(op)
            contador +=1

            return  Value(str(temp), True, ExpressionType.BOOLEAN, [], [], [])
        
        return None

    def Busqueda(self, gen,val, val2):
            result = val
            result2 = val2
            while True:
                if result != True or result != False:
                    result = gen.get_temp(int(val))
                if result2 != True or result2 != False:
                    result2 = gen.get_temp(int(val2))
                if result is True or result is False and result2 is True or result2 is False:
                    return result, result2    
                val = result
                val2 = result2