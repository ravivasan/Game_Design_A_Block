#learning while loop
#Ravi Vasan
#9/21
#Control the main game


#first thing is instructions of the game

import os
import random
num = 0

answer=input("do you want to play a game?")
while ('y' in answer):
    chances = 0
    randy=random.randint(1,100)
    print ("welcome")
    print ("guess a number between 1 and 100 and see if you guessed the right number. you have 10 chances")
    print (randy)
    while (chances < 10 and num != randy):
        num = input("give me a number")
        try:
            num = int(num)
            chances += 1
            if num == randy:
                print ("you win!!")
            else:
                if int(num)-randy <10:
                    print("guess higher")
                if int(num)-randy >10:
                    print("guess lower")
        except ValueError:
            check = False
            print ("guess an integer!!!")
            print ("try again")
        if int(num)-randy <10:
            print("guess higher")
        if int(num)-randy >10:
            print("guess lower")
    answer=input("do you want to play again?")
    # while (num>10):
    #     print (num)
    #     num +=5
    # print("this is you number", num)
    # answer = input("do you want to play again?")
    # try:
    #     answer = ("no")
    #     print ("")
    # except:
    #     answer = ("yes")
    #     print ()

    print("thank you for playing")




