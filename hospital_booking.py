import smtplib
from email.message import EmailMessage
import os
import time
from twilio.rest import Client
#creating server
#Gmail

def email_call_sms(name,age,hospital_name,place):
    emails=0
    calls=0
    sms=0
    arista_password =os.environ['arista_password']
    d={
            'lakeshore hospital':['arjunscorpio2000@gmail.com','+919074774118'],
            'mammen memorial hospital':['Shadow23legend@gmail.com','+917025094995'],
            'cherian memorial hospital':['g4c5hh1l@gmail.com','+918921799476']
        }
    hospital_mail_id = d[hospital_name.lower()][0]
    hospital_contact_number = d[hospital_name.lower()][1]
    print(hospital_mail_id)
    print(hospital_contact_number)
    try:


        # Emailing purpose
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('arista.assistant@gmail.com',arista_password)
        email = EmailMessage()
        email['From'] = 'arista.assistant@gmail.com'
        email['To'] = hospital_mail_id
        email['Subject'] = 'Hospital Booking for patient'
        email.set_content(f'Hello {hospital_name}\n There is a booking for a patient \n Name:{name}  \n Age:{age}  \n place: {place} \n Please book this at the earliest \n Yours Faithfully \n Arista \n ')
        server.send_message(email)
    except:
        emails=1
    #Calling purpose
    try:
        account_sid = os.environ['demo1']
        auth_token = os.environ['demo2']
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            twiml='<Response><Say>There is a booking for you please check ur sms or mail.</Say></Response>',
            to=hospital_contact_number,
            from_= '+13097245408'
        )

        print(call.sid)
    except:
        calls=1
    #Messaging Purpose

    try:

        account_sid = os.environ['demo1']
        auth_token = os.environ['demo2']
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            messaging_service_sid=os.environ['demo3'],
            body='hello there is a booking for a patient in this hospital \n Details are \n  Name :' + name + '\n Age :' + age + '\n place :' + place,
            to=hospital_contact_number
        )
        print(message.sid)
    except:
        sms = 1

    if calls ==0 and sms==0 and emails==0:
        return f"Booked successfully in all three modes"
    elif (calls==1 or sms==1) and emails==0 :
        return f"Booked successfully only through mail..Unable to call or sms "
    else:
        return f"Booking Unsuccessful Please try after sometimes.."







