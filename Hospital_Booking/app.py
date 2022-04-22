import os
from hospital_booking import email_call_sms
from hospital_booking_db import Hospital_Booking
from datetime import datetime,timedelta
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import sqlite3
db=Hospital_Booking()
db.create_table()
app = Flask(__name__)
account_sid = os.environ['demo1']
auth_token = os.environ['demo2']
client = Client(account_sid, auth_token)

def respond(message):
    response = MessagingResponse()
    response.message(message)
    return str(response)

@app.route('/message', methods=['POST'])
def reply():
    message = request.form.get('Body').lower()
    if message:
        user_data = db.fetch()
        print(f"user_data=={user_data}")
        db.remove_all_details()
        return respond(email_call_sms(*user_data[0]))
