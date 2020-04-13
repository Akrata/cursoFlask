from flask import Flask
from flask import render_template

app = Flask(__name__)

#crear la ruta
@app.route('/')
def index():#esta funcion se encuentra decorada por route
    name = "codi"
    return render_template("index.html", username = name)



if __name__ == "__main__":
    app.run(debug=True)