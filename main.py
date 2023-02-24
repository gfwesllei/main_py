import math;
import datetime;

def calcule_Square(number: int):
    return math.sqrt(number)

def calcule_age(birth_year:int):
    currentYear =  datetime.date.today().year
    return currentYear - birth_year


#print("Hello let calcule square of your number!")
#number = int(input('Type a number to calcule: '))
#print("Squart of "+str(number)+" is: ",calcule_Square(number))


#Calcule age of user
print(datetime.date.today)

birthYear = input("Type your burn year:")
birthYear = int(birthYear);
print(f'Yout age is {calcule_age(birthYear)}')
