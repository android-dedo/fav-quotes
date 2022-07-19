from flask import Flask , render_template , request , redirect , url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:blackbuzzard7@localhost/quotes'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qklnwvsyvmdsgw:c52293ab56f3e446ece3543e48d395e7b159a1df169a7e391712bec7a2c5b0ab@ec2-52-208-164-5.eu-west-1.compute.amazonaws.com:5432/d99kc5g5m3tom5'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
class Favquotes(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    author = db.Column(db.String(30))
    quote = db.Column(db.String(200))

@app.route('/')
def index():
    result = Favquotes.query.all()
    return(render_template('index.html', result = result))

@app.route('/quotes')
def quotes():
    return(render_template('quotes.html'))

@app.route('/process' , methods = ['POST'])
def process():
    author = request.form['author']
    quote = request.form['quote']
    quotedata = Favquotes(author = author , quote = quote)
    db.session.add(quotedata)
    db.session.commit()

    return(redirect(url_for('index')))
