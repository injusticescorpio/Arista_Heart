import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36'
}
url="https://www.google.co.in/search?q="

class Calorie_Details:
    def __init__(self,query):
        self.query =query
        self.search=url+self.query
    def calorie_info(self):
        page = requests.get(self.search, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        result = None
        try:
            result = soup.find("div", class_='LGOjhe').get_text()
        except:
            try:
                result = soup.find("div", class_='Z0LcW an_fna').get_text()
            except:
                try:
                    result = soup.find("div", class_='IZ6rdc').get_text()
                except:
                    result="Unable to find your result I think there's some problem with your input :) Sorry for that"
        return result
    def nutrition_info(self):
        pass

