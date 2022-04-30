from bloodbank_db import Blood_Bank
from faker import Faker
fake = Faker('en-IN')
user=Blood_Bank()
user.create_table()

def fake_details_generating():
    user.insert_details('arjun','+919074774118','Chengannur,Kerala')
    location=['Mannar,Kerala','Kollam,Kerala','Kottayam,Kerala','Kochi,Kerala','Chengannur,Kerala','Palakkad,Kerala','Kannur,Kerala','Chennai,Tamil nadu','Adoor,Kerala','Thrissur,Kerala','Alappuzha,Kerala','Munnar,Kerala','Vagamon,Kerala','Thiruvananthapuram,Kerala','Ernakulam,Kerala','Pathanamthitta,Kerala','Changanassery,Kerala','Kallissery,kerala']
    for _ in range(len(location)):
        user.insert_details(fake.first_name_male(),fake.phone_number(),location[_])
    print(user.fetch())
# fake_details_generating()
def add_representative_details(name,mobile,place):
    user.insert_details(name.title(), mobile, place.title())
    return f"user created with id number {user.fetch()[-1][0]} save this id for further usage"

def update_representative_details(name,mobile,place,id):
    user.update_details(name.title(),mobile,place.title(),id)
    return f"user successfully updated"