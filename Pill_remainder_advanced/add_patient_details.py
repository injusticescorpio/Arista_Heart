
from pill_remainder_db import Patient

db=Patient()
db.create_table()
db.insert_details(2,'Arjun','+919074774118','arjunpyromancer@gmail.com','parestamol 3 day night,omee 2 day noon night')
print(db.fetch())


