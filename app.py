from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_text = db.Column(db.String(100), index=True)

class Person(db.Model):
    # id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), primary_key=True, unique=True)
    race_prediction = db.Column(db.String(100), index=True)
    api_mean = db.Column(db.Float, index=True)
    black_mean = db.Column(db.Float, index=True)
    hispanic_mean = db.Column(db.Float, index=True)
    white_mean = db.Column(db.Float, index=True)

# clean out database
with app.app_context():
    all_persons = Person.query.all()
    for person in all_persons:
        db.session.delete(person)
        db.session.commit()

import routes
