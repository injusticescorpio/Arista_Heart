import requests
import json
response=requests.get('https://api.covid19india.org/state_district_wise.json').json()
kerala_details=response['Kerala']
# print(kerala_details)

class Covid_19():
    def __init__(self,district):
        self.district=district
    def covid_19_details_total(self):
        for i in kerala_details['districtData'].items():
            if i[0]==self.district.title():
                return(f"{self.district} Details so far\nActive cases:   {i[1]['active']}\nConfirmed Cases:{i[1]['confirmed']}\nDecreased by:{i[1]['deceased']}\nRecovered by:{i[1]['recovered']}")
        return('No such districts in kerala!Check whether your spellings are correct')    

    def covid_19_details_current(self):
        for i in kerala_details['districtData'].items():
            if i[0]==self.district.title():
                return(f"{self.district} todays details so far\nConfirmed Cases:{i[1]['delta']['confirmed']}\nDeceased by:{i[1]['deceased']}\nRecovered by:{i[1]['delta']['recovered']}")
        return('No such districts in kerala!Check whether your spellings are correct')
    
    def total_covid_19(self):   
        total_confirmed=0
        total_recovered=0
        total_death=0
        for i in kerala_details['districtData'].items():
            total_confirmed+=i[1]['delta']['confirmed']
            total_recovered+=i[1]['delta']['recovered']
            total_death+=i[1]['delta']['deceased']
        if(total_confirmed==0 and total_recovered==0 and total_death==0):
            return ("Sorry I didn't get the information yet! Please Try after sometime ")
        return (f"Kerala's Total confirmed cases of Today:  {total_confirmed}\n Kerala's Total recovered cases of Today:  {total_recovered}\n Kerala's Total death cases of Today: {total_death}")
    def kerala_total(self):
        total_confirmed = 0
        total_death = 0
        total_recovered = 0
        total_active = 0
        for i in kerala_details['districtData'].items():
            if i[0] not in ['Other State', 'Unknown']:
                total_confirmed += i[1]['confirmed']
                total_recovered += i[1]['recovered']
                total_death += i[1]['deceased']
                total_active += i[1]['active']
        return(f"Kerala Full details\n Total Confirmed: {total_confirmed} \n Total Recovered: {total_recovered}  \n Total Death: {total_death}  \n Currently Active: {total_active}")



# place=Covid_19('kannur')
# print(place.covid_19_details_current())
# print(place.covid_19_details_total())
# print(place.total_covid_19())
# print(place.kerala_total())
