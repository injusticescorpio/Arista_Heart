from datetime import datetime
class Pillremainder:
    def __init__(self,days,medine_details):
        self.days =days
        self.medine_details=medine_details
    def preprocess(self):
        self.disease=[]
        self.medicine_interval=[]
        self.medicine_number=[]
        for i in self.medine_details.split(','):
            d={'day':0,'noon':0,'night':0}
            details=i.split(' ')
            self.disease.append(details[0])
            self.medicine_number.append(int(details[1]))
            for j in details[2:]:
                d[j]+=1
            self.medicine_interval.append(''.join(list(map(str,d.values()))))

    def pill_remainder(self):
        print(self.disease)
        print(self.medicine_interval)
        print(self.medicine_number)
        while self.medicine_number:
            mytime = ["08:59","12:59","20:59"]
            day=[self.disease[i] for i in range(len(self.medicine_interval)) if self.medicine_interval[i][0]=='1']
            noon = [self.disease[i] for i in range(len(self.medicine_interval)) if self.medicine_interval[i][1] == '1']
            night = [self.disease[i] for i in range(len(self.medicine_interval)) if self.medicine_interval[i][2] == '1']
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            print(current_time)
            prev=''
            if len(day)>0 and current_time<=mytime[0]:
                while current_time!="09:00":
                    now = datetime.now()
                    current_time = now.strftime("%H:%M")
                    if prev!=current_time:
                        print(current_time)
                    prev=current_time
                print(f"you need to take the following medicines {' '.join(day)}")
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            print(current_time)
            prev = ''
            if len(noon)>0 and current_time<=mytime[1]:
                while current_time!="13:00":
                    now = datetime.now()
                    current_time = now.strftime("%H:%M")
                    if prev!=current_time:
                        print(current_time)
                    prev=current_time
                print(f"you need to take the following medicines {' '.join(noon)}")
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            print(current_time)
            prev = ''
            if len(night)>0 and current_time<=mytime[2]:
                while current_time!="21:00":
                    now = datetime.now()
                    current_time = now.strftime("%H:%M")
                    if prev!=current_time:
                        print(current_time)
                    prev=current_time
                print(f"you need to take the following medicines {' '.join(night)}")
            self.medicine_number=[i-1 for i in self.medicine_number]
            f=[]
            for i in self.medicine_number:
                if i!=0:
                    f.append(i)
            self.medicine_number=f[:]






# n=int(input('enter number of days')) 3
# m=input()  p 3 day night,a 2 day noon night

n=3
m='parestamol 3 day night,omee 2 day noon night'

p=Pillremainder(n,m)
p.preprocess()
p.pill_remainder()

