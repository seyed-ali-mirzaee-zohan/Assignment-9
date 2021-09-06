import pyfiglet
from termcolor import colored
result = pyfiglet.figlet_format("Time", font = "digital" )
print(result)
print(colored(' Hello, Welcome to the program ', 'red', attrs=['reverse', 'blink']))
print()
print(colored(' The following options are now available : ', 'white', attrs=['reverse', 'blink']))
print()
print(colored(' 1 : Addition       ', 'green', attrs=['reverse', 'blink']))
print(colored(' 2 : Subtraction    ', 'yellow', attrs=['reverse', 'blink']))
print(colored(' 3 : Second ⇨ Time  ', 'green', attrs=['reverse', 'blink']))
print(colored(' 4 : Time ⇨ Second  ', 'yellow', attrs=['reverse', 'blink']))
print()
enter=int(input("Please enter your desired number : "))
print()

class Time:
    def Specifications(self):

        time1=input("Please enter the first time  (h:m:s) :  ")
        time_1=time1.split(":")
        h1=int(time_1[0])
        m1=int(time_1[1])
        s1=int(time_1[2])
        self.h1=h1
        self.m1=m1
        self.s1=s1

        time2=input("Please enter the second time (h:m:s) :  ")
        time_2=time2.split(":")
        h2=int(time_2[0])
        m2=int(time_2[1])
        s2=int(time_2[2])
        self.h2=h2
        self.m2=m2
        self.s2=s2
        
    # تابع جمع
    def Addition(self):
        self.s3=self.s1+self.s2
        self.m3=self.m1+self.m2
        self.h3=self.h1+self.h2

        if self.s3>=60:
            self.s3-=60
            self.m3+=1
        if self.m3>=60:
            self.m3-=60
            self.h3+=1

        return f" {self.h3} : {self.m3} : {self.s3} "

    # نمایش تابع جمع
    def show_Addition(self):
        print(self.Addition())

    # تابع تفریق
    def Subtraction(self):
        self.total_seconds_1=self.h1*3600+self.m1*60+self.s1
        self.total_seconds_2=self.h2*3600+self.m2*60+self.s2

        if self.total_seconds_1>=self.total_seconds_2:
            self.seconds=self.total_seconds_1-self.total_seconds_2
            self.hour=self.seconds//3600
            self.total_Minutes=self.seconds-3600*self.hour
            self.minutes=self.total_Minutes//60
            self.second=self.total_Minutes-60*self.minutes 

            return f" {self.hour} : {self.minutes} : {self.second} "

        else :
            self.seconds=self.total_seconds_2-self.total_seconds_1
            self.hour=self.seconds//3600
            self.total_Minutes=self.seconds-3600*self.hour
            self.minutes=self.total_Minutes//60
            self.second=self.total_Minutes-60*self.minutes 

            return f" {self.hour} : {self.minutes} : {self.second} "    

    # نمایش تابع تفریق
    def show_Subtraction(self):
        print(self.Subtraction())

    # تابع تبدیل ثانیه به زمان
    def second_to_time(self):

        Seconds=int(input( "Please enter the seconds : "))
        self.seconds=Seconds
        self.hour=self.seconds//3600
        self.total_Minutes=self.seconds-3600*self.hour
        self.minutes=self.total_Minutes//60
        self.second=self.total_Minutes-60*self.minutes 

        return f" {self.hour} : {self.minutes} : {self.second} "

    # نمایش تابع تبدیل ثانیه به زمان
    def show_second_to_time(self):
        print(self.second_to_time())

    # تابع تبدیل زمان به ثانیه
    def time_to_second(self):

        time1=input("Please enter the first time  (h:m:s) :  ")
        time_1=time1.split(":")
        h1=int(time_1[0])
        m1=int(time_1[1])
        s1=int(time_1[2])
        self.h1=h1
        self.m1=m1
        self.s1=s1
        self.total_seconds_1=self.h1*3600+self.m1*60+self.s1

        return f"seconds : {self.total_seconds_1}"

    # نمایش تابع تبدیل زمان به ثانیه
    def show_time_to_second(self):
        print(self.time_to_second())

result = Time()

if enter==1:
    result.Specifications()
    result.show_Addition()

if enter==2:
    result.Specifications()
    result.show_Subtraction()

if enter==3:
    result.show_second_to_time()

if enter==4:
    result.show_time_to_second()