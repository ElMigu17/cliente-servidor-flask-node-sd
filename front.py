from flask import Flask
from flask import render_template
app =  Flask(__name__)


lista_obj=[
    {"id": 10,
    "done": False,
    "description": "Limpar quarto",
    "deadline": "10/11"},
    {"id": 11,
    "done": True,
    "description": "Tirar lixo",
    "deadline": "10/11"},
    {"id": 12,
    "done": False,
    "description": "Cozinhar torta",
    "deadline": "15/11"},
    {"id": 13,
    "done": False,
    "description": "Comprar torneira",
    "deadline": "17/11"},
]

@app.route("/")
def index():
    return "<h1>hi</h1>"

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('front.html', len=len(lista_obj), objects=lista_obj)

if __name__ == "__main__":
    app.run()