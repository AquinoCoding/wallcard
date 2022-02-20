from app import app
from flask import render_template
from app.random.models import randomAction

@app.route("/")
def index():
    cartasValue = randomAction().randomize()
    return render_template('index.html', cartas=cartasValue)


