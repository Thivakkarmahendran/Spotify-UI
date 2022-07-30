import json
from flask import Flask, render_template, request, make_response

from spotify.spotifyAPI import spotifyAPI


app = Flask(__name__)
spotifyApi = None

@app.route('/', methods=['GET'])
def index():
    return render_template('spotify.html')
    
    
@app.route('/spotifyData', methods=['GET','POST'])
def data():
    spotifyData = spotifyApi.getCurrentMusic()
    if spotifyData["playing"] == True:
        response = make_response(json.dumps(spotifyApi.getCurrentMusic()))
        response.content_type = 'application/json'
        return response
    else:
        return ('', 204)


def intializeApp():
    global spotifyApi
    spotifyApi = spotifyAPI()
    spotifyApi.getCurrentMusic()
    


if __name__ == '__main__':
    intializeApp()
    app.run(debug=True)