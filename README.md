---------------------
Weather Forecast API
---------------------

- The purpose of this project is getting the weather forecast and historical weather from Apixu API.

- We can get the hourly weather forecast by providing the latitude and longitude of the location, and the Unix Epoch format time range as well.

- The program would fetch the url in order to get the data in query format from Apixu API.

- The program returns a list of temperature in each Unix Epoch format hour between the time range in dictionary form.

## Main idea of the file
* client.py: send a request to the Apixu server to get the weather query 
* forecast.py: generate the query 
* main.py: test the method from forecast.py