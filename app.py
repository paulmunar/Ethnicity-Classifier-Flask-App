from flask import Flask, render_template, request
from app_forms import TodoForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

# data - should probably be in its own file
todos = ["Learn Flask", "Setup venv", "Build a Cool App"]

@app.route('/', methods=["GET", "POST"])
def index():
    todo_form = TodoForm()
    # if any request if made, and it has a "todo" attribute (from TodoForm class)
    if todo_form.validate_on_submit():
        # append the new todo from the form to the array
        todos.append(todo_form.todo.data)
    return render_template('index.html', todos=todos, template_form=todo_form)

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/about')
def about():
    return render_template('about.html')
