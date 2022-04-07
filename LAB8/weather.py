import pyowm,time
APIKEY='5b22170cf9d57041c6a4ef88d5009089'                 

while True:
    OpenWMap=pyowm.OWM(APIKEY)                   
    Weather=OpenWMap.weather_manager()
    location = Weather.weather_at_place('Reykjavik,IS')
    Data=location.weather                  
    print("Humidity: ",Data.humidity,"% - Temprature: ", Data.temperature("celsius")["temp"],"C°")
    time.sleep(30)