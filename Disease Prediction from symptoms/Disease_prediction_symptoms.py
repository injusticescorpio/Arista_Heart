import disease_precaution_description
import pandas as pd
import joblib as joblib
import warnings
warnings.filterwarnings("ignore")
class Disease_Prediction_Symptom:
    def __init__(self,name,user_symptoms,user_another_symptom):
        self.name = name
        self.user_symptoms =list(map(lambda _:_.lower().strip(),user_symptoms.split(',')))
        self.user_another_symptom =list(map(lambda _:_.lower().strip(),user_another_symptom.split(',')))
    def list_of_available_symptoms(self):
        symptoms_details = pd.read_csv('X_data.csv')
        symptoms_details.drop('Unnamed: 0', axis=1, inplace=True)
        return list(map(lambda item:item.replace('_',' '),list(map(lambda x: x.lower().strip(), list(symptoms_details.columns)))))
    def preprocess(self):
        symptoms_list=self.list_of_available_symptoms()
        # print(symptoms_list)
        input_symptoms=[0 for i in range(len(symptoms_list))]
        user_symptoms_list=[]
        if 'no' in self.user_another_symptom:
            user_symptoms_list=self.user_symptoms[:]
        else:
            user_symptoms_list=self.user_symptoms[:]+self.user_another_symptom[:]
        for symptoms in user_symptoms_list:
            if symptoms in symptoms_list:
                input_symptoms[symptoms_list.index(symptoms)]=1
        '''
        verifying that the symptoms entered are working
        '''
        def verify():
            print("Symptoms entered by user are:\n")
            for i in range(len(input_symptoms)):
                if input_symptoms[i]==1:
                    print(symptoms_list[i])
        # verify()
        return input_symptoms
    def disease_prediction(self):
        input_data=self.preprocess()
        decision_tree_classifier=joblib.load('decision_tree_model')
        return(decision_tree_classifier.predict([input_data])[0])

    def disease_precaution(self):
        self.precaution=disease_precaution_description.Disease_Precaution_Description(self.disease_prediction())
        return self.precaution.precaution()
    def disease_description(self):
        return '.\n'.join(self.precaution.description().split('.'))


d=Disease_Prediction_Symptom('Arjun',' HEadache,stomach pain,nodal skin eruptions','chills,obesity,excessive hunger')
d.preprocess()
print(d.disease_prediction())
print(d.disease_precaution())
print(d.disease_description())

warnings.filterwarnings("ignore")