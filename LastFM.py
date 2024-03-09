import urllib.request
import urllib.error
import json
from WebAPI import WebAPI

class LastFM(WebAPI):
    def __init__(self, user: str):
        super().__init__()
        self.user = user
        # Initialize attributes to store top tracks data
        self.top_tracks = []

    def load_top_tracks(self):
        url = f"http://ws.audioscrobbler.com/2.0/?method=user.gettoptracks&user={self.user}&api_key={self.api_key}&format=json&limit=5"
        data = self._download_url(url)
        # Processing and storing top tracks data
        self.top_tracks = [(track['name'], track['playcount']) for track in data['toptracks']['track']]

    def transclude(self, message: str) -> str:
        if '@lastfm' in message:
            self.load_top_tracks()  # Ensure data is loaded
            if self.top_tracks:
                top_tracks_str = ', '.join([f"'{name}' (Playcount: {playcount})" for name, playcount in self.top_tracks])
                message = message.replace('@lastfm', f"Top LastFM tracks: {top_tracks_str}")
            else:
                message = message.replace('@lastfm', "No top LastFM tracks available.")
        return message
