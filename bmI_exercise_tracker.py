
import requests
import os
import webbrowser


class BMI:
    def __init__(self,height,weight):
        self.headers = {
    "X-RapidAPI-Host": "body-mass-index-bmi-calculator.p.rapidapi.com",
    "X-RapidAPI-Key": os.environ['bmi_calculate_key']
}
        self.weight_details={

            'Underweight':"If your BMI is less than 18.5, then it means that you are underweight. To avoid health complications that may arise due to low levels of body fat, you need to put on more weight. Make sure you get in touch with your doctor or a dietician for professional insight and advice.",
                'Healthy':"If you have a BMI that falls in between 18.5 to 22.9, then it means that you have a healthy weight in relation to your height. This is your normal BMI range. When you maintain a healthy level of body fat, it means that you have a much lower risk of developing health complications.",
            'Overweight':"If you have a BMI that falls in between 23.0 to 24.9, it means that you are overweight. In other words, you have a higher than ideal level of body fats considering your height. In such cases, it is important that you lose some amount of weight in order to improve your health. It is recommended that you talk to a doctor or dietician for professional advice.",
            'Obese':"If your BMI is more than 25.0, then it indicates that you are obese, or in other words, heavily overweight. It is far from your ideal BMI and it means that you have way too much body fat in relation to your height, and this can pose serious health risks. It is important that you lose weight for health reasons. Make sure to contact your doctor or dietician for professional advice in such a situation."


        }
        self.height=height
        self.weight=weight

    def bmi_calculation(self):
        url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/metric"

        querystring = {"weight": self.weight, "height": self.height}
        # os.environ['bmi_calculate_key']

        self.bmi = requests.request("GET", url, headers=self.headers, params=querystring).json()['bmi']
        return f"Your BMI is {self.bmi}"

    def weight_category(self):
        url = "https://body-mass-index-bmi-calculator.p.rapidapi.com/weight-category"

        querystring = {"bmi": self.bmi}
        self.weightCategory = requests.request("GET", url, headers=self.headers, params=querystring).json()['weightCategory']
        return [self.weightCategory,self.weight_details[self.weightCategory]]
    def play_video(self,url):
        webbrowser.open(url)
    def play_category(self):
        if self.weightCategory =='Overweight' or self.weightCategory =='Obese':
            self.play_video('https://www.youtube.com/watch?v=H3jJ29oE8Zg')
        elif self.weightCategory == 'Underweight':
            self.play_video('https://www.youtube.com/watch?v=W45EUSMnlpg')
        else:
            self.play_video('https://www.youtube.com/watch?v=K-Ch9kbtLYQ')




bmi=BMI(1.94,100)
print(bmi.bmi_calculation())
print(bmi.weight_category())
bmi.play_video('https://www.youtube.com/watch?v=H3jJ29oE8Zg')






