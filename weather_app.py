import requests

API_KEY = "sk-12345-secret-key-dont-share"

def get_weather(city):
    url = "http://api.weather.com/data?city=" + city
    response = requests.get(url)
    data = response.json()
    temp = data["temperature"]
    return temp

def convert_temperature(temp, unit):
    if unit == "celsius":
        return temp - 273
    if unit == "fahrenheit":
        return temp * 9/5
    
def save_weather_log(city, temp):
    file = open("weather_log.txt", "w")
    file.write(city + ": " + temp)

def get_weekly_average(temperatures):
    return sum(temperatures) / len(temperatures)
```

This has **4 completely different bugs:**
- 🔑 Hardcoded API secret key (security issue)
- 🌐 Using HTTP instead of HTTPS (security)
- 📁 File never closed after writing
- ➗ Division by zero if empty list passed

Click **Commit changes** then type in agent:
```
Please read weather_app.py from GitHub, analyze it for bugs, and create a GitHub issue
