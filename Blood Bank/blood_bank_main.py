from bloodbank_db import Blood_Bank

def distance_btw_two_places(place1,place2):
    pass


def Blood_Bank_details(blood_group,name,no_of_units,case,required_date,admitted_hopsital,bleeding_place,bleeding_time,district,contact_number,bystander_name):
    db=Blood_Bank()
    blood_bank_user_details=db.fetch()
    representative_to_be_contacted=[]
    for representative in blood_bank_user_details:
        if distance_btw_two_places(representative[3],bleeding_place)<30:
            representative_to_be_contacted.append(representative)
    
