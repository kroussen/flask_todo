from flask import Flask

app = Flask(__name__)


@app.route('/')
def all_tasks():
    return 'Все задачи'


@app.route('/new_task', methods=('GET', 'POST'))
def new_task():
    return 'новая задвча'


@app.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    return 'удалить задачу'


@app.route('/complete_task/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    return 'завершить задачу'


if __name__ == '__main__':
    app.run(debug=True)
