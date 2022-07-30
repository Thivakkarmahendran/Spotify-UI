import spotipy
import spotipy.util as util
from credentials import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_SCOPE


class spotifyAPI:

    spotifyApi = None

    def  __init__(self):
        SPOTIFY_TOKEN = util.prompt_for_user_token('mthivakkar', SPOTIFY_SCOPE, client_id=SPOTIFY_CLIENT_ID, client_secret = SPOTIFY_CLIENT_SECRET, redirect_uri='http://127.0.0.1:8080/')
        self.spotifyApi = spotipy.Spotify(auth=SPOTIFY_TOKEN)
        
    def getCurrentMusic(self):
        currentMusic = {}
        
        try:
            playback = self.spotifyApi.current_playback()
            
            if playback != None:
                currentMusic["playing"] = True
                currentMusic["songTitle"] = playback["item"]["album"]["name"]
                currentMusic["songArtist"] = playback["item"]["album"]["artists"][0]["name"]
                currentMusic["songAlbumArt"] = playback["item"]["album"]["images"][0]["url"]
                
            else:
                currentMusic["playing"] = False
        except Exception as e:
            print("spotifyAPI.getCurrentMusic() - An exception occurred: {}".format(str(e)))
            currentMusic["playing"] = False
        
        return currentMusic
    
    
    


