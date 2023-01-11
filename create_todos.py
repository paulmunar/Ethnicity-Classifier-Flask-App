from app import app, db, Todo

todos = ["Learn Flask", "Setup venv", "Add name classification", "Add face classification"]
first_todo = Todo(todo_text="Add face classification")

# committing models to the database
# once again, these commands only need to be run once
# ALTERNATIVELY you can do all this in the terminal 
'''
> python3
>>> from app import db, todo
>>> second_todo = Todo(todo_text="Setup venv")
>>> db.session.add(second_todo)
# dont even need to put second_todo in a variable, can just straight add it 
'''
with app.app_context():
    # deleting a query
    # bad = Todo.query.get_or_404(6)
    # db.session.delete(bad)
    # db.session.commit()

    all_todos = Todo.query.all()
    for todo in all_todos:
        print(todo.todo_text)