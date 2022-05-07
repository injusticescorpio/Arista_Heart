import smtplib
from email.message import EmailMessage
import os
from twilio.rest import Client
def email_call_sms(name,contact_number,email,medicine_name):
    emails,calls,sms,whatsapp=0,0,0,0
    arista_password =os.environ['arista_password']
    d={
            'lakeshore hospital':['arjunscorpio2000@gmail.com','+919074774118'],
            'mammen memorial hospital':['Shadow23legend@gmail.com','+917025094995'],
            'cherian memorial hospital':['g4c5hh1l@gmail.com','+918921799476']
        }
    try:

        # Emailing purpose
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('arista.assistant@gmail.com',arista_password)
        email = EmailMessage()
        email['From'] = 'arista.assistant@gmail.com'
        email['To'] = email
        email['Subject'] = 'Pill remainder'
        email.set_content(f'Hello {name}\n  It\'s time to medicine {medicine_name}\nRegards Arista :)')
        server.send_message(email)
    except Exception as e:
        emails=1
        print("error from emailing part",e)
    #Calling purpose
    try:
        account_sid =os.environ['hospital_booking_sid']
        auth_token = os.environ['hospital_booking_token']
        client = Client(account_sid, auth_token)

        call = client.calls.create(
            twiml='<Response><Say>There is a booking for you please check ur sms or mail.</Say></Response>',
            to=contact_number,
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
            body=f'Hello {name}\n  It\'s time to medicine {medicine_name}\nRegards Arista :)',
            to=contact_number
        )
        print(message.sid)
    except Exception as e:
        sms = 1
        print(f"error from messaging part",e)

    if calls ==0 and sms==0 and emails==0 :
        return f"Booked successfully in all three modes"
    elif (calls==1 and  sms==1)and emails==0 :
        return f"Booked successfully only through mail..Unable to call or send sms "
    elif calls==1 and (sms==0 and emails==0 ):
        return "There is a problem while calling"
    elif sms==1 and (calls==0 and emails==0) :
        return "There is a problem in sending the booked info via sms"
    else:
        return f"Booking Unsuccessful Please try after sometimes.."