import requests
import tkinter as tk

google_api = "GOOGLE_GEOCODE_API_KEY"
openweather_api = "OPENWEATHER_API_KEY"

def get_weather(location):
    geocode_url = ("https://maps.googleapis.com/maps/api/geocode/json?address=" + location + "&key=" + google_api)
    geocode_response = requests.get(geocode_url)
    geocode_data = geocode_response.json()

    latitude = str(geocode_data['results'][0]['geometry']['location']['lat'])
    longitude = str(geocode_data['results'][0]['geometry']['location']['lng'])

    openweather_url = ("https://api.openweathermap.org/data/2.5/weather?lat=" + latitude + "&lon=" + longitude + "&appid="+ openweather_api)
    weather_response = requests.get(openweather_url)
    weather_data = weather_response.json()

    weather = weather_data['weather'][0]['main']
    temp_kelvins = weather_data['main']['temp']
    temp_celius = temp_kelvins - 273.15

    location_label_1 = tk.Label(main,bg="blue",foreground="White",text=(weather, round(temp_celius,1),"c"))
    location_label_1.pack()

def get_location():
    location = location_entry.get()
    get_weather(location)

main = tk.Tk()
main.title("Weather App")
main.geometry("400x100")
main.config(bg="Blue")
location_label = tk.Label(main,bg="blue",foreground="White",text="Enter the location")
location_label.pack()
location_entry = tk.Entry(main)
location_entry.pack()
location_submit = tk.Button(main,bg="blue",foreground="White",text="SUBMIT",command=get_location)
location_submit.pack()
main.mainloop()
