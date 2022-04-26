'''
References
https://www.verywellfit.com/how-many-calories-do-i-need-each-day-2506873
https://www.medicinenet.com/how_to_calculate_calorie_deficit_for_weight_loss/article.htm
'''

from BMI_db import BMI_Information_Store
from Calorie_details import Calorie_Details
import sqlite3
import json
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
        with open('lowcalorie.json') as json_file:
            data = json.load(json_file)
            json_file.close()
        self.juice = data['juice']
        self.soup = data['Soup']
        self.dishes_meals=data['dishes-meals']
        self.nuts_seeds=data['nuts-seeds']
        self.ice_cream=data['ice-cream']

        self.juice = sorted(self.juice.items(), key=lambda x: x[1]['Calories'])
        self.soup = sorted(self.soup.items(), key=lambda x: x[1]['Calories'])
        self.dishes_meals=sorted(self.dishes_meals.items(), key=lambda x: x[1]['Calories'])
        self.nuts_seeds=sorted(self.nuts_seeds.items(), key=lambda x: x[1]['Calories'])
        self.ice_cream=sorted(self.ice_cream.items(), key=lambda x: x[1]['Calories'])
        print(f"juice=={self.juice}")
        print(f"soup=={self.soup}")
        print(f"dishes_meals=={self.dishes_meals}")
        print(f"nuts_seeds=={self.nuts_seeds}")
        print(f"ice_cream=={self.ice_cream}")
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
            if food_calories is None:
                return f"""Sorry I don't have any idea about the {food} food item.
                Please try again :)
                """
            self.calories_user_entered+=food_calories
        print(f"calories from user is {self.calories_user_entered}")
        print(f"calories need :{self.calories_needed}")
        if self.calories_user_entered<self.calories_needed:
            self.load_low_calorie_food()
            remaining_calories=self.calories_needed-self.calories_user_entered
            remaining_food_items=[]
            juice1=soup1=dishes_meals1=nuts_seeds1=ice_cream1=0
            while remaining_calories>0 and (soup1<len(self.soup) or juice1<len(self.juice)):
                if soup1<len(self.soup) and (remaining_calories-self.soup[soup1][1]['Calories'])>=0:
                    remaining_calories-=self.soup[soup1][1]['Calories']
                    remaining_food_items.append(f"{self.soup[soup1][0]} having calories {self.soup[soup1][1]['Calories']} {self.soup[soup1][1]['unit']} and quantity {self.soup[soup1][1]['quantity']}")
                    soup1+=1
                if juice1<len(self.juice) and (remaining_calories- self.juice[juice1][1]['Calories'])>=0:
                    remaining_calories -= self.juice[juice1][1]['Calories']
                    remaining_food_items.append(f"{self.juice[juice1][0]} having calories {self.juice[juice1][1]['Calories']} {self.juice[juice1][1]['unit']} and quantity {self.juice[juice1][1]['quantity']}")
                    juice1+=1
                if dishes_meals1<len(self.dishes_meals) and (remaining_calories-self.dishes_meals[dishes_meals1][1]['Calories'])>=0:
                    remaining_calories-=self.dishes_meals[dishes_meals1][1]['Calories']
                    remaining_food_items.append(f"{self.dishes_meals[dishes_meals1][0]} having calories {self.dishes_meals[dishes_meals1][1]['Calories']} {self.dishes_meals[dishes_meals1][1]['unit']} and quantity {self.dishes_meals[dishes_meals1][1]['quantity']}")
                    dishes_meals1+=1
                if nuts_seeds1<len(self.nuts_seeds) and (remaining_calories-self.nuts_seeds[nuts_seeds1][1]['Calories'])>=0:
                    remaining_calories-=self.nuts_seeds[nuts_seeds1][1]['Calories']
                    remaining_food_items.append(f"{self.nuts_seeds[nuts_seeds1][0]} having calories {self.nuts_seeds[nuts_seeds1][1]['Calories']} {self.nuts_seeds[nuts_seeds1][1]['unit']} and quantity {self.nuts_seeds[nuts_seeds1][1]['quantity']}")
                    nuts_seeds1+=1
                if ice_cream1<len(self.ice_cream) and(remaining_calories-self.ice_cream[ice_cream1][1]['Calories'])>=0:
                    remaining_calories-=self.ice_cream[ice_cream1][1]['Calories']
                    remaining_food_items.append(f"{self.ice_cream[ice_cream1][0]} having calories {self.ice_cream[ice_cream1][1]['Calories']} {self.ice_cream[ice_cream1][1]['unit']} and quantity {self.ice_cream[ice_cream1][1]['quantity']}")
                    ice_cream1+=1
            print(remaining_food_items)
            print(remaining_calories)








c=Calorie_Tracker('Arjun','chicken curry,3 idli,1 large apple,1 litre of apple juice,3 eggs',3,'reduce weight')
# c.load_low_calorie_food()
print(c.process())
