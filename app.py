from flask import Flask, render_template, request
from forms import TodoForm, NameForm
from ethnicolr import pred_census_ln
from flask_sqlalchemy import SQLAlchemy
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_text = db.Column(db.String(100), index=True)

# only need to run this line once! (can delete it now)
# with app.app_context():
#     db.create_all()

@app.route('/', methods=["GET", "POST"])
def index():
    todo_form = TodoForm()
    # if any request if made, and it has a "todo" attribute (from TodoForm class)
    if "todo" in request.form: # and todo_form.validate_on_submit():
        db.session.add(Todo(todo_text=todo_form.todo.data))
        db.session.commit()
    return render_template('index.html', todos=Todo.query.all(), template_form=todo_form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/name_classification', methods=["GET", "POST"])
def name_classification():
    name_form = NameForm()
    first_name, last_name = None, None
    first_name_race, last_name_race = None, None
    if "first_name" in request.form and "last_name" in request.form:
        first_name = name_form.first_name.data
        last_name = name_form.last_name.data
        names = [{"name":first_name},{"name":last_name}]
        df = pd.DataFrame(names)
        pred_df = pred_census_ln(df, "name", year=2010, num_iter=100, conf_int=0.9)
        first_name_race = pred_df["race"][0]
        last_name_race = pred_df["race"][1]
        
    return render_template('name_classification.html', template_form=name_form, first_name=first_name, last_name=last_name,
    first_name_race=first_name_race, last_name_race=last_name_race)

@app.route('/name_classification/<name>')
def name_data(name):
    # this is bad... repeating pred_census_ln
    categories = ["api_mean", "black_mean", "hispanic_mean", "white_mean"]
    names = [{"name":name}]
    df = pd.DataFrame(names)
    pred_df = pred_census_ln(df, "name", year=2010, num_iter=100, conf_int=0.9)
    return render_template('name_data.html', name=name, pred_df=pred_df, categories=categories)
