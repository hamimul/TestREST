# Django API Project

This is a Django-based REST API project. Follow the instructions below to set up and run the project locally.


## 🚀 Installation Steps

### 1. Install Python 3
Ensure you have Python 3 installed on your system. You can check with:
```bash
python3 --version
```
2. Set Up Virtual Environment
Create a virtual environment:

```bash
python3 -m venv ~/.venv/django
```
💡 If you're using a specific Python version:

```bash
python -m venv ~/.venv/django
```
Activate the virtual environment:

```bash
source ~/.venv/django/bin/activate
```
Upgrade pip:

```bash

pip install -U pip
```
3. Install Dependencies
Install required Python packages from requirements.txt:

```bash

pip install -r requirements.txt
```
🛠️ Database Setup & Configuration
Ensure you have your database configured in the settings.py file. For SQLite (default), no additional setup is needed.

Run the following commands to apply migrations:

```bash

python manage.py migrate
```
👤 Create Django Superuser
Create a superuser to access the Django admin panel:

```bash

python manage.py createsuperuser
```
Follow the prompts to enter your username, email, and password.

▶️ Running the Application
Start the Django development server:

```bash

python manage.py runserver
```
Visit the app in your browser:

```bash

http://127.0.0.1:8000/
```
You should see the login screen. Use the superuser credentials to log in.

🧪 Testing the API Endpoints
You can test the API via a browser or Postman.

Example Endpoints:
GET /api/countries/ - List all countries

GET /api/countries/1/ - Get details of a specific country

GET /api/countries/1/same_region/ - Get countries in the same region

GET /api/countries/by_language/?language=English - Get countries that speak English

You can use the Django REST Framework’s browsable interface for testing or tools like Postman for POST, PUT, DELETE requests.

🔄 Updating Django
To update Django to the latest version:

```bash

pip install -U Django
```
Check the Django version:

```bash

django-admin --version
```
✅ Summary
Install Python 3

Create and activate virtual environment

Install dependencies

Apply migrations

Create superuser

Run the server

Test API endpoints

