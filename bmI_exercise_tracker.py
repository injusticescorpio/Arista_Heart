
import requests
import os
import webbrowser
import sqlite3

class BMI_Information_Store:
    def __init__(self,name=None,bmi=None,weight=None):
        self.name = name
        self.bmi = bmi
        self.weight =weight
        self.conn = sqlite3.connect('bmi_info.db')
        self.curr = self.conn.cursor()
    def create_table(self):
        self.curr.execute("""CREATE TABLE BMI (
                    name text not null,
                     bmi integer NOT NULL,
                     weight integer NOT NULL
                    )""")
    def retrieve_all_details(self):
        self.curr.execute("""SELECT * from BMI""")
        return self.curr.fetchall()
    def retrieve_user_details(self,name):
        self.curr.execute("SELECT * FROM BMI WHERE name=:name", {'name': name})
        return self.curr.fetchall()
    def insert_details(self):
        if self.name is not None and self.bmi is not None:
            with self.conn:
                self.curr.execute("INSERT INTO BMI VALUES (:name, :bmi, :weight)",
                        {'name': self.name.title(), 'bmi': self.bmi,"weight": self.weight})
    def update_defails(self):
        if self.name is not None and self.bmi is not None:
            with self.conn:
                self.curr.execute("""UPDATE BMI SET bmi = :bmi, weight = :weight
                            WHERE name = :name""",
                          {'name': self.name.title(), 'bmi': self.bmi,'weight':self.weight})
    def check_table_exists(self):
        bmi_table=self.curr.execute(
            """SELECT name FROM sqlite_master WHERE type='table'
            AND name='BMI'; """).fetchall()
        return True if bmi_table!=[] else False


class BMI:
    def __init__(self,name,weight,height):
        self.headers = {
    "X-RapidAPI-Host": "body-mass-index-bmi-calculator.p.rapidapi.com",
    "X-RapidAPI-Key": os.environ['secret_key']
}
        self.weight_details={

            'Underweight':"If your BMI is less than 18.5, then it means that you are underweight. To avoid health complications that may arise due to low levels of body fat, you need to put on more weight. Make sure you get in touch with your doctor or a dietician for professional insight and advice.",
                'Normal Weight':"If you have a BMI that falls in between 18.5 to 22.9, then it means that you have a healthy weight in relation to your height. This is your normal BMI range. When you maintain a healthy level of body fat, it means that you have a much lower risk of developing health complications.",
            'Overweight':"If you have a BMI that falls in between 23.0 to 24.9, it means that you are overweight. In other words, you have a higher than ideal level of body fats considering your height. In such cases, it is important that you lose some amount of weight in order to improve your health. It is recommended that you talk to a doctor or dietician for professional advice.",
            'Obese':"If your BMI is more than 25.0, then it indicates that you are obese, or in other words, heavily overweight. It is far from your ideal BMI and it means that you have way too much body fat in relation to your height, and this can pose serious health risks. It is important that you lose weight for health reasons. Make sure to contact your doctor or dietician for professional advice in such a situation."


        }
        self.name = name
        self.weight = weight
        self.height=height

    def bmi_calculation(self):
        url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/metric"

        querystring = {"weight": self.weight, "height": self.height}
        # os.environ['bmi_calculate_key']

        self.bmi = round(requests.request("GET", url, headers=self.headers, params=querystring).json()['bmi'],1)
        return f"Your BMI is {self.bmi}"

    def weight_category(self):
        url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/weight-category"

        querystring = {"bmi": self.bmi}
        self.weightCategory = requests.request("GET", url, headers=self.headers, params=querystring).json()['weightCategory']
        return [self.weightCategory,self.weight_details[self.weightCategory]]
    def play_video(self,url):
        webbrowser.open(url)
    def play_category(self):
        if self.weightCategory =='Overweight' or self.weightCategory =='Obese':
            self.play_video('https://www.youtube.com/watch?v=H3jJ29oE8Zg')
        elif self.weightCategory == 'Underweight':
            self.play_video('https://www.youtube.com/watch?v=W45EUSMnlpg')
        else:
            self.play_video('https://www.youtube.com/watch?v=K-Ch9kbtLYQ')
    def store_details(self):
        bmi_details = BMI_Information_Store(self.name,self.bmi,self.weight)
        if not bmi_details.check_table_exists():
            bmi_details.create_table()
        if bmi_details.retrieve_user_details(self.name)==[]:
            bmi_details.insert_details()
        else:
            bmi_details.update_defails()
# bmi=BMI('Arjun',80,1.94)
# print(f"bmi of {bmi.name} is {bmi.bmi_calculation()}")
# bmi.store_details()
# bmi1=BMI('Dennis',60,1.78)
# print(f"bmi of {bmi1.name} is {bmi1.bmi_calculation()}")
# bmi1.store_details()
# details=BMI_Information_Store()
# print(details.retrieve_user_details('Arjun'))
# print(details.retrieve_all_details())
# print(bmi.weight_category())
# bmi.play_category()





