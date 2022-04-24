import sqlite3

conn=sqlite3.connect('ambulance.db', check_same_thread=False,timeout=1)
curr=conn.cursor()


class Ambulance_Service:
    def create_table(self):
        curr.execute("""
        CREATE TABLE IF NOT EXISTS ambulance_service (
                name_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text not null,
                mobile text not null,
                place text not null
                )
        """)
    def insert_details(self,name,mobile,place):
        with conn:
            # curr.execute("INSERT INTO ambulance_service VALUES (:name,:mobile,:place)",{'name': name, 'mobile': mobile,'place':place})
            curr.execute('INSERT INTO ambulance_service(name, mobile,place) VALUES (?,?,?)',(name,mobile,place))
    def remove_all_details(self):
        with conn:
            curr.execute('''
            DELETE FROM ambulance_service
            ''')

    def update_details(emp,name,mobile,place,id):
        with conn:
            curr.execute("""UPDATE employees SET name = :name,mobile = :mobile,place = :place
                        WHERE id = :id""",
                      {'name': name, 'mobile': mobile, 'place': place,'id':id})
        # curr.close()
    def fetch(self):
        curr.execute("SELECT * FROM ambulance_service")
        items=curr.fetchall()
        return items

user=Ambulance_Service()
user.create_table()
user.insert_details('arjun','+919074774118','Kollam')
print(user.fetch())