import math
import random

upper = int(input("\n Input the upper value to be guessed \n"))
lower = int(input("\n Input the lower limit to be guessed \n"))

x = random.randint(lower, upper)
# randrange(start,stop,step),
print("\n you have only ",round(math.log(upper - lower + 1, 2)),"chances left to guess \n")
# number of chances = (upper - lower +1),
count = 0
#intializing the count
while count < math.log(upper - lower + 1, 2):
    count +=1
    guess = int(input("enter the guessed number\n"))
    if x == guess:
        print("congo ! you did it in ",count, "try")
        break
    elif x > guess :
        print("\n the number you guessed is too small please try again")
    elif x < guess :
        print("\n the number you have entered is too high , try again")

if count  >= math.log(upper-lower+1,2):
    print("\n the number is %d %x")
    print("\n better luck ")

#DONE


