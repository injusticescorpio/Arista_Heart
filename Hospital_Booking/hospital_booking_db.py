import sqlite3

conn=sqlite3.connect('hospital.db')
# curr=conn.cursor()


class Hospital_Booking:
    def create_table(self):
        curr=conn.cursor()
        curr.execute("""
        CREATE TABLE  IF NOT EXISTS hospital_booking (
                name text,
                age text,
                hospital_name text,
                place text)
        """)
        curr.close()
    def insert_details(self,name,age,hospital_name,place):
        with conn:
            curr = conn.cursor()
            curr.execute("INSERT INTO hospital_booking VALUES (:name,:age,:hospital_name,:place)",
                      {'name': name, 'age': age,'hospital_name':hospital_name,'place':place})
            curr.close()
    def remove_all_details(self):
        curr = conn.cursor()
        curr.execute('''
        DELETE FROM hospital_booking
        ''')
        curr.close()
    def fetch(self):
        with conn:
            curr = conn.cursor()
            curr.execute("SELECT * FROM hospital_booking")
            items=curr.fetchall()
            curr.close()
            return items

# userdata=Hospital_Booking()
# userdata.create_table()
# userdata.insert_details('arju',20,'lakeshore','cgnr')
# userdata.insert_details('mikku',28,'lakeshore','thiruvala')
# print(userdata.fetch())
# userdata.remove_all_details()
# print(userdata.fetch())
# userdata.insert_details('dennis',28,'lakeshore','thiruvala')
# print(userdata.fetch())
# d=Hospital_Booking()
# d.create_table()
# print("started")
# while True:
#     while d.fetch()==[]:
#         pass
#     print(d.fetch())
#     d.remove_all_details()