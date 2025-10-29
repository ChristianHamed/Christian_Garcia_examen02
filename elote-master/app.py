from flask import Flask, render_template, request
from entities.palindrome import Palindrome
from entities.animal import Animal

app = Flask(__name__)

#Esta será la ruta index (de la página principal)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/math')
def math():
    return render_template('math.html')

@app.route('/animals')
def animals():
    return render_template('animals.html', animals = Animal.get_list())

@app.route('/palindrome', methods=['GET', 'POST'])
def palindrome():
    if request.method == 'POST':
        phrase = request.form.get('input_phrase')

        p = Palindrome(phrase)
        result = p.is_palindrome()
        return render_template('result.html', resultado = result)
    return render_template('palindrome.html')

if __name__ == '__main__':
    #Ejecuta Flask con la configuración predeterminada, la cual es:
    # localhost (127.0.0.1) No permite conexiones externas
    # Puerto 5000
    #app.run()

    #Lo cambiamos para permitir conexiones internas desde la IP dinámica y con un puerto personalizado.
    app.run(host='0.0.0.0', port=5147)

@app.route('/sorteo', methods=['GET', 'POST'])
def sorteo():
    if request.method == 'POST':
        n1 = int(request.form['numero1'])
        n2 = int(request.form['numero2'])
        n3 = int(request.form['numero3'])
        juego = Sorteo(n1, n2, n3)
        return render_template('resultado-sorteo.html', mensaje=juego.jugar())
    return render_template('sorteo.html')