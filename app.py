from flask import Flask, request, jsonify
from flask import Flask, render_template, request
from clases import Empleado, Gerente

app = Flask(__name__)

@app.route('/health', methods=['GET'])  
def health_check():  
    return jsonify({"status": "ok", "message": "Servidor activo"}), 200

@app.route('/')
def formulario():
    return render_template('formulario.html')

@app.route('/calcular', methods=['POST'])
def calcular():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    salario_base = float(request.form['salario_base'])
    tipo_empleado = request.form['tipo_empleado']

    if tipo_empleado == 'gerente':
        bono = float(request.form['bono'])
        empleado = Gerente(nombre, edad, salario_base, bono)
    else:
        empleado = Empleado(nombre, edad, salario_base)

    salario_mensual = empleado.calcular_salario_mensual()
    return render_template('resultado.html', nombre=nombre, salario=round(salario_mensual, 2))

if __name__ == '__main__':
    app.run(debug=True)


