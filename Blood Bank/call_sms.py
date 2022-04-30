import smtplib
from email.message import EmailMessage
import os
from twilio.rest import Client
#creating server
#Gmail

def call_sms(blood_group,name,no_of_units,case,required_date,admitted_hopsital,bleeding_place,bleeding_time,district,contact_number,bystander_name,representative_mobile):
    calls,sms=0,0
    #Calling purpose
    try:
        account_sid =os.environ['hospital_booking_sid']
        auth_token = os.environ['hospital_booking_token']
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            twiml='<Response><Say>There is an emergency for blood details will be forward via sms please check and do the needful</Say></Response>',
            to=representative_mobile,
            from_= '+13605154394'
        )

        print(call.sid)
    except Exception as e:
        calls=1
        print("error from calling part",e)
    #Messaging Purpose

    try:
        account_sid =os.environ['hospital_booking_sid']
        auth_token = os.environ['hospital_booking_token']
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            messaging_service_sid=os.environ['hospital_booking_msid'],
            body=f'''
            🛑 URGENT!!!🛑
            🩸 BLOOD REQUIREMENT🩸
            Blood group  :   {blood_group}
            Name of person : {name}
            No of units :    {no_of_units}
            Case :           {case}
            Required Date :  {required_date}
            Admitted Hospital:{admitted_hopsital}
            Bleeding Place:  {bleeding_place}
            Bleeding  Time : {bleeding_time}
            District:        {district}  
            Contact number:  {contact_number}
            Bystanders Name: {bystander_name} 
                    ''',
            to=representative_mobile
        )
        print(message.sid)
    except Exception as e:
        sms = 1
        print(f"error from messaging part",e)

    if calls ==0 and sms==0:
        return 1
    else:
        return 0
# print(call_sms('O+ve','tony stark','2','heart','24-04-2022','mammen memorial hospital','chengannur','8:00AM',"Alappuzha","9074774118","Arjun",'+919074774118'))






