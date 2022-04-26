import sqlite3
conn = sqlite3.connect('bmi_info.db')
class BMI_Information_Store:
    def create_table(self):
        curr = conn.cursor()
        curr.execute("""CREATE TABLE IF NOT EXISTS BMI (
                    name text not null,
                     bmi integer NOT NULL,
                     weight integer NOT NULL
                    )""")
        curr.close()
    def retrieve_all_details(self):
        with conn:
            curr = conn.cursor()
            curr.execute("""SELECT * from BMI""")
            items = curr.fetchall()
            curr.close()
            return items
    def retrieve_user_details(self,name):
        with conn:
            curr = conn.cursor()
            curr.execute("SELECT * FROM BMI WHERE name=:name", {'name': name.title()})
            items = curr.fetchall()
            curr.close()
            return items
    def insert_details(self,name,bmi,weight):
        if name is not None and bmi is not None:
            with conn:
                curr = conn.cursor()
                curr.execute("INSERT INTO BMI VALUES (:name, :bmi, :weight)",
                        {'name': name.title(), 'bmi': bmi,"weight": weight})
                curr.close()
    def update_details(self,name,bmi,weight):
        if name is not None and bmi is not None and weight is not None:
            with conn:
                curr = conn.cursor()
                curr.execute("""UPDATE BMI SET bmi = :bmi, weight = :weight
                            WHERE name = :name""",
                          {'name': name.title(), 'bmi': bmi,'weight':weight})
                curr.close()

#
# user=BMI_Information_Store()
# user.create_table()
# print(user.retrieve_all_details())
# print(user.retrieve_user_details('ar'))