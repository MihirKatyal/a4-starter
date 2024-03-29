#Mihir Katyal
#mkatyal@uci.edu
#19099879

from OpenWeather import OpenWeather

def main():
    zipcode = "92697"
    ccode = "US"
    apikey = "6aff17baf0c23f582c0d2028522c3d03"  
    
    open_weather = OpenWeather(zipcode, ccode)
    open_weather.set_apikey(apikey)
    try:
        open_weather.load_data()
        print(f"The temperature for {zipcode} is {open_weather.temperature} degrees")
        print(f"The high for today in {zipcode} will be {open_weather.high_temperature} degrees")
        print(f"The low for today in {zipcode} will be {open_weather.low_temperature} degrees")
        print(f"The coordinates for {zipcode} are {open_weather.longitude} longitude and {open_weather.latitude} latitude")
        print(f"The current weather for {zipcode} is {open_weather.description}")
        print(f"The current humidity for {zipcode} is {open_weather.humidity}")
        print(f"The sun will set in {open_weather.city} at {open_weather.sunset}")
    except ConnectionError as e:
        print(f"Error: {str(e)}")
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == '__main__':
    main()