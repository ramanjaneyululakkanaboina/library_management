Library Management System
--------------------------

Overview:
----------
This Library Management System is built using Django . The system provides functionalities for admin users to manage books and for students to view available books.

Features:
---------
Admin: Signup, Login, Book CRUD operations.

Students: View book list.

Authentication: Token-based authentication for admins.

Error Handling: Proper HTTP status codes.

Database: MySQL.

Setup Instructions:
------------------

Backend Setup (Django)

Clone the repository:

git clone https://github.com/ramanjaneyululakkanaboina/library_management.git

cd library_management/library_management_system

Create a virtual environment and activate it:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py makemigrations
python manage.py migrate

Create a superuser:

python manage.py createsuperuser

Run the development server:

python manage.py runserver

API Endpoints:
--------------

| Method | Endpoint             | Description    |
| ------ | -------------------- | -------------- |
| POST   | `/api/admin/signup/` | Admin Signup   |
| POST   | `/api/admin/login/`  | Admin Login    |
| GET    | `/api/books/`        | Get all books  |
| POST   | `/api/books/`        | Add a new book |
| PUT    | `/api/books/{id}/`   | Update a book  |
| DELETE | `/api/books/{id}/`   | Delete a book  |

Assumptions:
------------

-> Only admins can add, update, or delete books.

-> Students can only view the book list.

-> Admin authentication uses token-based authentication.

-> The MySQL database must be pre-configured in settings.py.
