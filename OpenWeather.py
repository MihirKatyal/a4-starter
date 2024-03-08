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
        