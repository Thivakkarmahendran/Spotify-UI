import json
import threading

from flask import Flask, render_template, request, make_response, url_for, redirect

from API.spotify.spotifyAPI import spotifyAPI


app = Flask(__name__)
spotifyApi = None
spotifyData = None


# FLASK endpoints:

@app.route('/', methods=['GET'])
def index():
    global spotifyData
    if spotifyData["playing"] == True:
        return redirect('/spotify')
    else:
        return redirect('/clock')


@app.route('/clock', methods=['GET'])
def clock():
    return render_template('clock.html')

@app.route('/spotify', methods=['GET'])
def spotify():
    return render_template('spotify.html')

    
@app.route('/spotifyData', methods=['GET','POST'])
def spotifyData():
    global spotifyData
    response = make_response(json.dumps(spotifyData))
    response.content_type = 'application/json'
    return response


#CORE Code
def checkUpdate():
    threading.Timer(10.0, checkUpdate).start()
    global spotifyData
    spotifyData = spotifyApi.getCurrentMusic()
    



def intializeApp():
    global spotifyApi
    spotifyApi = spotifyAPI()
    checkUpdate()
    


if __name__ == '__main__':
    intializeApp()
    app.run(debug=True)