import requests

GOOGLE_MAPS_API_URL = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyBUj_H7Bp6sel10RKaSJm8DQop5NoH1-WE'

params = {'wifiAccessPoints':[{'macAddress':'fc:c2:de:3c:4f:8f'}]}

# Do the request and get the response data
req = requests.post(GOOGLE_MAPS_API_URL, params=params)
res = req.json()

location = 'lat:'+str(res['location']['lat'])+' lng:'+str(res['location']['lng'])
print (location)