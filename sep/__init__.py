import spotipy
import os
from spotipy.oauth2 import SpotifyOAuth

import Himitsu


class Spotify:

    def __init__(self):
        print(os.getcwd())
        invisible = Himitsu.Secrets()
        self.sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=invisible.id(),
                                                            client_secret=invisible.password(),
                                                            redirect_uri="http://localhost:8080",
                                                            scope='playlist-read-private playlist-modify-private playlist-modify-public'))