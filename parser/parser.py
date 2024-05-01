# PLY Imports
import parser.ply.yacc as yacc
import parser.ply.lex as Lex

# Expressions imports
from environment.types import ExpressionType
from expressions.primitive import Primitive
from expressions.operation import Operation
from expressions.access import Access
from expressions.array import Array
from expressions.array_access import ArrayAccess
from expressions.break_statement import Break
from expressions.continue_statement import Continue
from expressions.ternario import Ternario
from expressions.call import Call
from expressions.return_statement import Return
from expressions.interface_access import InterfaceAccess
from expressions.Embebidas import Embebida
from expressions.Operadores import Operadores
from expressions.Parseo import Parseo

# Instructions imports
from instructions.print import Print
from instructions.declaration import Declaration
from instructions.assignment import Assignment
from instructions.array_declaration import ArrayDeclaration
from instructions.if_instruction import If
from instructions.while_instruction import While
from instructions.function import Function
from instructions.interface import Interface
from instructions.interface_declaration import InterfaceDeclaration
from instructions.Swtich import Switch
from instructions.Cases import Cases
from instructions.For import For

from environment.ast import Ast
from expressions.Errores import Errores, list_erroes


ast = Ast()


class codeParams:
    def __init__(self, line, column):
        self.line = line
        self.column = column

#LEXICO
reserved_words = {
    'console': 'CONSOLE', 
    'log': 'LOG',
    'var': 'VAR',
    'float': 'FLOAT',
    'number': 'NUMBER',
    'string': 'STRING',
    'boolean': 'BOOL',
    'if' : 'IF',
    'while' : 'WHILE',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'return' : 'RETURN',
    'function' : 'FUNC',
    'interface' : 'INTERFACE',
    'else': 'ELSE',
    
    'tolowercase': 'LCASE',
    'touppercase': 'UPCASE',
    'length' : 'LENGHT',
    'push' : 'PUSH',
    'indexof':'INDEXOF',
    'join' : 'JOIN',
    'pop' : 'POP',
    'parseInt': 'PARSEINT',
    'parseFloat': 'PARSEFLOAT',
    'toString': 'TOSTRING',
    'typeof': 'TYPEOF',
    'switch': 'SWITCH',
    'case': 'CASE',
    'default': 'DEFAULT',
    'const': 'CONST',
    'for': 'FOR',
    
}

# Listado de tokens
tokens = [
    'PARIZQ',
    'PARDER',
    'MAS',
    'MENOS',
    'POR',
    'DIVIDIDO',
    'MOD',
    'PUNTO',
    'DOSPUNTOS',
    'COMA',
    'PUNTOCOMA',
    'CADENA',
    'ENTERO',
    'DECIMAL',
    'BOOLEANO',
    'IGUAL',
    'IGUALDAD',
    'DIF',
    'CORIZQ',
    'CORDER',
    'LLAVEIZQ',
    'LLAVEDER',
    'MAYOR',
    'MENOR',
    'MAYORIG',
    'MENORIG',
    'AND',
    'OR',
    'NOT',
    'TERN',
    'ID',
    'true',
    'false',
    
    
] + list(reserved_words.values())

t_MAYOR         = r'>'
t_MENOR         = r'<'
t_MAYORIG       = r'>='
t_MENORIG       = r'<='
t_PARIZQ        = r'\('
t_PARDER        = r'\)'
t_MAS           = r'\+'
t_MENOS         = r'-'
t_POR           = r'\*'
t_DIVIDIDO      = r'/'
t_MOD      =  r'\%'

t_PUNTO         = r'\.'
t_DOSPUNTOS        = r':'
t_COMA          = r','
t_PUNTOCOMA           = r';'
t_IGUALDAD          = r'=='
t_IGUAL            = r'='
t_DIF           = r'!='
t_CORIZQ        = r'\['
t_CORDER        = r'\]'
t_LLAVEIZQ      = r'\{'
t_LLAVEDER      = r'\}'
t_AND           = r'&&'
t_OR            = r'\|\|'
t_NOT           = r'!'
t_TERN          = r'\?'

t_false = r'false'
t_true = r'true'

