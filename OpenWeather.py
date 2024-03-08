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
            # Convert UNIX timestamp to readable format if necessary
            # For simplicity, here it's left as UNIX timestamp
            self.sunset = sunset_time
        except urllib.error.URLError as e:
            raise ConnectionError("There was an error connecting to the internet or the API URL was incorrect.")
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise ConnectionError("Requested data not found (404 error).")
            elif e.code == 503:
                raise ConnectionError("Service unavailable (503 error).")
            else:
                raise ConnectionError(f"HTTP error encountered: {e.code}")
        except json.JSONDecodeError:
            raise ValueError("Error processing JSON data from API.")
        except KeyError:
            raise ValueError("Incomplete or incorrect data received from API.")