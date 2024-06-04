from interfaces.expression import Expression
from environment.types import ExpressionType
from environment.value import Value

class Primitive(Expression):
    def __init__(self, line, col, value, type):
        self.line = line
        self.col = col
        self.value = value
        self.type = type

    def ejecutar(self, ast, env, gen):
        temp = gen.new_temp()
        if(self.type == ExpressionType.INTEGER):
            gen.add_br()
            gen.add_li('t0', str(self.value))
            gen.add_li('t3', str(temp))
            gen.add_sw('t0', '0(t3)')
            print("guardando")
            return  Value(str(temp), True, self.type, [], [], [], self.value)
        elif (self.type == ExpressionType.STRING):
            nameId = 'str_'+str(temp)
            gen.variable_data(nameId, 'string', '\"'+str(self.value)+'\"')
            return  Value(nameId, False, self.type, [], [], [],self.value)
        
        elif (self.type == ExpressionType.FLOAT):
            nameId = 'float_'+str(temp)
            gen.variable_data(nameId, 'float', str(self.value))
            return  Value(nameId, False, self.type, [], [], [],self.value)
        elif (self.type == ExpressionType.BOOLEAN):
            gen.add_br()
            gen.comment('Agregando un primitivo booleano')
            if self.value == True:
                gen.add_li('t0', str(1))
                gen.add_li('t3', str(temp))
                gen.add_sw('t0', '0(t3)')
            
            if self.value == False:
                gen.add_li('t0', str(0))
                gen.add_li('t3', str(temp))
                gen.add_sw('t0', '0(t3)')
            
            return  Value(str(temp), True, self.type, [], [], [],self.value)