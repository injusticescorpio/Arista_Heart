
from pill_remainder_db import Patient

db=Patient()
db.insert_details(3,'parestamol 3 day night,omee 2 day noon night')

print(db.fetch())
