from flask import Flask, render_template, request
from form import Datos

app = Flask(__name__)
app.secret_key='123456'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/accesorios')
def accesorios():
    return render_template('accesorios.html')

@app.route('/rines')
def rines():
    return render_template('rines.html')

@app.route('/llantas')
def llantas():
    return render_template('llantas.html')

@app.route('/cotizacion', methods=['POST', 'GET'])
def cotizacionobjeto():
    form = Datos()
    if request.method == 'POST':
        return "nombre={request.form['nombre']} | apellido={request.form['apellido']} | direccion={request.form['direccion']} | tel={request.form['tel']} | cotizacion={request.form['cotizacion']}"
    return render_template('cotizacion.html', form=form)

if __name__=='__main__':
    app.run(debug=True)