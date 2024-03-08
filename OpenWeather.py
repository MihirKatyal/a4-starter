import urllib.request
import urllib.error
import json

class OpenWeather:
    def __init__(self, zip_code: str, country_code: str):
        self.zip_code = zip_code
        self.country_code = country_code
        self.apikey = None
        self.temperature = None
        self.high_temperature = None
        self.low_temperature = None
        self.longitude = None
        self.latitude = None
        self.description = None
        self.humidity = None
        self.sunset = None
        self.city = None

    def set_apikey(self, apikey: str) -> None:
        self.apikey = apikey

    def load_data(self) -> None:
        if not self.apikey:
            raise ValueError("API key is not set.")
        
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={self.zip_code},{self.country_code}&appid={self.apikey}&units=metric"
        try:
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
            # Assign data to attributes
            self.temperature = data['main']['temp']
            self.high_temperature = data['main']['temp_max']
            self.low_temperature = data['main']['temp_min']
            self.longitude = data['coord']['lon']
            self.latitude = data['coord']['lat']
            self.description = data['weather'][0]['description']
            self.humidity = data['main']['humidity']
            sunset_time = data['sys']['sunset']
            self.city = data['name']       