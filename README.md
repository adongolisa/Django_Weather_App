This is a simple Django-based Weather App that allows users to search for weather information by city. The app fetches real-time weather data from the OpenWeatherMap API and displays the temperature, humidity, and weather conditions.

 Features

Search for weather information by city.

Displays temperature, humidity, and weather conditions.

Uses OpenWeatherMap API for real-time data.

Simple and clean UI with CSS styling.

 Technologies Used

Django (Python Web Framework)

HTML, CSS (Frontend Styling)

JavaScript (For Interactivity)

OpenWeatherMap API (Weather Data Source)

 Installation & Setup

1. Clone the repository

git clone https://github.com/Kazenzi/django-weather-app.git
cd django-weather-app

2.  Create a Virtual Environment

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3.  Install Dependencies

pip install -r requirements.txt

4.  Set Up OpenWeatherMap API Key

Get an API key from OpenWeatherMap.

Add the API key in views.py:

api_key = "YOUR_API_KEY"

5.  Run Migrations

python manage.py migrate

6.  Start the Django Development Server

python manage.py runserver

Open the app in a browser: http://127.0.0.1:8000/
