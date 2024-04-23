from environment.types import ExpressionType

def RootExecuter(instructionList, ast, env, gen):
    for inst in instructionList:
        inst.ejecutar(ast, env, gen)

def StatementExecuter(instructionList, ast, env, gen):
    for inst in instructionList:
        res = inst.ejecutar(ast, env, gen)
        if res != None:
            if res.type == ExpressionType.RETURN:
                return res.value
            return res
    return None

def LoopExecuter(instructionList, ast, env):
    for inst in instructionList:
        res = inst.ejecutar(ast, env)
        if res != None:
            if res.type == ExpressionType.BREAK:
                return True
            if res.type == ExpressionType.CONTINUE:
                break
    return False