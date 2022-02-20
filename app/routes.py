from app import app
from flask import render_template
from app.random.models import randomAction

@app.route("/")
def main():
    return '<a href="/index"><button>Cartas</button></a>'

@app.route("/index")
def index():
    cartasValue = randomAction().randomize()
    
    return render_template('index.html', cartas=cartasValue)


