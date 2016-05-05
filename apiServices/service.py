import requests
import json
def getSpotifyData(artist):

	#Construct query for Spotify
	getUrl = "https://api.spotify.com/v1/search?q="+artist+"&type=artist"
	#Send request and load as JSON
	data = requests.get(getUrl)
	jsonData = json.loads(data.text)

	if not jsonData['artists']['items']:
		return None;
	else:
		data = {'artist':jsonData['artists']['items'][0]}
		return data
	#Accessing the first artist in results list
	#(ordered by ascending popularity)
	#Create new object with first result
	data = {'artist':jsonData['artists']['items'][0]}
	return data