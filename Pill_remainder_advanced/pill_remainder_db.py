import sqlite3

conn=sqlite3.connect('pill_remainder.db')

class Patient:
    def create_table(self):
        curr = conn.cursor()
        curr.execute("""CREATE TABLE IF NOT EXISTS patient (
                    day integer not null,
                    name text not null,
                    contact text not null,
                    email text not null,
                     description text NOT NULL
                    )""")
        curr.close()
    def insert_details(self,day,name,contact,email,description):
        with conn:
            curr = conn.cursor()
            curr.execute("INSERT INTO patient VALUES (:day,:name,:contact,:email,:description)",
                     {'day': day,'name':name,'contact':contact,'email':email, 'description': description})
            curr.close()

    def fetch(self):
        with conn:
            curr = conn.cursor()
            curr.execute("SELECT * FROM patient")
            items = curr.fetchall()
            curr.close()
            return items
    def remove_all_details(self):
        curr = conn.cursor()
        curr.execute('''
        DELETE FROM patient
        ''')
        curr.close()


