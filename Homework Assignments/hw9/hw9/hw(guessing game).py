#Ravi Vasan
#9/15
# Make a random number between 1-100 inclusive
# Give the user 10 chances to guess
    # must control that they use one of the chances
    # must +1 chances
    # if (random number is - guess > 25)
            #Too HIGH
    # else (guess - number is > 25)
            #Too LOW

import os #brings up a bunch of different helpful tools
import random #random is similar and has a lot of different functions
#import brings in a chunk of program that someone else did for us


os.system('cls')
random.seed(20)

randy = random.randrange(1,100)
print("this is a guessing game between 1 and 100. you have 10 chances to guess the number")

for counter in range(10):
        guess=int(input("give me a #..."))
        if guess==randy:
                print("you win!!")
                break
        else: 
                print("try again...")
print(randy)




