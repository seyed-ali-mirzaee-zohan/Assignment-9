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

s1 = int(input("Please enter s1: "))
m1 = int(input("Please enter m1: "))
s2 = int(input("Please enter s2: "))
m2 = int(input("Please enter m2: "))


class Fraction:
    def __init__(self,s,m):
        self.s =s
        self.m =m

    # تابع جمع
    def Addition(host,guest):
        return f" {(host.s * guest.m) + (guest.s * host.m)} / {host.m * guest.m} "

    # نمایش تابع جمع
    def show_Addition(self):
        print(self.Addition())

    # تابع ضرب
    def Multiplication(host,guest):
        return f" {(host.s * guest.s)} / {host.m * guest.m} "

    # نمایش تابع ضرب
    def show_Multiplication(self):
        print(self.Multiplication())

    # تابع تفریق
    def Subtraction(host,guest):
        return f" {(host.s * guest.m) - (guest.s * host.m)} / {host.m * guest.m} "

    # نمایش تابع تفریق
    def show_Subtraction(self):
        print(self.Subtraction())

    # تابع تقسیم
    def Division(host,guest):
        return f" {host.s * guest.m} / {guest.s * host.m} "

    # نمایش تابع تقسیم
    def show_Division(self):
        print(self.Division())

fraction_1=Fraction(s1,m1)
fraction_2=Fraction(s2,m2)

if enter==1:
    answer =fraction_1.Addition(fraction_2)
    print(answer)

if enter==2:
    answer =fraction_1.Multiplication(fraction_2)
    print(answer)

if enter==3:
    answer =fraction_1.Subtraction(fraction_2)
    print(answer)

if enter==4:
    answer =fraction_1.Division(fraction_2)
    print(answer)