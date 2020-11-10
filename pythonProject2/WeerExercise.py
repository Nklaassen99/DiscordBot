import pyowm

owm = pyowm.OWM('9b8570036732dd3c168f5870dd01c086')


print('Van welke stad wil je het weer en de temperatuur weten?')
Stad = input()
location = owm.weather_at_place(Stad)
weather = location.get_weather()
tempdict = weather.get_temperature('celsius')
status = weather.get_detailed_status()
x = tempdict['temp_max']

print(x)
print(weather)
print(int(tempdict['temp']))
print(status)



