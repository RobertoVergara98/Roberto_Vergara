from flask import Flask, render_template, request

app = Flask(__name__)


# Ruta para la página principal
@app.route('/')
def index():
    return render_template('index.html')


# Ruta para el Ejercicio 1 (Notas)
@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        # Obtener los datos del formulario como enteros
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        # Calcular el promedio
        promedio = (nota1 + nota2 + nota3) / 3

        # Evaluar condiciones de aprobación
        if promedio >= 40 and asistencia >= 75:
            estado = "Aprobado"
        else:
            estado = "Reprobado"

        # Retornar la vista con los resultados calculados
        return render_template('ejercicio1.html', promedio=round(promedio, 1), estado=estado)

    # Si la petición es GET, solo muestra el formulario vacío
    return render_template('ejercicio1.html')


# Ruta para el Ejercicio 2 (Nombres)
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        # Obtener nombres del formulario
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        nombres = [nombre1, nombre2, nombre3]

        # Encontrar el nombre con mayor longitud
        nombre_mayor = max(nombres, key=len)
        longitud = len(nombre_mayor)

        return render_template('ejercicio2.html', nombre_mayor=nombre_mayor, longitud=longitud)

    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)