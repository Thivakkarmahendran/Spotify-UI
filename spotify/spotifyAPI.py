
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth
from credentials import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_SCOPE


class spotifyAPI:

    spotifyApi = None

    def  __init__(self):
        SPOTIFY_TOKEN = util.prompt_for_user_token('mthivakkar', SPOTIFY_SCOPE, client_id=SPOTIFY_CLIENT_ID, client_secret = SPOTIFY_CLIENT_SECRET, redirect_uri='http://127.0.0.1:8080/')
        self.spotifyApi = spotipy.Spotify(auth=SPOTIFY_TOKEN)
        
    def getCurrentMusic(self):
        playback = self.spotifyApi.current_playback()
        return playback
    
    
    


