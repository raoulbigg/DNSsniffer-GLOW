import requests
import json

def save(site):
	#Increment ints in api
	r = requests.get("https://api.myjson.com/bins/y941o")
	JSON = r.json()
	JSON["site"][site] = int(JSON["site"][site]) + 1
	#Saves to api
	headers = {"Content-Type": "application/json; charset=utf-8"}
	r = requests.put('https://api.myjson.com/bins/y941o', data=json.dumps(JSON), headers=headers)