#  TaskFlow - Project & Task Management System

A complete Project and Task Management System built using **FastAPI, MySQL, HTML, CSS, and JavaScript**.

TaskFlow helps organizations manage projects, assign tasks, monitor employee progress, generate reports, upload attachments, and track project completion through a centralized dashboard.

---

#  Table of Contents

* Introduction
* Features
* System Architecture
* Technology Stack
* Project Structure
* Database Design
* API Endpoints
* Installation Guide
* Usage Guide
* Screenshots
* Future Enhancements
* Author

---

#  Introduction

TaskFlow is designed to simplify project management and task tracking.

The system provides:

* Secure Authentication
* Role-Based Access Control
* Project Tracking
* Employee Task Assignment
* Task Progress Monitoring
* PDF Report Generation
* File Upload Support
* Dashboard Analytics

The platform supports both **Admin** and **Employee** users.

---

#  Features

## Authentication

* User Registration
* Secure Login
* Logout
* Session Management
* Role-Based Authorization

---

## Admin Features

### Dashboard

* Total Projects
* Active Projects
* Completed Projects
* Total Tasks
* Completed Tasks
* Recent Projects
* Recent Tasks

### Project Management

* Create Projects
* Edit Projects
* Delete Projects
* View Project Details
* Project Progress Tracking

### Task Management

* Create Tasks
* Assign Tasks
* Edit Tasks
* Delete Tasks
* Change Task Status
* Monitor Task Progress

### User Management

* View Users
* Manage Employee Accounts

### Reports

* Generate PDF Reports
* Download Reports

---

## Employee Features

### Employee Dashboard

* View Assigned Tasks
* Check Task Status
* Track Deadlines
* Update Task Progress

---

## Attachments

* Upload Files
* Download Files
* Manage Task Documents

---

## Email Notifications

* Task Assignment Notifications
* Project Updates

---

#  System Architecture

```text
+----------------------+
|      Frontend        |
| HTML CSS JavaScript  |
+----------+-----------+
           |
           |
           ▼
+----------------------+
|      FastAPI API     |
|     Router Layer     |
+----------+-----------+
           |
           |
           ▼
+----------------------+
|   Service Layer      |
| Business Logic       |
+----------+-----------+
           |
           |
           ▼
+----------------------+
|     MySQL Database   |
+----------------------+
```

---

#  Technology Stack

## Backend

* FastAPI
* Python
* Pydantic
* Uvicorn
* ReportLab

## Frontend

* HTML5
* CSS3
* JavaScript

## Database

* MySQL

## Other Tools

* Git
* GitHub
* VS Code

---

#  Project Structure

```text
TaskFlow/
│
├── database/
│   └── db.py
│
├── frontend/
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── projects.html
│   ├── project-details.html
│   ├── tasks.html
│   ├── users.html
│   ├── reports.html
│   └── employee-dashboard.html
│
├── models/
│   ├── user.py
│   ├── project.py
│   ├── task.py
│   └── login.py
│
├── routers/
│   ├── auth.py
│   ├── users.py
│   ├── projects.py
│   ├── tasks.py
│   ├── reports.py
│   └── attachments.py
│
├── services/
│   ├── auth_service.py
│   ├── user_service.py
│   ├── project_service.py
│   ├── task_service.py
│   ├── report_service.py
│   ├── attachment_service.py
│   └── email_service.py
│
├── static/
│   ├── style.css
│   ├── app.js
│   ├── projects.js
│   ├── tasks.js
│   ├── users.js
│   ├── reports.js
│   └── employee-dashboard.js
│
├── uploads/
│
├── utils/
│   └── auth.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

#  Database Design

## Users Table

```sql
CREATE TABLE users(
    User_id INT PRIMARY KEY,
    Username VARCHAR(100),
    Mail VARCHAR(100),
    Password VARCHAR(255),
    Role ENUM('Admin','Employee')
);
```

---

## Projects Table

```sql
CREATE TABLE projects(
    Project_id INT PRIMARY KEY,
    Project_name VARCHAR(255),
    Description TEXT,
    Created_on DATE,
    Deadline DATE,
    Project_Status ENUM(
        'Active',
        'Completed'
    ),
    is_deleted BOOLEAN
);
```

---

## Tasks Table

```sql
CREATE TABLE tasks(
    Task_id INT AUTO_INCREMENT PRIMARY KEY,
    Project_id INT,
    Task_name VARCHAR(255),
    Description TEXT,
    Assigned_by VARCHAR(100),
    Assigned_to VARCHAR(100),
    Deadline DATE,
    Status ENUM(
        'Pending',
        'In Progress',
        'Completed'
    )
);
```

---

## Notifications Table

```sql
CREATE TABLE notifications(
    Notification_id INT AUTO_INCREMENT,
    User_Email VARCHAR(100),
    Message TEXT,
    Created_on DATETIME
);
```

---

## Attachments Table

```sql
CREATE TABLE attachments(
    Attachment_id INT AUTO_INCREMENT,
    Task_id INT,
    File_name VARCHAR(255),
    File_path VARCHAR(500)
);
```

---

#  API Endpoints

## Authentication

```http
POST /auth/register
POST /auth/login
GET  /auth/logout
GET  /auth/me
```

---

## Projects

```http
GET    /projects/
POST   /projects/
PUT    /projects/{id}
DELETE /projects/{id}
GET    /projects/recent
GET    /projects/dashboard/stats
```

---

## Tasks

```http
GET    /tasks/
POST   /tasks/
PUT    /tasks/{id}
DELETE /tasks/{id}
GET    /tasks/project/{id}
GET    /tasks/mytasks
GET    /tasks/recent
```

---

## Users

```http
GET /users/
```

---

## Reports

```http
GET /reports/projects
```

---

#  Installation

## Clone Repository

```bash
git clone https://github.com/yourusername/TaskFlow.git
cd TaskFlow
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Environment

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Configure Database

Update:

```python
database/db.py
```

```python
host="127.0.0.1"
user="root"
password="your_password"
database="taskflow"
```

---

## Run Server

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

---

#  Workflow

```text
Admin Login
     ↓
Create Project
     ↓
Assign Tasks
     ↓
Employee Dashboard
     ↓
Employee Updates Status
     ↓
Project Progress Updated
     ↓
Report Generation
```

---

#  Screenshots

Add screenshots here:

```text
screenshots/
├── login.png
├── dashboard.png
├── projects.png
├── tasks.png
├── reports.png
└── employee-dashboard.png
```

---

#  Future Enhancements

* JWT Authentication
* Dark Mode
* Real-Time Notifications
* Team Chat System
* Mobile Application
* Calendar Integration
* AI Task Recommendations
* Analytics Dashboard
* Role Management System

---

#  Author

**Gopinath T**

B.Tech Artificial Intelligence and Data Science

Project: TaskFlow Management System

Year: 2026

---

#  License

This project is developed for educational and learning purposes.

Feel free to modify and extend the project.
