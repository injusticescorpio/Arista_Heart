import smtplib
from email.message import EmailMessage
import os
from twilio.rest import Client


def call_sms1(name,contact,place,ambulance_driver_mobile):
    calls,sms=0,0
    #Calling purpose
    try:
        account_sid =os.environ['hospital_booking_sid']
        auth_token = os.environ['hospital_booking_token']
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            twiml='<Response><Say>There is an emergency for an ambulance service, Details will be forward via sms please check and do the needful</Say></Response>',
            to=ambulance_driver_mobile,
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
                There's an emergency for Ambulance Service, Details of the patient is mentioned below
                patient's name :{name}
                patient's phone number :{contact}
                patient's place : {place}
                 Kindly do the needful
                 Regards
                 ArIsTa
                    ''',
            to=ambulance_driver_mobile
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






