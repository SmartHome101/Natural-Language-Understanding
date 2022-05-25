import requests
from utils.TTS import speak


def weather(result):
    city_name = '' 
    
    if result['Entities'] is None:
            city_name = 'cairo'
        
    elif 'location' not in result['Entities']:
        city_name = 'cairo'
    
    else :
        city_name += result['Entities']['location']
    
    api_key = "661d81f3b17f7764fba64a3b2e0118db"
    complete_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name,api_key)
    response = requests.get(complete_url)
    
    x = response.json()
    if x["cod"] != "404":
        y = x["main"]
        z = x["weather"]
        
        min_temp = round(y["temp_min"] - 273.15,2)
        max_temp = round(y["temp_max"] - 273.15,2)
        weather_description = z[0]["description"]
        
        res = "The weather forecast in {} is {} with a minimum of {} Celsius and a maximum of {} Celsius".format(city_name,weather_description,min_temp,max_temp)
        speak(res)
        
    else:
        speak("There are error")