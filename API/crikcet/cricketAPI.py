from pandas import array
import requests
import json
from requests.exceptions import HTTPError



def updateCricketData():
    try:
        #response = requests.get('https://hs-consumer-api.espncricinfo.com/v1/pages/matches/current?latest=true')
        #response.raise_for_status()
        #jsonResponse = response.json()
        
        f = open('API/crikcet/sampleScore1.json')
        jsonResponse = json.load(f)
            
        return parseData(jsonResponse)
    
    except HTTPError as http_err:
        print("cricketAPI.fetchLivedata() - HTTP error occurred:{}".format(http_err))
        gameData = {} 
        gameData["liveGame"] = False
        return gameData
        
    except Exception as err:
        print("cricketAPI.fetchLivedata() - unexpected error occurred:{}".format(err))
        gameData = {} 
        gameData["liveGame"] = False
        return gameData


def isInterestedGame(game):
    
    interestedTeams = ["IND", "SA"]
    interestedSeries = ["IPL", "T20 World Cup"]
    
    if game["status"] != "Live":
        return False
    
    if game["stage"] != "RUNNING":
        return False
    
    if game["series"]["alternateName"] in interestedSeries:
        return True
    
    if game["teams"][0]["team"]["abbreviation"] not in interestedTeams and game["teams"][1]["team"]["abbreviation"] not in interestedTeams:
        return False
    
    
    return True


def parseData(data):
    
    interestedGames = []
    
    for game in data["matches"]:
        
        if isInterestedGame(game):  
             
            gameData = {} 
            gameData["liveGame"] = True
            
            gameData["title"] = game["title"]
            
            gameData["seriesName"] = game["series"]["name"]
            gameData["seriesNameAbbreviation"] = game["series"]["alternateName"]
            gameData["groundName"] = game["ground"]["smallName"]
            gameData["format"] = game["format"]
            
            gameData["teamAName"] = game["teams"][0]["team"]["name"]
            gameData["teamANameAbbreviation"] = game["teams"][0]["team"]["abbreviation"]
            gameData["teamAPrimaryColor"] = game["teams"][0]["team"]["primaryColor"]
            gameData["teamALogo"] = "https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_160,q_50/lsci/{}".format(game["teams"][0]["team"]["image"]["url"])
            gameData["teamAScore"] = game["teams"][0]["score"]
            gameData["teamAscoreInfo"] = game["teams"][0]["scoreInfo"]
            
            
            
            gameData["teamBName"] = game["teams"][1]["team"]["name"]
            gameData["teamBNameAbbreviation"] = game["teams"][1]["team"]["abbreviation"]
            gameData["teamBPrimaryColor"] = game["teams"][1]["team"]["primaryColor"]
            gameData["teamBLogo"] = "https://img1.hscicdn.com/image/upload/f_auto,t_ds_square_w_160,q_50/lsci/{}".format(game["teams"][1]["team"]["image"]["url"])
            gameData["teamBScore"] = game["teams"][1]["score"]
            gameData["teamBscoreInfo"] = game["teams"][1]["scoreInfo"]
            
            gameData["statusText"] = game["statusText"]
            
            interestedGames.append(gameData)

    if(len(interestedGames) == 0):
        gameData = {} 
        gameData["liveGame"] = False
        return gameData
    
    return interestedGames[0]











