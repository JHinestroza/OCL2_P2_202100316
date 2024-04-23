from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
from parser.parser import Parser
from environment.ast import Ast
from environment.environment import Environment
from environment.generator import Generator
from environment.execute import RootExecuter
import os


# Se crea una instancia de la aplicación Flask
app = Flask(__name__,template_folder="./Templates")
CORS(app)

# Se define una ruta de Test
@app.route('/')
def saludo():
    return render_template('index.html')

@app.route('/obtener-texto', methods=['POST'])
def obtener_texto():
    # Obtención del código
    data = request.get_json()
    texto = data['EntradaTexto']
    # Creación del entorno global
    env = Environment(None, 'GLOBAL')
    # Creación del AST
    ast = Ast()
    # Creación del generador
    gen = Generator()
    # Creación del parser
    parser = Parser()
    # [inst1, inst2, inst2]
    instructionsArr = parser.interpretar(texto)
    # Ejecución
    RootExecuter(instructionsArr, ast, env, gen)
    # Estructurando respuesta
    # res = {"result": True,"console": gen.get_final_code(),"errors": ast.getErrors()}
    res = {"result": True,"console":gen.get_final_code(),"errors":  ast.getErrors() }
    return jsonify({'mensaje': res})
    
if __name__ == '__main__':
    archivo_a_borrar = "./parser/parsetab.py"

# Intenta borrar el archivo
    try:
        os.remove(archivo_a_borrar)
        print(f"El archivo '{archivo_a_borrar}' ha sido borrado exitosamente.")
    except OSError as e:
        print(f"No se pudo borrar el archivo '{archivo_a_borrar}': {e}")
    app.run(debug=True)
    app.run(debug=True)
    