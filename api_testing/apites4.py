import requests
#import key

url = "https://api.openweathermap.org/data/2.5/weather?q=London&APPID=" + WEATHERKEY
resp = requests.get(url)
print(resp.json())
