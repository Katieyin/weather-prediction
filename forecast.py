from apixu.client import ApixuClient

from datetime import datetime
import time

def dictForm(query):
    dictionary = dict()
    for i in range(0, 24):
        t = query['forecast']['forecastday'][0]['hour'][i]['time_epoch']
        # t = query['forecast']['forecastday'][0]['hour'][i]['time']
        temp = query['forecast']['forecastday'][0]['hour'][i]['temp_c']
        dictionary.update({t: temp})
    # print(dictionary)
    return dictionary

class GiatecForecast:

    forecast = ApixuClient('9efb84acc45d4c13bbe164406170905')

    def getFutureForecast(self, lat, lon, days, start_date):
        query = (lat, lon)
        forecast = dict()
        for i in range(0, days):
            date = datetime.fromtimestamp(int(start_date)).strftime('%Y-%m-%d')
            print(date)
            result = self.forecast.getForecastWeather(q=query, dt=date)
            start_date = start_date + 86400
            dictionary = dictForm(result)
            forecast.update(dictionary)
        return forecast

    def getHistory(self, lat, lon, days, start_date):
        query = (lat, lon)
        history = dict()

        for i in range(0, days):
            date = datetime.fromtimestamp(int(start_date)).strftime('%Y-%m-%d')
            print(date)
            result = self.forecast.getHistoricalWeather(q=query, dt=date)
            start_date = start_date + 86400
            dictionary = dictForm(result)
            history.update(dictionary)
        return history

    def getWeatherRange(self, lat, lon, time1, time2):
        now = datetime.now().date()
        unix_now = int(time.mktime(now.timetuple()))
        time_range = int((time2 - time1) / 86400)
        # upper bound smaller than lower bound
        if time2 < time1:
            print("\nError1! time1 has to be smaller than time2!\n")
            return

        # time1 and time2 are both in the past
        if unix_now >= time2:
            if unix_now - time1 > 2592000:
                print("\nError2! limited to get history data within last 30 days only!\n")
                return
            else:
                return self.getHistory(lat, lon, time_range, time1)

        # time1 and time2 are both in the future
        if unix_now <= time1:
            if time2 - unix_now > 1296000:
                print("\nError3! limited to get future data within next 15 days only!\n")
                return
            else:
                return self.getFutureForecast(lat, lon, time_range, time1)

        # time1 is in the past and time2 is in future
        if (time1 < unix_now) and (time2 > unix_now):
            wr_dict = dict()
            wr_past = int((unix_now - time1) / 86400)
            wr_future = int((time2 - unix_now) / 86400)
            if unix_now - time1 > 2592000:
                print("\nError4! limited to get history data within last 30 days only!\n")
                return
            if time2 - unix_now > 1296000:
                print("\nError5! limited to get future data within next 15 days only!\n")
                return
            else:
                wr_dict.update(self.getHistory(lat, lon, wr_past, time1))
                wr_dict.update(self.getFutureForecast(lat, lon, wr_future, unix_now))
                return wr_dict

