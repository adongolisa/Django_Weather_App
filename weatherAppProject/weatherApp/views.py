from django.shortcuts import render
import requests
import os

def index(request):
    city = request.GET.get('city', 'Nairobi')  # Default city
    api_key = os.getenv("WEATHER_API_KEY", "YOUR_DEFAULT_API_KEY")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    weather_data = response.json()

    context = {
        "city": city,
        "temperature": weather_data.get("main", {}).get("temp", "N/A"),
        "humidity": weather_data.get("main", {}).get("humidity", "N/A"),
        "description": weather_data["weather"][0]["description"] if "weather" in weather_data else "N/A",
        "icon": weather_data["weather"][0]["icon"] if "weather" in weather_data else "",
    }
    
    return render(request, 'weatherApp/index.html', context)


