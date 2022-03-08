from app import app
from flask import render_template
from app.random.models import randomAction
from app.allcards.models import AllCards

@app.route("/")
def index():
    cartasValue = randomAction().randomize()
    return render_template('index.html', cartas=cartasValue)

'''@app.route("/all")
def allcards():
    Allcartas = AllCards().AllCardsReturn()
    return render_template('allcards.html', cartas=Allcartas)
'''

