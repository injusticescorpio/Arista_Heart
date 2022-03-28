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
    '''
    here we can call the pill remainder class and this python file runs according to the condition provided by the user 
    to set the pills so he/she will get reminder either by an sms or by a call or by a whatsapp message.
    so all together total 2 server + 2 python file (1 for pill_remainder and 1 for ambulanceService) needed to run for its complete operation
    '''
create_table()
get_all_details()
