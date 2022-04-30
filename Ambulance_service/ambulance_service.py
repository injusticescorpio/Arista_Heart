from ambulance_service_db import Ambulance_Service
from call_sms import call_sms1
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
    print(ambulance_driver_details)
    driver_to_be_contacted = []
    for driver in ambulance_driver_details:
        if name.title() != driver[1]:  # checking whether the driver not equal to the actual user
            if distance_btw_two_places(place.title(),driver[-1]) <= 30.0:
                driver_to_be_contacted.append([driver, distance_btw_two_places(place.title(),driver[-1])])
    driver_to_be_contacted = sorted(driver_to_be_contacted, key=lambda x: x[1])
    driver_to_be_contacted_phone = [i[0][2] for i in driver_to_be_contacted]
    booking_successful1 = 0
    for i in driver_to_be_contacted_phone[:5]:
        booking_successful1 += call_sms(name,contact,place,i)
    return f"your ambulance requirement has been sent to {booking_successful1} user successfully"


