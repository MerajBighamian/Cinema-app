import requests
res = requests.get("https://api.oceandrivers.com/static/docs.html#!/ODWeather/getWeatherDisplay_get_2")
#res = res.json
print(res)