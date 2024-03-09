import urllib.request
import urllib.error
import json

class LastFM:
    def __init__(self, user: str):
        self.user = user
        self.api_key = None
        self.top_tracks = None

    def set_apikey(self, api_key: str) -> None:
        self.api_key = api_key

    def load_top_tracks(self) -> None:
        if not self.api_key:
            raise ValueError("API key is not set.")

        url = f"http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={self.user}&api_key={self.api_key}&format=json&limit=5"
        try:
            response = urllib.request.urlopen(url)
            data = json.loads(response.read())
            self.top_tracks = [(track['name'], track['playcount']) for track in data['toptracks']['track']]
        except urllib.error.URLError as e:
            raise ConnectionError("There was an error connecting to the internet or the API URL was incorrect.")
        except urllib.error.HTTPError as e:
            raise ConnectionError(f"HTTP error encountered: {e.code}")
        except json.JSONDecodeError:
            raise ValueError("Error processing JSON data from API.")
        except KeyError:
            raise ValueError("Incomplete or incorrect data received from API.")
        
    def print_top_tracks(self) -> None:
        if not self.top_tracks:
            print("No top tracks available.")
            return
        print("Top Tracks:")
        for i, (track, playcount) in enumerate(self.top_tracks, start=1):
            print(f"{i}. {track} (Playcount: {playcount})")