
import requests
import os
url = "https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"

def nutrition(query):
	querystring = {"ingr": query}

	headers = {
		"X-RapidAPI-Host": "edamam-edamam-nutrition-analysis.p.rapidapi.com",
		"X-RapidAPI-Key": os.environ['secret_key']
	}

	response = requests.request("GET", url, headers=headers, params=querystring).json()
	print(response)

nutrition('1 large apple')



