from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '1234567890'  # Set a secret key for session encryption

# Initialize tasks in the session if not already present
@app.before_request
def initialize_tasks():
    if 'tasks' not in session:
        session['tasks'] = []

@app.route('/')
def index():
    tasks = enumerate(session.get('tasks', []))
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:
        session['tasks'] = session.get('tasks', []) + [task]
        session.modified = True  # Ensure the session is saved
    return redirect('/')

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    tasks = session.get('tasks', [])
    if request.method == 'POST':
        new_task = request.form.get('task')
        if new_task and 0 <= task_id < len(tasks):
            tasks[task_id] = new_task
            session['tasks'] = tasks
            session.modified = True
            return redirect('/')
    elif 0 <= task_id < len(tasks):
        return render_template('edit.html', task=tasks[task_id], task_id=task_id)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks = session.get('tasks', [])
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
        session['tasks'] = tasks
        session.modified = True
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)