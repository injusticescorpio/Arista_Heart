from ambulance_service_db import Ambulance_Service
from call_sms import call_sms
import requests
import os
import re
def distance_btw_two_places(place1,place2):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?"
    distanceapi = os.environ['distanceapi']
    response = requests.get(url + 'origins=' + place1 + '&destinations=' + place2 + '&key=' + distanceapi).json()
    res=''
    try:
        res = response['rows'][0]['elements'][0]['distance']['text']
    except Exception as e:
        print(f"error occured {e} and place not available is {place2}")
        return float('inf')
    if 'km' in res:
        return float(''.join([i for i in res if i.isdigit() or i=='.']))
    return float(''.join([i for i in res if i.isdigit() or i=='.']))/1000
def Ambulance_Service_Info(name,contact,place):
    db=Ambulance_Service()
    ambulance_driver_details=db.fetch()



