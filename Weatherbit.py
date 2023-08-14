import requests

def get_current_weather(latitude, longitude):
    url = "https://weatherbit-v1-mashape.p.rapidapi.com/current"

    querystring = {"lon": longitude, "lat": latitude}

    headers = {
        "X-RapidAPI-Key": "a516b473d6msh632a920313cd3cdp1175e2jsn3fb328e5e530",
        "X-RapidAPI-Host": "weatherbit-v1-mashape.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching current weather. Status code: {response.status_code}")
        return None

def main():
    latitude = "38.5"
    longitude = "-78.5"

    weather_data = get_current_weather(latitude, longitude)

    if weather_data:
        print("Current Weather:")
        weather_info = weather_data.get("data", [{}])[0]
        print(f"Temperature: {weather_info.get('temp', 'N/A')}°C")
        print(f"Description: {weather_info.get('weather', {}).get('description', 'N/A')}")
        print(f"Humidity: {weather_info.get('rh', 'N/A')}%")
        print(f"Wind Speed: {weather_info.get('wind_spd', 'N/A')} m/s")
    else:
        print("No weather data found.")

if __name__ == "__main__":
    main()
