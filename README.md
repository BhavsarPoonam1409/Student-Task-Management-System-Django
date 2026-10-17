# Student Task Management System

## Practical Assignment – Question 1

**Project Title:** Student Task Management System
**Technology Used:** Python, Django, HTML, CSS, SQLite

### Aim

To develop a Student Task Management System using Django that allows users to manage their tasks efficiently.

### Project Description

The Student Task Management System is a web application developed using Python and Django. Users can create an account, log in, add tasks, view task details, edit or delete tasks, and mark tasks as completed. Each user can manage their own tasks through a personalized dashboard.

### Features

* User Registration and Login
* User Authentication and Logout
* Personalized Dashboard
* Add New Tasks
* View Task Details
* Edit and Delete Tasks
* Mark Tasks as Completed or Pending
* Set Task Priority (Low, Medium, High)
* Add Task Due Dates
* Dashboard displaying total, pending, and completed tasks
* Responsive user interface

### Technologies Used

* **Frontend:** HTML5, CSS3
* **Backend:** Python, Django
* **Database:** SQLite
* **Authentication:** Django Authentication System
* **Version Control:** Git and GitHub

### Project Structure

```text
Student-Task-Management-System-Django/
│
├── manage.py
├── db.sqlite3
├── Qus1_Student_Task_Management_System/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── tasks/
│   ├── migrations/
│   ├── templates/
│   │   └── tasks/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── dashboard.html
│   │       ├── task_form.html
│   │       ├── task_detail.html
│   │       └── task_confirm_delete.html
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
│
└── static/
    └── css/
        └── style.css
```

### Installation and Execution

**Step 1: Clone the repository**

```bash
git clone https://github.com/BhavsarPoonam1409/Student-Task-Management-System-Django.git
```

**Step 2: Open the project directory**

```bash
cd Student-Task-Management-System-Django
```

**Step 3: Install Django**

```bash
pip install django
```

**Step 4: Apply database migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

**Step 5: Run the development server**

```bash
python manage.py runserver
```

**Step 6: Open the application**

Open the following address in your browser:

```text
http://127.0.0.1:8000/
```

### Expected Outcome

The application allows users to register, log in, and manage their personal tasks. Users can add, update, view, delete, and complete tasks while monitoring their progress through the dashboard.

### Conclusion

The Student Task Management System demonstrates the use of Django for web application development, user authentication, database operations, CRUD functionality, and responsive interface design.

---

**Developed by:** Poonam Bhavsar
**Course:** M.Sc. IT (Software Development)
**Assignment:** Practical Question 1
