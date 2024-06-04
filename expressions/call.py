from interfaces.expression import Expression
from environment.symbol import Symbol
from environment.types import ExpressionType
from environment.environment import Environment
from environment.execute import StatementExecuter
from expressions.continue_statement import Continue
from expressions.Errores import Errores,list_erroes
from environment.value import Value

class Call(Expression):
    def __init__(self, line, col, id, params):
        self.line = line
        self.col = col
        self.id = id
        self.params = params

    def ejecutar(self, ast, env, gen):
        # Buscar la función
        func = env.getFunction(ast, self.id)
        if func == {}:
            return
        # Validar cantidad de parámetros
        if len(self.params) != len(func['params']):
            err = Errores(self.line, self.col,"Semantico", f"La función esperaba {len(func['params'])} parámetros, pero se obtuvieron {len(self.params)}")
            list_erroes.append(err)
            ast.setErrors(f"La función esperaba {len(func['params'])} parámetros, pero se obtuvieron {len(self.params)}")
            return Value(0, False, ExpressionType.NULL, [], [], [],0)
        # Crear entorno de funcion
        function_env = Environment(env.getGlobalEnvironment(), 'FUNCTION_'+self.id)
        # Validar parámetros
        if len(self.params) > 0:
            symbolList = []
            # Lista de parámetros
            for i in range(len(self.params)):
                # Obteniendo simbolo del parámetro
                symParam = self.params[i].ejecutar(ast, env,gen)
                symbolList.append(symParam)
                # Guardando valores de funcion
                id_param = list(func['params'][i].keys())[0]
                type_param = list(func['params'][i].values())[0]
                # Validando tipos
                if type_param != symParam.type:
                    ast.setErrors('Los tipos de parámetros son incorrectos')
                    err = Errores(self.line, self.col,"Semantico", 'Los tipos de parámetros son incorrectos')
                    list_erroes.append(err)
                    return Value(0, False, ExpressionType.NULL, [], [], [],0)
                # Agregar parámetros al entorno
                function_env.saveVariable(ast, id_param, symParam)
        # Ejecutar bloque
        returnValue = StatementExecuter(func['block'], ast, function_env,gen)
        print("es el retorno",returnValue)
        if returnValue != None:
            if returnValue != str( func['type']):
                ast.setErrors('El tipo de retorno es incorrecto')
                err = Errores(self.line, self.col,"Semantico", 'El tipo de retorno es incorrecto')
                list_erroes.append(err)
                return Value(0, False, ExpressionType.NULL, [], [], [],0)
            return Value(0, True, ExpressionType.NULL, [], [], [],returnValue)     
        return None
