from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app  = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

todos = ["Learn Flask", "Setup venv", "Build a Cool App"]

class TodoForm(FlaskForm):
    todo = StringField("Todo")
    submit = SubmitField("Add Todo")

@app.route('/', methods=["GET", "POST"])
def index():
    # if any request if made, and it has a "todo" attribute
    if 'todo' in request.form:
        # append the new todo from the form to the array
        todos.append(request.form['todo'])
    return render_template('index.html', todos=todos, template_form=TodoForm())
