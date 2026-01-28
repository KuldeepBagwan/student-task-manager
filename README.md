# Title
# student-task-manager
# Goal
This full-stack web application allows students to add and view homework tasks through a simple API-driven interface, updating the task list dynamically without page refreshes.

# The Logic (How I Thought)
# Why Did I Choose This Approach?
I chose a simple full-stack setup with Python (Flask) for the backend and plain HTML/JS for the front
end because it aligns with your Python domain, keeps things beginner-friendly, and meets the requirements without overcomplicating. Flask is lightweight for building the API (add/list tasks), JSON storage is easy to manage locally (no database setup needed), and vanilla JS ensures the SPA updates dynamically via fetch() calls—avoiding frameworks like React to keep it minimal. This approach "connects" everything locally or on a platform like Heroku, making it deployable and scalable for a small app like a task manager.
# What Was the Hardest Bug I Faced, and How Did I Fix It?
The hardest bug was a CORS (Cross-Origin Resource Sharing) error during local testing—when the frontend (running in the browser) tried to call the Flask API, it blocked requests with "Access-Control-Allow-Origin" issues, preventing tasks from adding. This happened because browsers restrict cross-origin requests for security. I fixed it by installing and enabling flask-cors in the backend (from flask_cors import CORS; CORS(app) in app.py), which adds the necessary headers to allow the frontend to connect. After restarting the server, the API calls worked seamlessly. If deploying to Heroku, I ensured the Procfile and port settings matched to avoid path-related 404s.

#  Output Screenshots: Embed the images proving your code works (as requested in the problem statement).
<img width="384" height="257" alt="image" src="https://github.com/user-attachments/assets/2828dfec-9ca8-4304-bc2a-41bdd588b7f2" />

# Future Improvements: If I Had 2 More Days, What Would I Add?
If I had 2 more days to enhance the Student Task Manager, I'd focus on user experience, data persistence, and basic security to make it more practical for real students. Here's what I'd add, prioritized by impact and feasibility:

Task Editing and Deletion (Day 1): Add "Edit" and "Delete" buttons next to each task in the list. In the frontend (script.js), I'd add event listeners to update the input field for editing or send a DELETE request to the backend. On the backend (app.py), I'd add a DELETE /tasks/<id> endpoint to remove tasks from tasks.json. This improves usability—students often need to modify or remove tasks. (Why? It turns the app from read-only to interactive, reducing frustration.)

Due Dates and Task Categories (Day 1-2): Extend the task model to include due dates (using HTML <input type="date">) and categories (e.g., "Homework", "Project"). Update the API to handle these fields, and display them in the list (e.g., "Math Homework - Due: 2023-10-15"). Store in JSON or switch to SQLite for better structure. This adds value for students tracking deadlines. (Why? Makes the app more functional for schoolwork without overcomplicating the UI.)

Basic Authentication and User Sessions (Day 2): Add simple login (e.g., username/password stored in JSON) using Flask sessions. Protect the API routes so only logged-in users can add/view tasks. This prevents shared data issues if deployed publicly. (Why? For a student app, privacy is key—imagine multiple users on the same device.)

Responsive Design and Styling (Bonus, if time allows): Use CSS media queries to make the app mobile-friendly (e.g., stack elements vertically on small screens). Add a simple theme (e.g., dark mode toggle). This polishes the UI without backend changes.
