import requests
import os
url = "https://edamam-edamam-nutrition-analysis.p.rapidapi.com/api/nutrition-data"
headers = {
	"X-RapidAPI-Host": "edamam-edamam-nutrition-analysis.p.rapidapi.com",
	"X-RapidAPI-Key": os.environ['secret_key']
}

class Nutrition_Info:
	def __init__(self,query):
		self.query =query
		querystring = {"ingr": query}
		self.response = requests.request("GET", url, headers=headers, params=querystring).json()
	def calorie_information(self):
		return str(self.response['calories'])+" cal"
	def nutrition_info(self):
		info1=f"Diet Labels --> {' '.join(self.response['dietLabels'])}\nHealthy Labels --> {' '.join(self.response['healthLabels'])[:5]}\nForMore Inormation :)"

		info2=''
		for i in self.response['totalNutrients']:
			each_info=f"{self.response['totalNutrients'][i]['label']} : {self.response['totalNutrients'][i]['quantity']}{self.response['totalNutrients'][i]['unit']}\n"
			info2+=each_info
		info1+=info2 if info2!='' else "\nUnable to find more information"
		return info1
# nutrition=Nutrition_Info('1 large apple')
#
# print(nutrition.calorie_information())
# print(nutrition.nutrition_info())