#Función de reconocimiento
def t_CADENA(t):
    r'"[^"]*"'
    try:
        strValue = str(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, strValue.replace('"', ''), ExpressionType.STRING)
    except ValueError:
        error = Errores(line,column,"Sintactico",f"Error al convertir string %d, {t.value}")
        ast.setErrors(error)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t


def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        floatValue = float(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, floatValue, ExpressionType.FLOAT)
    except ValueError:
        error = Errores(line,column,"Sintactico",f"Error al convertir a decimal %d, {t.value}")
        ast.setErrors(error)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t


def t_BOOLEANO(t):
    r'true | false'
    try:
        boolValue = True 
        if t.value == 'true':
            boolValue = True 
        else:
            boolValue = False
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line    
        t.value = Primitive(line, column, boolValue, ExpressionType.BOOLEAN)
    except ValueError:
        error = Errores(line,column,"Sintactico",f"Error al convertir a booleano %d, {t.value}")
        ast.setErrors(error)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t



def t_ENTERO(t):
    r'\d+'
    try:
        intValue = int(t.value)
        line = t.lexer.lexdata.rfind('\n', 0, t.lexpos) + 1
        column = t.lexpos - line
        t.value = Primitive(line, column, intValue, ExpressionType.INTEGER)
    except ValueError:
        print("Error al convertir a entero %d", t.value)
        t.value = Primitive(0, 0, None, ExpressionType.NULL)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    #  t.type = reserved_words.get(t.value.lower(),'ID')
    t.type = reserved_words.get(t.value,'ID')
    return t

t_ignore = " \t"

t_ignore_COMMENTLINE = r'\/\/.*'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_ignore_COMMENTBLOCK(t):
    r'\/\*[^*]*\*+(?:[^/*][^*]*\*+)*\/'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    params = get_params(t)
    error = Errores(params.line, params.column,"LEXICO", f"no se reconoce el valor {t.value[0]}")
    ast.setErrors(f"LEXICO no se reconoce el valor {t.value[0]}")
    list_erroes.append(error)
    print("Error Léxico '%s'" % t.value[0])
    t.lexer.skip(1)

#SINTACTICO
precedence = (
    ('left', 'MENOR', 'MAYOR'),
    ('left', 'MENORIG', 'MAYORIG'),
    ('left', 'MENORIG', 'MAYORIG','IGUALDAD'),
    ('left', 'MAS', 'MENOS'),
    ('right','UMENOS'),
    ('left', 'POR', 'DIVIDIDO','MOD')
)

#START
def p_start(t):
    '''s : block'''
    t[0] = t[1]

def p_instruction_block(t):
    '''block : block instruccion
            | instruccion '''
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

#Listado de instrucciones
def p_instruction_list(t):
    '''instruccion : print
                | ifinstruction 
                | whileinstruction 
                | declaration
                | arraydeclaration
                | forinstruction
                | assignment
                | breakstmt
                | continuestmt
                | functionstmt
                | call
                | returnstmt
                | interfacecreation
                | switch_statement
                | interdeclaration'''
    t[0] = t[1]

def p_instruction_console(t):
    'print : CONSOLE PUNTO LOG PARIZQ expressionList PARDER PUNTOCOMA'
    params = get_params(t)
    t[0] = Print(params.line, params.column, t[5])

def p_instruction_if_else(t):
    '''ifinstruction : IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER ELSE LLAVEIZQ block LLAVEDER
                     | IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER ELSE ifinstruction
                     | IF PARIZQ expression PARDER LLAVEIZQ block LLAVEDER'''
    params = get_params(t)
    if len(t) == 8:
        t[0] = If(params.line, params.column, t[3], t[6], None)
    elif len(t) == 12:
        t[0] = If(params.line, params.column, t[3], t[6], t[10])
    else:
        t[0] = If(params.line, params.column, t[3], t[6], [t[9]])
        

def p_switch_statement(t):
    '''switch_statement : SWITCH PARIZQ expression PARDER LLAVEIZQ cases_statement default_case LLAVEDER   
                        | SWITCH PARIZQ expression PARDER LLAVEIZQ cases_statement LLAVEDER'''
    print(len(t[6]))
    params = get_params(t)
    if len(t) == 9:
        t[0] = Switch(params.line, params.column,t[3],t[6],t[7])
    else:
        t[0] = Switch(params.line, params.column,t[3],t[6],None)
        
