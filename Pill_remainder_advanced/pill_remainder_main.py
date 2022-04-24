from pill_remainder_db import Patient
import sys
sys.path.insert(1,'D:\S8_Project\Arista_Heart\Hospital_Booking')

from hospital_booking import email_call_sms
def pill_remainder(*userdetails):
    email_call_sms(*userdetails)

db=Patient()
db.create_table()
while True:
    print('started')
    while db.fetch() == []:
        pass
    items=db.fetch()
    db.remove_all_details()
    print(items)





























# import sqlite3
# conn=sqlite3.connect('pill_remainder.db')
# curr=conn.cursor()
# class Patient:
#     def __init__(self,day,description):
#         self.day=day
#         self.description=description
#     def insert_details(self):
#         with conn:
#             curr.execute("INSERT INTO patient VALUES (:day,:description)",
#                       {'day': self.day, 'description': self.description})
#
# patient=Patient(3,'parestamol 3 day night,omee 2 day noon night')
# patient.insert_details()





