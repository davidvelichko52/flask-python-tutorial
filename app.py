from flask import Flask, redirect, render_template, request
from pymongo import MongoClient

client = MongoClient()
db = client.operators
collection = db.op

host = 'localhost'
port = 27017
client = MongoClient()
db = client.test_database
op = db.dinosaur_collection

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/loops')
def loops():
    return render_template('loops.html')

@app.route('/operators', methods=('GET', 'POST'))
def operators():
    if request.method == 'POST':
        db.op.insert_one({
            'name': request.form['name'],
            'description': request.form['description'],
            'symbol': request.form['symbol'],
            'example': request.form['example'],
            'uses': request.form['uses']
        })
        return redirect('/operators')
    else:
        operators = db.op.find()
        return render_template('operators.html', operators=operators)

if __name__ == "__main__":
    app.run()