def p_cases_statement(t):
    '''cases_statement : cases_statement case_statement
                       | case_statement'''
    if 2 < len(t):
        t[1].append(t[2])
        t[0] = t[1]
    else:
        t[0] = [t[1]]

def p_case_statement(t):
    'case_statement : CASE expression DOSPUNTOS block '
    params = get_params(t)
    t[0] = Cases(params.line, params.column,t[2],t[4])

def p_default_statement(t):
    'default_case : DEFAULT DOSPUNTOS block'
    params = get_params(t)
    primitivo =  Primitive(params.line, params.column,"default", ExpressionType.STRING)
    t[0] = Cases(params.line, params.column,primitivo,t[3])


def p_instruction_while(t):
    'whileinstruction : WHILE PARIZQ expression PARDER LLAVEIZQ block LLAVEDER'
    params = get_params(t)
    t[0] = While(params.line, params.column, t[3], t[6])
    
def p_instruction_operadores(t):
    '''operadores : ID MAS MAS  '''
    params = get_params(t)
    t[0] = Operadores(params.line, params.column,'+=',t[1], Primitive(params.line, params.column, 1, ExpressionType.INTEGER))
    
def p_instruction_FOR(t):
    '''forinstruction : FOR PARIZQ declaration expression PUNTOCOMA operadores PARDER LLAVEIZQ block LLAVEDER  '''
    params = get_params(t)
    print("ENTRE AL FOR")
    t[0] = For(params.line, params.column, t[3], t[4], t[9],t[6])


def p_instruction_declaration(t):
    'declaration : VAR ID DOSPUNTOS type IGUAL expression PUNTOCOMA'
    params = get_params(t)
    if t[4] == None:
        t[0] = Declaration(params.line, params.column, t[2],  t[6].type , t[6])
        
    else:
        t[0] = Declaration(params.line, params.column, t[2], t[4], t[6])
        
        
def p_instruction_assignment_decla(t):
    'declaration : VAR ID IGUAL expression PUNTOCOMA'
    params = get_params(t)
    print(t[4])
    t[0] = Declaration(params.line, params.column, t[2], t[4].type , t[4])

def p_instruction_declaration2  (t):
    'declaration : CONST ID DOSPUNTOS type IGUAL expression PUNTOCOMA'
    params = get_params(t)
    t[0] = Declaration(params.line, params.column, t[2], t[4], t[6])


def p_instruction_array_declaration(t):
    'arraydeclaration : VAR ID DOSPUNTOS type CORIZQ CORDER IGUAL expression PUNTOCOMA'
    params = get_params(t)
    t[0] = ArrayDeclaration(params.line, params.column, t[2], t[4], t[8])

def p_instruction_interface_declaration(t):
    'interdeclaration : VAR ID DOSPUNTOS ID IGUAL LLAVEIZQ interfaceContent LLAVEDER PUNTOCOMA'
    params = get_params(t)
    t[0] = InterfaceDeclaration(params.line, params.column, t[2], t[4], t[7])

def p_instruction_interface_content(t):
    '''interfaceContent : interfaceContent COMA ID DOSPUNTOS expression
                | ID DOSPUNTOS expression'''
    arr = []
    if len(t) > 5:
        param = {t[3] : t[5]}
        arr = t[1] + [param]
    else:
        param = {t[1] : t[3]}
        arr.append(param)
    t[0] = arr

def p_instruction_assignment(t):
    'assignment : ID IGUAL expression PUNTOCOMA'
    params = get_params(t)
    t[0] = Assignment(params.line, params.column, t[1], t[3])

def p_instruction_return(t):
    '''returnstmt : RETURN expression PUNTOCOMA
                | RETURN PUNTOCOMA'''
    params = get_params(t)
    if len(t) > 3:
        t[0] = Return(params.line, params.column, t[2])
    else:
        t[0] = Return(params.line, params.column, None)

