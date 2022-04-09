import requests
import os


def Medi_news():
    url = "https://newsapi.org/v2/top-headlines?"
    parameters = {
        'q': 'health news',
        'category': 'health',
        'language': 'en',
        'country': 'in',
        'apiKey': 'API-KEY'
    }

    response = requests.get(url, params=parameters)
    response_json = response.json()
    # pprint(response_json)

    for i in response_json['articles']:
        print(str(i['title']), ":", "\n", str(i['description']), "\n")
        print("For More Details", str(i['url']), "\n")


Medi_news()


