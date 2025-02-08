# Overview
The Task Manager App is a simple web application that allows users to manage their tasks. Users can add new tasks, edit existing tasks, and delete tasks. The app uses Flask for the backend and stores tasks in the server-side session, making it a lightweight and session-based task manager.

Key Features
Add Tasks:

Users can add new tasks by entering them in an input field and submitting the form.

Tasks are stored in the session and displayed in a list.

Edit Tasks:

Users can edit any task by clicking the "Edit" link next to the task.

The app redirects to an edit page where the user can update the task.

Delete Tasks:

Users can delete a task by clicking the "Delete" link next to the task.

The task is removed from the session, and the list is updated.

Session Storage:

Tasks are stored in the server-side session (session['tasks']), making them persistent for the duration of the user's session.

No database is required, making the app simple and easy to set up.

Technical Details
Framework: Flask (Python)

Session Management: Flask's session object is used to store tasks.

Templates: Jinja2 is used for rendering HTML templates.

Routes:

/: Displays the list of tasks and a form to add new tasks.

/add: Handles the addition of new tasks.

/edit/<int:task_id>: Handles editing of tasks.

/delete/<int:task_id>: Handles deletion of tasks.
