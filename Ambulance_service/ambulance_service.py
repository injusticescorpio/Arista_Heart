from ambulance_service_db import Ambulance_Service
import sys
sys.path.insert(1,'D:\S8_Project\Arista_Heart\Hospital_Booking')

from hospital_booking import email_call_sms

def pill_remainder(*userdetails):
    email_call_sms(*userdetails)
db=Ambulance_Service()
db.create_table()