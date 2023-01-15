from app import app, db, Todo, Person

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
    db.create_all()
    # all_persons = Person.query.all()
    # for person in all_persons:
    #     db.session.delete(person)
    #     db.session.commit()

    db.session.add(Person(name="test", race_prediction="white",
    api_mean=0.3, black_mean=0.2, 
    hispanic_mean=0.4, white_mean=0.5))
    db.session.commit()


    # only need to run this line once!! (can delete it now)
    # use this line when you add a new model
    # db.create_all()

    # deleting a query
    # bad = Todo.query.get_or_404(6)
    # db.session.delete(bad)
    # db.session.commit()

    all_todos = Todo.query.all()
    for todo in all_todos:
        print(todo.todo_text)