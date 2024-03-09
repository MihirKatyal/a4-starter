from OpenWeather import OpenWeather
from LastFM import LastFM
from WebAPI import WebAPI

def test_api(message: str, apikey: str, webapi: WebAPI):
    webapi.set_apikey(apikey)
    webapi.load_data()
    result = webapi.transclude(message)
    print(result)

if __name__ == "__main__":
    # Replace 'your_openweather_api_key' with your actual OpenWeather API key
    open_weather_api_key = 'your_openweather_api_key'
    # Replace 'your_lastfm_api_key' with your actual LastFM API key
    lastfm_api_key = 'your_lastfm_api_key'
    
    open_weather = OpenWeather()  # Utilizes default parameters
    lastfm = LastFM("default_user")  # You might want to set a default user for testing
    
    # Testing OpenWeather
    test_api("Testing the weather: @weather", open_weather_api_key, open_weather)
    
    # Testing LastFM
    test_api("Testing lastFM: @lastfm", lastfm_api_key, lastfm)
