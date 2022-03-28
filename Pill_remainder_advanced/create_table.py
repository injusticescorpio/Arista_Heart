import sqlite3
conn=sqlite3.connect('pill_remainder.db')
curr=conn.cursor()
class Patient:
    def __init__(self,day,description):
        self.day=day
        self.description=description
    def insert_details(self):
        with conn:
            curr.execute("INSERT INTO patient VALUES (:day,:description)",
                      {'day': self.day, 'description': self.description})

patient=Patient(3,'parestamol 3 day night,omee 2 day noon night')
patient.insert_details()





