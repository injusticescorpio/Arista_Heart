import sqlite3

conn=sqlite3.connect('hospital.db', check_same_thread=False,timeout=1)
curr=conn.cursor()


class Hospital_Booking:
    def create_table(self):
        curr.execute("""
        CREATE TABLE hospital_booking (
                name text,
                age text,
                hospital_name text,
                place text)
        """)
    def insert_details(self,name,age,hospital_name,place):
        with conn:
            curr.execute("INSERT INTO hospital_booking VALUES (:name,:age,:hospital_name,:place)",
                      {'name': name, 'age': age,'hospital_name':hospital_name,'place':place})
    def remove_all_details(self):
        curr.execute('''
        DELETE FROM hospital_booking
        ''')
        # curr.close()
    def fetch(self):
        curr.execute("SELECT * FROM hospital_booking")
        items=curr.fetchall()
        return items
#
# userdata=Hospital_Booking()
# userdata.create_table()
# userdata.insert_details('arju',20,'lakeshore','cgnr')
# userdata.insert_details('mikku',28,'lakeshore','thiruvala')
# print(userdata.fetch())
# userdata.remove_all_details()
# print(userdata.fetch())
# userdata.insert_details('dennis',28,'lakeshore','thiruvala')
# print(userdata.fetch())
