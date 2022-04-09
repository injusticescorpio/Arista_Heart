import requests
import os

url = "https://newsapi.org/v2/top-headlines?"
parameters = {'q': 'health','category': 'health','language': 'en',
                'country': 'in', 'apiKey': os.environ['news_api']
}

class Medicine_News_Teller:
    def __init__(self):
        self.response = requests.get(url, params=parameters).json()
    def details(self):
        self.seperator='.\n'
        self.news_details =[]
        for details in self.response['articles']:
            self.news_details.append(f"⚫ {details['title']} => \n {self.seperator.join(details['description'].split('.'))} \nFor more Information visit {details['url']}")
        return ('\n'.join(self.news_details))

m=Medicine_News_Teller()
m.details()