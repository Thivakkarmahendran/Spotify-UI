from pandas import array
import requests
import json
from requests.exceptions import HTTPError




def fetchLivedata():
    try:
        response = requests.get('https://hs-consumer-api.espncricinfo.com/v1/pages/matches/current?latest=true')
        response.raise_for_status()
        jsonResponse = response.json()
        return jsonResponse
    except HTTPError as http_err:
        print("cricketAPI.fetchLivedata() - HTTP error occurred:{}".format(http_err))
    except Exception as err:
        print("cricketAPI.fetchLivedata() - unexpected error occurred:{}".format(err))



def parseData(data):
    
    interestedGames = []
    
    for game in data["matches"]:
        
        if game["id"] == 104631:  
             
            gameData = {} 
            gameData["liveGame"] = True
            
            gameData["title"] = game["title"]
            gameData["seriesName"] = game["series"]["name"]
            gameData["groundName"] = game["ground"]["smallName"]
            gameData["format"] = game["format"]
            
            gameData["teamA-Name"] = game["teams"][0]["team"]["name"]
            gameData["teamA-NameAbbreviation"] = game["teams"][0]["team"]["abbreviation"]
            gameData["teamA-PrimaryColor"] = game["teams"][0]["team"]["primaryColor"]
            gameData["teamA-Logo"] = "https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_160,q_50/lsci/{}".format(game["teams"][0]["team"]["image"]["url"])
            
            gameData["teamB-Name"] = game["teams"][1]["team"]["name"]
            gameData["teamB-NameAbbreviation"] = game["teams"][1]["team"]["abbreviation"]
            gameData["teamB-PrimaryColor"] = game["teams"][1]["team"]["primaryColor"]
            gameData["teamB-Logo"] = "https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_160,q_50/lsci/{}".format(game["teams"][1]["team"]["image"]["url"])
            
            gameData["statusText"] = game["statusText"]
            
            interestedGames.append(gameData)

    
    
    print(interestedGames)




f = open('API/crikcet/sampleScore.json')
parseData(json.load(f))










