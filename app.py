from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simpan tugas dalam list sementara
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']
    tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        del tasks[task_id]
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['POST'])
def edit_task(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id] = request.form['task']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
