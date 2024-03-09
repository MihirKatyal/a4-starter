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