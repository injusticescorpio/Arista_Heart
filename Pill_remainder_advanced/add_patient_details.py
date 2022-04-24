
from pill_remainder_db import Patient

db=Patient()
db.create_table()
db.insert_details(2,'parestamol 3 day night,omee 2 day noon night')
print(db.fetch())


