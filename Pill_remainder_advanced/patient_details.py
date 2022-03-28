import sqlite3
conn=sqlite3.connect('pill_remainder.db')
curr=conn.cursor()

def create_table():
    curr.execute("""CREATE TABLE patient (
                day integer not null,
                 description text NOT NULL
                )""")
def get_all_details():
    while curr.fetchall()==[]:
        curr.execute("SELECT * FROM patient")
    curr.execute("SELECT * FROM patient")
    print(curr.fetchall())
create_table()
get_all_details()
