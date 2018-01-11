from forecast import GiatecForecast

import datetime, time


forecast = GiatecForecast()
lat = 48.8567
lon = 2.3508
future = 1495425600  # '2017-05-22'
past = 1463976000  # '2016-04-10'

# future = forecast.getFutureForecast(lat, lon, 4, future)
# print(future, "\n")

# history = forecast.getHistory(lat, lon, 30, past)
# print(history, "\n")


'''history_history = forecast.getWeatherRange(lat, lon, 1491969600, 1493438400)  # 4.12  4.28
print("4.12  4.28\n", history_history, "\n")

history_now = forecast.getWeatherRange(lat, lon, 1494216000, 1494475200)  # 5.08  5.10
print("5.08  5.10\n", history_now, "\n")
'''
history_future = forecast.getWeatherRange(lat, lon, 1491796800, 1495684800)  # 4.10  5.24
print("4.10  5.24\n", history_future, "\n")
'''
now_now = forecast.getWeatherRange(lat, lon, 1494388800, 1494475200)  # 5.10  5.10
print("5.10  5.10\n", now_now, "\n")

now_future = forecast.getWeatherRange(lat, lon, 1494388800, 1495339200)  # 5.10  5.20
print("5.10  5.20\n", now_future, "\n")

future_future = forecast.getWeatherRange(lat, lon, 1494820800, 1495339200)  # 5.15  5.20
print("5.15  5.20\n", future_future, "\n")'''





