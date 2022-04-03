'''
References
https://www.verywellfit.com/how-many-calories-do-i-need-each-day-2506873
https://www.medicinenet.com/how_to_calculate_calorie_deficit_for_weight_loss/article.htm
'''

from bmI_exercise_tracker import BMI_Information_Store
from Calorie_details import Calorie_Details
import sqlite3


conn = sqlite3.connect('bmi_info.db')
curr = conn.cursor()
class Calorie_Tracker:
    def __init__(self,name,fooditems,lifestyle,weight_info):
        self.name = name
        self.fooditems = fooditems
        self.lifestyle = lifestyle
        self.weight_info=weight_info
    def calories_details_extractor(self,calories_details):
        self.calories = calories_details.lower().split(' ')
        print(self.calories)
        prev = 0
        for i in range(len(self.calories)):
            if 'calories' in self.calories[i].lower() or "cal" in self.calories[i].lower() or "cals" in self.calories[i].lower():
                prev = i - 1
                if self.calories[prev].isdigit():
                    return int(self.calories[prev])
    def load_low_calorie_food(self):
        pass
    def getting_calorie_details(self,calories,weight_info):
        if 'reduce' in weight_info:
            if self.lifestyle==1 or self.lifestyle==2:
                calories-=500
            elif self.lifestyle==3 or self.lifestyle==4:
                calories-=400
            elif self.lifestyle==5:
                calories-=300
            return calories if self.lifestyle in [1,2,3,4,5] else None
        elif 'maintain' in weight_info:
            return calories
        else:
            return None
    def calculate_total_calorie_food(self,weight):
        return int(round(float(weight)* 2.205*15.0))
    def process(self):
        self.user = BMI_Information_Store()
        self.user_details = self.user.retrieve_user_details(self.name)
        if self.user_details is None or self.user_details==[]:
            return "First you calculate the bmi then only use this feature :)"

        self.calories_needed=self.getting_calorie_details(self.calculate_total_calorie_food(self.user_details[0][-1]),self.weight_info)
        if self.calories_needed is None:
            return "Invalid option provided please provide correct option"
        '''
        calories calculation steps
        '''
        self.calories_user_entered=0
        for food in self.fooditems.split(","):
            c=Calorie_Details(food)
            food_calories=self.calories_details_extractor(c.calorie_info())
            print(f"food_calories=={food_calories}")
            if food_calories is None:
                return f"""Sorry I don't have any idea about the {food} food item.
                Please try again :)
                """
            self.calories_user_entered+=food_calories
        if self.calories_user_entered<self.calories_needed:
            pass


c=Calorie_Tracker('Arjun','chicken curry,3 idli,1 large apple,1 litre of apple juice',3,'reduce weight')

print(c.process())
