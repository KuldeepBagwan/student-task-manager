const API_BASE = 'http://localhost:5000'; // Backend URL (must match Flask port)

// Function to load and display tasks from the backend
async function loadTasks() {
  try {
    const response = await fetch(`${API_BASE}/tasks`); // Call GET /tasks
    const tasks = await response.json();
    const taskList = document.getElementById('task-list');
    taskList.innerHTML = ''; // Clear the list
    tasks.forEach(task => {
      const li = document.createElement('li');
      li.textContent = task.task; // Display the task text
      taskList.appendChild(li);
    });
  } catch (error) {
    console.error('Error loading tasks:', error);
  }
}

// Function to add a new task
async function addTask() {
  const taskInput = document.getElementById('task-input');
  const taskText = taskInput.value.trim();
  if (!taskText) return alert('Please enter a task!');

  try {
    await fetch(`${API_BASE}/tasks`, { // Call POST /tasks
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ task: taskText })
    });
    taskInput.value = ''; // Clear the input
    loadTasks(); // Reload the list without refreshing the page
  } catch (error) {
    console.error('Error adding task:', error);
  }
}

// Event listener for the Add button
document.getElementById('add-btn').addEventListener('click', addTask);

// Load tasks when the page loads
window.onload = loadTasks;