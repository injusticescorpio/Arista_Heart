import json
from collections import defaultdict

class Disease_Precaution_Description:
    def __init__(self,disease):
        self.disease=disease
    def precaution(self):
        with open('symptom_precaution.json', 'r') as f:
            disease_precaution_details = json.load(f)
        disease_precaution = defaultdict(list)
        for disease in disease_precaution_details:
            for i in range(1, len(disease_precaution_details[disease])):
                disease_precaution[disease.strip()].append(disease_precaution_details[disease][f"Precaution_{i}"])
        disease_precaution = dict(disease_precaution)
        try:
            return '\n'.join(disease_precaution[self.disease.strip()])
        except:
            return "Occured some problem in retrieving the disease precaution :("
    def description(self):
        with open('symptom_description.json', 'r') as f:
            disease_description = json.load(f)
        disease_description_details = defaultdict(list)
        for disease in disease_description:
            disease_description_details[disease.strip()].append(disease_description[disease]['Description'])
        try:
            return f'\n{"".join(disease_description_details[self.disease])}'
        except:
            return "Occured some problem in retrieving the disease precaution :("
d=Disease_Precaution_Description('Malaria')
print(d.precaution())