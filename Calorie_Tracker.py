'''
References
https://www.verywellfit.com/how-many-calories-do-i-need-each-day-2506873
https://www.medicinenet.com/how_to_calculate_calorie_deficit_for_weight_loss/article.htm
'''

import sqlite3
import re
from bmI_exercise_tracker import BMI_Information_Store,BMI
import sqlite3

conn = sqlite3.connect('bmi_info.db')
curr = conn.cursor()
class Calorie_Tracker:
    def __init__(self,name,fooditems,lifestyle):
        self.name = name
        self.fooditems = fooditems
        self.lifestyle = lifestyle
        """
        needed to add one  more variable for prompting the user for to loose or maintain weight, By setting this option
        Arista can calculate the total calories for the person per day.
        """
    def load_low_calorie_food(self):
        pass
    def getting_calorie_details(self):
        pass
    def calculate_total_calorie_food(self,weight):
        return round(weight* 2.205*15)
    def process(self):
        self.user = BMI_Information_Store()
        self.user_details = self.user.retrieve_user_details(self.name)
        if self.user_details is None or self.user_details==[]:
            return "First you calculate the bmi then only use this feature :)"
        self.calories_needed=self.calculate_total_calorie_food(self.user_details[-1])


c=Calorie_Tracker('Arjun','chicken curry,3 idli,1 large apple,1 litre of apple juice',2)

print(c.process())
