from flask import Flask
from flask import render_template,request

app = Flask(__name__)

@app.before_request
def before_request():
    print("antes de la peticion")

@app.after_request
def after_request(response):
    print ("despues de la peticion")
    return response




#crear la ruta
@app.route('/')
def index():#esta funcion se encuentra decorada por route
    name = "codi"
    course = "Python"
    is_premium = True
    courses = ['Python','Java', 'Ruby', 'CSS']

    return render_template("index.html", username = name,course = course, is_premium=is_premium, courses = courses)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/usuario/<username>')
def usuario(username):
    
    return "hola " + username

@app.route('/datos')
def datos():
    nombre = request.args.get('nombre')
    curso = request.args.get('curso')
    return "Listado de datos" + nombre +curso


if __name__ == "__main__":
    app.run(debug=True)