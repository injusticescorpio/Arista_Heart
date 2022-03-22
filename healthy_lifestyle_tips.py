'''
Add healthy life style tips in a list.
'''

import random

# Add rest of the tips
Healthy_tips =['Eat a balanced diet', 'Add variety to your meals',
'Stay well hydrated','Remember to drink 8 glasses of water a day','Exercise regularly','Get enough good sleep ',
'Limit your alcohol intake','Do not smoke','Protect yourself from the sun','Wash your hands']

def healthy_tips():
    return random.choice(Healthy_tips)