def p_instruction_call_function(t):
    '''call : ID PARIZQ expressionList PARDER PUNTOCOMA
            | ID PARIZQ PARDER PUNTOCOMA'''
    params = get_params(t)
    if len(t) > 5:
        t[0] = Call(params.line, params.column, t[1], t[3])
    else:
        t[0] = Call(params.line, params.column, t[1], [])
    
def p_instruction_function(t):
    'functionstmt : FUNC ID funcparams functype LLAVEIZQ block LLAVEDER'
    params = get_params(t)
    t[0] = Function(params.line, params.column, t[2], t[3], t[4], t[6])

def p_instruction_function_params_list(t):
    '''funcparams : PARIZQ paramsList PARDER
                |  PARIZQ PARDER'''
    if len(t) > 3:
        t[0] = t[2]
    else:
        t[0] = []

def p_instruction_interface_creation(t):
    'interfacecreation : INTERFACE ID LLAVEIZQ attributeList LLAVEDER PUNTOCOMA'
    params = get_params(t)
    t[0] = Interface(params.line, params.column, t[2], t[4])

def p_instruction_interface_attribute(t):
    '''attributeList : attributeList ID DOSPUNTOS type PUNTOCOMA
                | ID DOSPUNTOS type PUNTOCOMA'''
    arr = []
    if len(t) > 5:
        param = {t[2] : t[4]}
        arr = t[1] + [param]
    else:
        param = {t[1] : t[3]}
        arr.append(param)
    t[0] = arr

def p_expression_param_list(t):
    '''paramsList : paramsList COMA ID DOSPUNTOS type
                | ID DOSPUNTOS type'''
    arr = []
    if len(t) > 5:
        param = {t[3] : t[5]}
        arr = t[1] + [param]
    else:
        param = {t[1] : t[3]}
        arr.append(param)
    t[0] = arr

def p_instruction_function_type(t):
    '''functype : DOSPUNTOS type
                | '''
    if len(t) > 2:
        t[0] = t[2]
    else:
        t[0] = ExpressionType.NULL

def p_instruction_break(t):
    'breakstmt : BREAK PUNTOCOMA'
    params = get_params(t)
    t[0] = Break(params.line, params.column)

def p_instruction_continue(t):
    'continuestmt : CONTINUE PUNTOCOMA'
    params = get_params(t)
    t[0] = Continue(params.line, params.column)

def p_type_prod(t):
    '''type : NUMBER
            | FLOAT
            | STRING
            | BOOL'''
    if t[1] == 'number':
        t[0] = ExpressionType.INTEGER
    if t[1] == 'float': 
        t[0] = ExpressionType.FLOAT
    if t[1] == 'string':
        t[0] = ExpressionType.STRING
    if t[1] == 'boolean':
        t[0] = ExpressionType.BOOLEAN
  

def p_expression_list(t):
    '''expressionList : expressionList COMA expression
                    | expression '''
    arr = []
    if len(t) > 2:
        arr = t[1] + [t[3]]
    else:
        arr.append(t[1])
    t[0] = arr

# expressiones aritmeticas, relacionales y lógicas
def p_expression_binaria(t):
    '''expression : expression MAS expression
                  | expression MENOS expression
                  | expression POR expression
                  | expression DIVIDIDO expression
                  | expression MOD expression     '''
    params = get_params(t)
    if t[2] == '+'  : t[0] = Operation(params.line, params.column, "+", t[1], t[3])
    elif t[2] == '-': t[0] = Operation(params.line, params.column, "-", t[1], t[3])
    elif t[2] == '*': t[0] = Operation(params.line, params.column, "*", t[1], t[3])
    elif t[2] == '/': t[0] = Operation(params.line, params.column, "/", t[1], t[3])
    elif t[2] == '%': t[0] = Operation(params.line, params.column, "%", t[1], t[3])
    
def p_expresion_unaria(t):
    'expression : MENOS expression %prec UMENOS'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "-", Primitive(params.line, params.column, 0, t[2].type), t[2])


