'''
References
inorder to sent whatsapp message refer the twilio its easy and pretty straight forward
https://www.twilio.com/docs/whatsapp/api

Inorder to receive message via whatsapp
 refer
https://www.twilio.com/blog/receive-whatsapp-messages-python-flask-twilio

'''

import os
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
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
        return respond("req accepted")