import sqlite3

conn=sqlite3.connect('blood_bank.db')



class Blood_Bank:
    def create_table(self):
        curr = conn.cursor()
        curr.execute("""
        CREATE TABLE IF NOT EXISTS blood_bank (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name text not null,
                mobile text not null,
                place text not null
                )
        """)
    def insert_details(self,name,mobile,place):
        with conn:
            curr = conn.cursor()
            # curr.execute("INSERT INTO ambulance_service VALUES (:name,:mobile,:place)",{'name': name, 'mobile': mobile,'place':place})
            curr.execute('INSERT INTO blood_bank(name, mobile,place) VALUES (?,?,?)',(name,mobile,place))
            curr.close()
            return f"user created sucessfully with id number {self.fetch()[-1][0]} note this detail for further updation and deletion"
    def remove_all_details(self):
        with conn:
            curr = conn.cursor()
            curr.execute('''
            DELETE FROM blood_bank
            ''')
            curr.close()

    def update_details(emp,name,mobile,place,id):
        try:
            with conn:
                curr = conn.cursor()
                curr.execute("""UPDATE blood_bank SET name = :name,mobile = :mobile,place = :place
                            WHERE id = :id""",
                          {'name': name, 'mobile': mobile, 'place': place,'id':id})
                curr.close()
                return "Updated Successfully"
        except:
            return "No such id available in database"
    def fetch(self):
        with conn:
            curr = conn.cursor()
            curr.execute("SELECT * FROM blood_bank")
            items=curr.fetchall()
            curr.close()
            return items
    def remove_user(self,id):
        with conn:
            curr = conn.cursor()
            curr.execute('''
            DELETE FROM blood_bank WHERE id = :id
            ''',{'id':id})
# user=Blood_Bank()
# user.create_table()
# print(user.insert_details('arjun','+919074774118','Kollam'))
# print(user.insert_details('arj','+919074774118','cgnr'))
# print(user.insert_details('arj','+919074774118','cgnr'))
# print(user.fetch())
# user.update_details('arjun','+919074774118','nepal',3)
# user.remove_user(2)
# print(user.insert_details('arj','+919074774118','cgnr'))
# print(user.fetch())