def p_expression_Relacionales(t):
    '''expression : expression MENOR expression
                  | expression MAYOR expression
                  | expression MENORIG expression
                  | expression MAYORIG expression'''
    params = get_params(t)
    if t[2] == '<'  :  t[0] = Operation(params.line, params.column, "<", t[1], t[3])
    elif t[2] == '>':  t[0] = Operation(params.line, params.column, ">", t[1], t[3])
    elif t[2] == '<=': t[0] = Operation(params.line, params.column, "<=", t[1], t[3])
    elif t[2] == '>=': t[0] = Operation(params.line, params.column, ">=", t[1], t[3])

def p_expression_igual(t):
    'expression : expression IGUALDAD expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "==", t[1], t[3])

def p_expression_diferente(t):
    'expression : expression DIF expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "!=", t[1], t[3])

def p_expression_and(t):
    'expression : expression AND expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "&&", t[1], t[3])

def p_expression_or(t):
    'expression : expression OR expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "||", t[1], t[3])

def p_expression_not(t):
    'expression : NOT expression'
    params = get_params(t)
    t[0] = Operation(params.line, params.column, "!", t[2], None)

def p_expression_agrupacion(t):
    'expression : PARIZQ expression PARDER'
    t[0] = t[2]


def p_instruction_embebidas(t):
    '''expression :    PARSEINT PARIZQ expression PARDER 
                    | PARSEFLOAT PARIZQ expression PARDER '''

    params = get_params(t)
    t[0] = Embebida(params.line, params.column,t[3],t[1])
    
    
def p_instruction_embebidas_string(t):
    '''expression :    expression PUNTO TOSTRING PARIZQ PARDER '''          
    params = get_params(t)
    t[0] = Parseo(params.line, params.column,t[1], t[3])

def p_instruction_embebidas_string2(t):
    '''expression :    ID PUNTO TOSTRING PARIZQ PARDER '''          
    params = get_params(t)
    print("xd?")
    acceso = Access(params.line, params.column, t[1])
    t[0] = Parseo(params.line, params.column,acceso, t[3])
                    

def p_instruction_embebidas_typeof(t):
    '''expression : TYPEOF expression '''          
    params = get_params(t)
    t[0] = Embebida(params.line, params.column, t[2] , t[1])

def p_expression_ternario(t):
    'expression : expression TERN expression DOSPUNTOS expression'
    params = get_params(t)
    t[0] = Ternario(params.line, params.column, t[1], t[3], t[5])

def p_expression_primitiva(t):
    '''expression    : ENTERO
                    | CADENA
                    | DECIMAL
                    | BOOLEANO
                    | listArray'''
    t[0] = t[1]

def p_expression_array_primitiva(t):
    '''expression : CORIZQ expressionList CORDER'''
    params = get_params(t)
    t[0] = Array(params.line, params.column, t[2])

def p_expression_call_function(t):
    '''expression : ID PARIZQ expressionList PARDER
            | ID PARIZQ PARDER'''
    params = get_params(t)
    if len(t) > 4:
        t[0] = Call(params.line, params.column, t[1], t[3])
    else:
        t[0] = Call(params.line, params.column, t[1], [])

def p_expression_list_array(t):
    '''listArray : ID CORIZQ expression CORDER
                | ID'''
    params = get_params(t)
    if len(t) > 3:
        t[0] = ArrayAccess(params.line, params.column, t[1], t[3])
    else:
        t[0] = Access(params.line, params.column, t[1])

def p_error(p):
    if p:
        params = get_params(p)
        error = Errores(params.line, params.column,"LEXICO", f"no se reconoce el valor {p.value[0]}")
        ast.setErrors(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
        list_erroes.append(error)
        print(f"Error de sintaxis en línea {p.lineno}, columna {p.lexpos}: Token inesperado '{p.value}'")
    else:
        print("Error de sintaxis")

def get_params(t):
    line = t.lexer.lineno  # Obtener la línea actual desde el lexer
    lexpos = t.lexpos if isinstance(t.lexpos, int) else 0  # Verificar si lexpos es un entero
    column = lexpos - t.lexer.lexdata.rfind('\n', 0, lexpos) 
    return codeParams(line, column)

class Parser:
    def __init__(self):
        pass

    def interpretar(self, input):
        lexer = Lex.lex()
        parser = yacc.yacc()
        result = parser.parse(input)
        return result