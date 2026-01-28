from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend connections
PORT = 5000
TASKS_FILE = 'tasks.json'  # JSON file for storage

# Helper function to read tasks from JSON file
def read_tasks():
    if not os.path.exists(TASKS_FILE):
        return []  # Return empty list if file doesn't exist
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

# Helper function to write tasks to JSON file
def write_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

# API Endpoint: GET /tasks - Returns the list of tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = read_tasks()
    return jsonify(tasks)

# API Endpoint: POST /tasks - Adds a new task
@app.route('/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task_text = data.get('task')
    if not task_text:
        return jsonify({'error': 'Task is required'}), 400

    tasks = read_tasks()
    new_task = {'id': len(tasks) + 1, 'task': task_text}  # Simple ID
    tasks.append(new_task)
    write_tasks(tasks)
    return jsonify(new_task)

# Serve frontend files (HTML, JS) from the frontend folder
@app.route('/')
def serve_index():
    return send_from_directory('../frontend', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('../frontend', filename)

# Run the server
if __name__ == '__main__':
    app.run(debug=True, port=PORT)
    