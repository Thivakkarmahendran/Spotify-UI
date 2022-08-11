import json
import threading

from flask import Flask, render_template, request, make_response, url_for, redirect

from API.spotify.spotifyAPI import spotifyAPI
from API.crikcet import cricketAPI


app = Flask(__name__)
spotifyApi = None

spotifyData = None
cricketData = None


# FLASK endpoints:

@app.route('/', methods=['GET'])
def index():
    global spotifyData, cricketData
    
    if cricketData["liveGame"] == True:
       return redirect('/cricket') 
    elif spotifyData["playing"] == True:
        return redirect('/spotify')
    else:
        return redirect('/clock')


@app.route('/clock', methods=['GET'])
def clock():
    return render_template('clock.html')

@app.route('/cricket', methods=['GET'])
def cricket():
    return render_template('cricket.html')

@app.route('/spotify', methods=['GET'])
def spotify():
    return render_template('spotify.html')

    
@app.route('/spotifyData', methods=['GET','POST'])
def spotifyData():
    global spotifyData
    response = make_response(json.dumps(spotifyData))
    response.content_type = 'application/json'
    return response

@app.route('/cricketData', methods=['GET','POST'])
def cricketData():
    global cricketData
    response = make_response(json.dumps(cricketData))
    response.content_type = 'application/json'
    return response



@app.route('/checkSwitch', methods=['GET'])
def checkSwitch():
    global cricketData, spotifyData
    
    if cricketData["liveGame"] == True:
        response = make_response(json.dumps("cricket"))
        response.content_type = 'application/json'
        return response
    elif spotifyData["playing"] == True:
        response = make_response(json.dumps("spotify"))
        response.content_type = 'application/json'
        return response
    else:
        response = make_response(json.dumps("clock"))
        response.content_type = 'application/json'
        return response
    

#CORE Code
def checkUpdate():
    threading.Timer(10.0, checkUpdate).start()
    global spotifyData, cricketData
    spotifyData = spotifyApi.getCurrentMusic()
    cricketData = cricketAPI.updateCricketData()
    
    

def intializeApp():
    global spotifyApi
    spotifyApi = spotifyAPI()
    checkUpdate()
    


if __name__ == '__main__':
    intializeApp()
    app.run(debug=True)