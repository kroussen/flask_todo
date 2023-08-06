from flask import Flask, render_template, request, redirect, url_for
from models import db, Task
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.getcwd(), 'instance/tasks.db')
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def all_tasks():
    tasks = Task.query.all()
    return render_template('all_tasks.html', tasks=tasks)


@app.route('/new_task', methods=('GET', 'POST'))
def new_task():
    if request.method == 'POST':
        task = request.form.get('task')
        new_task = Task(title=task)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('all_tasks'))
    return render_template('new_task.html')


@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('all_tasks'))


@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = True
        db.session.commit()
    return redirect(url_for('all_tasks'))


if __name__ == "__main__":
    app.run(debug=True)
