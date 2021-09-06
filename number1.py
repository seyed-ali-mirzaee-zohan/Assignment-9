import pyfiglet
from termcolor import colored
result = pyfiglet.figlet_format("fraction", font = "digital" )
print(result)
print(colored(' Hello, Welcome to the fractions program ', 'red', attrs=['reverse', 'blink']))
print()
print(colored(' The following options are now available : ', 'white', attrs=['reverse', 'blink']))
print()
print(colored(' 1 : Addition       ', 'green', attrs=['reverse', 'blink']))
print(colored(' 2 : Multiplication ', 'yellow', attrs=['reverse', 'blink']))
print(colored(' 3 : Subtraction    ', 'green', attrs=['reverse', 'blink']))
print(colored(' 4 : Division       ', 'yellow', attrs=['reverse', 'blink']))
print()
enter=int(input( "Please enter your desired number : "))
print()

class Fraction:
    def __init__(self):
        self.s1 = int(input("Please enter s1: "))
        self.m1 = int(input("Please enter m1: "))
        self.s2 = int(input("Please enter s2: "))
        self.m2 = int(input("Please enter m2: "))

    # تابع جمع
    def Addition(self):
        return f" {(self.s1 * self.m2) + (self.s2 * self.m1)} / {self.m1 * self.m2} "

    # نمایش تابع جمع
    def show_Addition(self):
        print(self.Addition())

    # تابع ضرب
    def Multiplication(self):
        return f" {(self.s1 * self.s2)} / {self.m1 * self.m2} "

    # نمایش تابع ضرب
    def show_Multiplication(self):
        print(self.Multiplication())

    # تابع تفریق
    def Subtraction(self):
        return f" {(self.s1 * self.m2) - (self.s2 * self.m1)} / {self.m1 * self.m2} "

    # نمایش تابع تفریق
    def show_Subtraction(self):
        print(self.Subtraction())

    # تابع تقسیم
    def Division(self):
        return f" {self.s1 * self.m2} / {self.s2 * self.m1} "

    # نمایش تابع تقسیم
    def show_Division(self):
        print(self.Division())

result = Fraction()

if enter==1:
    result.show_Addition()

if enter==2:
    result.show_Multiplication()

if enter==3:
    result.show_Subtraction()

if enter==4:
    result.show_Division()