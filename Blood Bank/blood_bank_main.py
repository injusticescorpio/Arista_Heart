from bloodbank_db import Blood_Bank
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

def Blood_Bank_details(blood_group,name,no_of_units,case,required_date,admitted_hopsital,bleeding_place,bleeding_time,district,contact_number,bystander_name):
    db=Blood_Bank()
    blood_bank_user_details=db.fetch()
    print(blood_bank_user_details)
    representative_to_be_contacted=[]
    for representative in blood_bank_user_details:
        if name.title()!=representative[1]:#checking whether the representative
            if distance_btw_two_places(bleeding_place.title(),representative[-1])<=30.0:
                representative_to_be_contacted.append([representative,distance_btw_two_places(bleeding_place,representative[-1])])
    representative_to_be_contacted=sorted(representative_to_be_contacted,key=lambda x:x[1])
    representative_to_be_contacted_phone=[i[0][2] for i in representative_to_be_contacted]
    booking_successful=0
    for i in representative_to_be_contacted_phone[:5]:
        booking_successful+=call_sms(blood_group,name,no_of_units,case,required_date,admitted_hopsital,bleeding_place,bleeding_time,district,contact_number,bystander_name,i)
    return f"your blood requirement has been sent to {booking_successful} user successfully"




    
print(Blood_Bank_details('O+ve','tony stark','2','heart','24-04-2022','mammen memorial hospital','chengannur','8:00AM',"Alappuzha","9074774118","Arjun"))

# print(distance_btw_two_places('Chengannur','kallissery,kerala'))