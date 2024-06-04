from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
from parser.parser import Parser

from environment.environment import Environment
from environment.generator import Generator
from environment.execute import RootExecuter
import os

from parser.parser import ast
import graphviz
from expressions.Errores import list_erroes

from parser.parser import simbolos


env = Environment(None, 'GLOBAL')
# Se crea una instancia de la aplicación Flask
app = Flask(__name__,template_folder="./Templates")
CORS(app)

# Se define una ruta de Test
@app.route('/')
def saludo():
    return render_template('index.html')

@app.route('/obtener-texto', methods=['POST'])
def obtener_texto():
    global ast
    # Obtención del código
    data = request.get_json()
    texto = data['EntradaTexto']
    # Creación del entorno global
    
    # Creación del AST
    
    # Creación del generador
    gen = Generator()
    # Creación del parser
    parser = Parser()
    # [inst1, inst2, inst2]
    instructionsArr = parser.interpretar(texto)
    # Ejecución
    RootExecuter(instructionsArr, ast, env, gen)
    print(ast.getErrors())
    # res = {"result": True,"console": gen.get_final_code(),"errors": ast.getErrors()}
    res = {"result": True,"console":gen.get_final_code(),"errors":  ast.getErrors() }
    
    try:
        tabla = generar_grafo_tabla()
        print(tabla)
    except:
        pass
    generar_grafo_tablaErrores()
    list_erroes.clear()
    ast.ClearErrors()
    simbolos.clear()
    return jsonify({'mensaje': res})


def generar_tabla_html_Errores():
    global simbolos
    # Encabezado de la tabla
    tabla_html = "<table border='1' cellspacing='0'>\n"
    tabla_html += "<tr>   <td>Tipo</td>  <td>Descripcion</td> <td>Ammbito</td>  <td>Línea</td>  <td>Columna</td>  </tr>\n"
    contador = 0
    valor = None
    # Iterar sobre las filas y columnas para generar las celdas de la tabla
    for error in list_erroes:
        tabla_html += "<tr>\n"
        tabla_html += f"<td> {error.type} </td>   <td> {error.error} </td>  <td> GLOBAL</td>   <td> {error.line}</td> <td> {error.colum}</td>\n"
        tabla_html += "</tr>\n"

    # Cierre de la tabla
    tabla_html += "</table>"
    
    return tabla_html

def generar_grafo_tablaErrores():
    tabla_html = generar_tabla_html_Errores()
    grafo = "digraph G {\n"
    grafo += "node [shape=plaintext]\n"
    grafo += "nodo [label=<{}>]\n".format(tabla_html)
    grafo += "}"
    with open("grafo.dot", "w") as dot_file:
        dot_file.write(grafo)

    # Generar la imagen a partir del archivo DOT
    graph = graphviz.Source(grafo)
    graph.render("tablaErrores", format="png",  directory= "./static/Reportes",cleanup=True)
    print("Imagen generada con éxito.")
    
    
    
    
def generar_tabla_html_graphviz():
    global simbolos
    # Encabezado de la tabla
    tabla_html = "<table border='1' cellspacing='0'>\n"
    tabla_html += "<tr><td>ID</td><td>Tipo de símbolo</td><td>Tipo de dato</td><td>Línea</td><td>Columna</td></tr>\n"
    contador = 0
    valor = None
    # Iterar sobre las filas y columnas para generar las celdas de la tabla
    for dato in simbolos:
        tabla_html += "<tr>\n"
        try:
            valor = env.getVariable(ast, dato)
            cadena = str(valor.type)
            cadena = cadena.replace("ExpressionType.", "")
            tabla_html += f"<td> {dato} </td> <td> Variable  </td>  <td> {cadena} </td>  <td> {valor.line}</td> <td> {valor.col}</td>\n"  
        except:
            pass
               

        try:
            valor = env.getVariable(ast, dato)
            valor = env.getFunction(ast, dato)
            cadena = str(valor['type'])
            cadena = cadena.replace("ExpressionType.", "")
            tabla_html += f"<td> {dato} </td> <td> Funcion  </td>  <td> {cadena} </td>  <td> {contador}</td> <td> {contador}</td>\n"
        except:
                pass
        contador +=1
        tabla_html += "</tr>\n"

    # Cierre de la tabla
    tabla_html += "</table>"
    
    return tabla_html

def generar_grafo_tabla():
    tabla_html = generar_tabla_html_graphviz()
    grafo = "digraph G {\n"
    grafo += "node [shape=plaintext]\n"
    grafo += "nodo [label=<{}>]\n".format(tabla_html)
    grafo += "}"
    with open("grafo.dot", "w") as dot_file:
        dot_file.write(grafo)

    # Generar la imagen a partir del archivo DOT
    graph = graphviz.Source(grafo)
    graph.render("tabla de simbolos", format="png",  directory= "./static/Reportes",cleanup=True)
    print("Imagen generada con éxito. 2")


    
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
    
    
