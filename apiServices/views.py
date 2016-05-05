from django.shortcuts import render
import requests
import service
import urllib
# Create your views here.
def index(request):
	return render(request,'searchLanding.html')

def spotifyQuery(request):
	print "=====SPOTIFY QUERY ===="
	encodeQuery = urllib.quote(request.POST['artistQuery'])
	spotifyData = service.getSpotifyData(encodeQuery)

	if spotifyData is None:
		return render(request, 'noResult.html')
	else:
		return render(request, 'searchResult.html', spotifyData['artist'])
	