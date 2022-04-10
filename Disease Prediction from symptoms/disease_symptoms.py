import pickle
# arista_model=joblib.load('Arista_symtoms_model')
with open('D:\\Rasa\\Arista_prototype\\actions\\arist_demo','rb') as f:
    arista_model=pickle.load(f)
def symptom_prediction(name,symptoms,anyother_symptoms):
    symptom_evaluate=[]
    if anyother_symptoms in ['no','nay','NO','No','No way']:
        symptoms_list = symptoms.split(',')
    else:
        symptoms_list = symptoms.split(',') + anyother_symptoms.split(',')



    f1 = open('D:\\Rasa\\Arista_prototype\\actions\\symptoms.txt','r')
    symptoms = f1.read().split(' \n')
    f1.close()
    for i in range(0, len(symptoms) - 1):
        if symptoms[i] in symptoms_list:
            symptom_evaluate.append(1)
        else:
            symptom_evaluate.append(0)
    print(symptom_evaluate)
    return f"Hey {name} I think you are having {arista_model.predict([symptom_evaluate])[0]}\n Take rest \n see u {name} \n byArista"



# symptom_evaluate=[]
# symptoms_list = ['shortness of breath','dizziness','asthenia','fall','syncope','pain chest','drool','retch','headache']
# f1 = open('symptoms.txt', 'r')
# symptoms=f1.read().split(' \n')
# f1.close()
# symptom_evaluate=[]
# for i in range(0,len(symptoms)-1):
#     if symptoms[i] in symptoms_list:
#         symptom_evaluate.append(1)
#     else:
#         symptom_evaluate.append(0)
#
#
# print(len(symptom_evaluate))

# p=[0]*404
# print(arista_model.predict([p])[0])
# print(symptom_prediction('Arjun','headache,shortness of breath','vomiting'))