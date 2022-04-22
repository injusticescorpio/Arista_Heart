import sqlite3

conn=sqlite3.connect('hospital.db', check_same_thread=False)

curr=conn.cursor()


class Hospital_Booking:
    def __init__(self,name=None,age=None,hospital_name=None,place=None):
        self.name = name
        self.age=age
        self.hospital_name =hospital_name
        self.place = place
    def create_table(self):
        curr.execute("""
        CREATE TABLE hospital_booking (
                name text,
                age text,
                hospital_name text,
                place text)
        """)
    def insert_details(self):
        with conn:
            curr.execute("INSERT INTO hospital_booking VALUES (:name,:age,:hospital_name,:place)",
                      {'name': self.name, 'age': self.age,'hospital_name':self.hospital_name,'place':self.place})

    def remove_all_details(self):
        curr.execute('''
        DELETE FROM hospital_booking
        ''')
    def fetch(self):
        curr.execute("SELECT * FROM hospital_booking")
        return curr.fetchall()

# userdata=Hospital_Booking('arju',20,'lakeshore','cgnr')
# userdata.create_table()
# userdata.insert_details()
# userdata.fetch()
# userdata.remove_all_details()
# userdata.fetch()
