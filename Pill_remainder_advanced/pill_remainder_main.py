from pill_remainder_db import Patient
import sys
from datetime import date,timedelta
sys.path.insert(1,'D:\S8_Project\Arista_Heart\Hospital_Booking')
from hospital_booking import email_call_sms
from apscheduler.schedulers.background import BackgroundScheduler

# Creates a default Background Scheduler
sched = BackgroundScheduler()
def pill_remainder(*userdetails):
    print(userdetails)

db=Patient()
db.create_table()
sched.start()
while True:
    print('started')
    while db.fetch() == []:
        pass
    number_of_medicine,name,contact_number,email_id,description=db.fetch()[-1]
    db.remove_all_details()
    for medicine_details in description.split(','):
        medicine_full_details=medicine_details.split(' ')
        medicine_name, medicine_taking_duration,*medicine_timings=medicine_full_details
        medicine_taking_time=int(medicine_taking_duration)
        reminder_start_date=date.today()
        reminder_end_date=reminder_start_date+timedelta(medicine_taking_time)
        print(medicine_name,medicine_timings,reminder_start_date,reminder_end_date,contact_number,name,email_id)
        if len(medicine_timings)==3:
            sched.add_job(pill_remainder, 'cron',start_date=reminder_start_date  ,hour=8,
                          end_date=reminder_end_date,
                          args=[name,email_id,medicine_name])
            sched.add_job(pill_remainder, 'cron',start_date=reminder_start_date  ,hour=14,minute=53,
                          end_date=reminder_end_date,
                          args=[name,contact_number,email_id,medicine_name])
            sched.add_job(pill_remainder, 'cron',start_date=reminder_start_date  ,hour=20,minute=30,
                          end_date=reminder_end_date,
                          args=[name,contact_number,email_id,medicine_name])
        elif 'day' in medicine_timings and 'noon' in medicine_timings:
            sched.add_job(pill_remainder, 'cron',start_date=reminder_start_date  ,hour=8,
                          end_date=reminder_end_date,
                          args=[name,contact_number,email_id,medicine_name])
            sched.add_job(pill_remainder, 'cron',start_date=reminder_start_date  ,hour=12,minute=30,
                          end_date=reminder_end_date,
                          args=[name,contact_number,email_id,medicine_name])
        elif 'day' in medicine_timings and 'night' in medicine_timings:
            sched.add_job(pill_remainder, 'cron', start_date=reminder_start_date, hour=8,
                          end_date=reminder_end_date,
                          args=[name,contact_number,email_id,medicine_name])
            sched.add_job(pill_remainder, 'cron', start_date=reminder_start_date, hour=20, minute=30,
                          end_date=reminder_end_date,
                          args=[name,contact_number,email_id,medicine_name])
        elif 'noon' in medicine_timings and 'night' in medicine_timings:
            sched.add_job(pill_remainder, 'cron',start_date=reminder_start_date  ,hour=12,minute=30,
                          end_date=reminder_end_date,
                          args=[name,contact_number,email_id,medicine_name])
            sched.add_job(pill_remainder, 'cron',start_date=reminder_start_date  ,hour=20,minute=30,
                          end_date=reminder_end_date,
                          args=[name,contact_number,email_id,medicine_name])
        elif len(medicine_timings)==1 and 'day' in medicine_timings:
            sched.add_job(pill_remainder, 'cron', start_date=reminder_start_date, hour=8,
                          end_date=reminder_end_date,
                          args=[name,contact_number,email_id,medicine_name])
        elif len(medicine_timings) == 1 and 'noon' in medicine_timings:
            sched.add_job(pill_remainder, 'cron', start_date=reminder_start_date, hour=12, minute=30,
                          end_date=reminder_end_date,
                          args=[name,contact_number,email_id,medicine_name])
        elif len(medicine_timings) == 1 and 'night' in medicine_timings:
            sched.add_job(pill_remainder, 'cron', start_date=reminder_start_date, hour=20, minute=30,
                          end_date=reminder_end_date,
                          args=[name,contact_number,email_id,medicine_name])
        else:
            print("invalid entry from user part")

    print("Schedulting set successfully")




































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





