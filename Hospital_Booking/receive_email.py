# imap supports polish notations

from datetime import datetime,timedelta
from hospital_booking import email_call_sms
from hospital_booking_db import Hospital_Booking
import os
import email
import imaplib
current_date_time_info = datetime.now()
current_date = str(current_date_time_info.strftime("%d-%b-%Y"))
print(current_date)
# db=Hospital_Booking()
# db.create_table()
# print('started')
# while db.fetch()==[]:
#     db.fetch()
# items=db.fetch()
# print(items)
# current_time = datetime.now()
# future_time = current_time + timedelta(minutes=2)
# current_time=current_time.strftime("%H:%M")
# future_time=future_time.strftime("%H:%M")
# while current_time<=future_time:
#     current_time = datetime.now()
#     current_time=current_time.strftime("%H:%M")

arista_password =os.environ['arista_password']
EMAIL = 'arista.assistant@gmail.com'
PASSWORD = arista_password
SERVER = 'imap.gmail.com'




# connect to the server and go to its inbox
mail = imaplib.IMAP4_SSL(SERVER)
mail.login(EMAIL, PASSWORD)
# we choose the inbox but you can select others
mail.select('inbox')

# we'll search using the ALL criteria to retrieve
# every message inside the inbox
# it will return with its status and a list of ids
status, data = mail.search(None,f'(ON "{current_date}"(OR SUBJECT "Hospital Booking For Patient" TEXT "hospital booking available"))')
# the list returned is a list of bytes separated
# by white spaces on this format: [b'1 2 3', b'4 5 6']
# so, to separate it first we create an empty list
mail_ids = []
# then we go through the list splitting its blocks
# of bytes and appending to the mail_ids list
for block in data:
    # the split function called without parameter
    # transforms the text or bytes into a list using
    # as separator the white spaces:
    # b'1 2 3'.split() => [b'1', b'2', b'3']
    mail_ids += block.split()

# now for every id we'll fetch the email
# to extract its content
for i in mail_ids:
    # the fetch function fetch the email given its id
    # and format that you want the message to be
    status, data = mail.fetch(i, '(RFC822)')

    # the content data at the '(RFC822)' format comes on
    # a list with a tuple with header, content, and the closing
    # byte b')'
    for response_part in data:
        # so if its a tuple...
        if isinstance(response_part, tuple):
            # we go for the content at its second element
            # skipping the header at the first and the closing
            # at the third
            message = email.message_from_bytes(response_part[1])

            # with the content we can extract the info about
            # who sent the message and its subject
            mail_from = message['from']
            mail_subject = message['subject']

            # then for the text we have a little more work to do
            # because it can be in plain text or multipart
            # if its not plain text we need to separate the message
            # from its annexes to get the text
            if message.is_multipart():
                mail_content = ''

                # on multipart we have the text message and
                # another things like annex, and html version
                # of the message, in that case we loop through
                # the email payload
                for part in message.get_payload():
                    # if the content type is text/plain
                    # we extract it
                    if part.get_content_type() == 'text/plain':
                        mail_content += part.get_payload()
            else:
                # if the message isn't multipart, just extract it
                mail_content = message.get_payload()

            # and then let's show its result
            print(f'From: {mail_from}')
            print(f'Subject: {mail_subject}')
            print(f'Content: {mail_content}')
            possible_yes,possible_no = ['yes', 'yep', 'yass', 'yes available'],['no','nope','not','sorry not available','sorry']