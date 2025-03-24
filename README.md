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

git clone https://github.com/your-repo/library-management.git
cd library-management/backend

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
