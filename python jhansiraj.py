import requests
import requests,_json

# Replace 'YOUR_API_KEY' with your actual API key from OpenWeatherMap
API_KEY = 'us&appid=b6907d289e10d714a6e88b30761fae22'
API_URL = 'https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22'


def get_weather_data(date):
    params = { 'appid': API_KEY}
    response = requests.get(API_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return data.get(date, None)
    else:
        print(f"Error: {response.status_code}")
        return None

def print_temperature():
    
    date = input("Enter the date (DD-MM-YYYY): ")

    data = get_weather_data(date)
    if data:
        temperature = data['main']['temp']
        print(f"The temperature on {date}  is {temperature:.2f}°C")
    else:
        print("Weather data not available for the specified date.")

def print_wind_speed():
    
    date = input("Enter the date (DD-MM-YYYY): ")

    data = get_weather_data(date)
    if data:
        wind_speed = data['wind']['speed']
        print(f"The wind speed on {date} is {wind_speed} m/s")
    else:
        print("Weather data not available for the specified date.")

def print_pressure():
    
    date = input("Enter the date (DD-MM-YYYY): ")

    data = get_weather_data(date)
    if data:
        pressure = data['main']['pressure']
        print(f"The pressure on {date} is {pressure} hPa")
    else:
        print("Weather data not available for the specified date.")

def main():
    while True:
        print("\nOptions:")
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        option = input("Enter your choice: ")

        if option == '1':
            print_temperature()
        elif option == '2':
            print_wind_speed()
        elif option == '3':
            print_pressure()
        elif option == '0':
            break
        else:
            print("Invalid option. Please try again.")
            
if __name__=="__main__":
   main()