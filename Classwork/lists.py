#ravi vasan
#learning about collections in python
#list

myfruits = ["apple," "berries", "bananas"]

# for x in myfruits:
#     print (x)
# for x in myfruits[0]:
#     print ("_", end = " ")

#homework
#word guessing game but you ask for one letter at a time

import os, sys, random
os.system ('cls')

fruits = ('apple', 'banana', 'strawberry', 'blueberry', 'grape', 'watermelon', 'orange')

print ("welcome")
print ("guess a letter to see if it is in the fruit. you have 10 tries.")

answer=input("do you want to play a game?")
while ('y' in answer):
    guesses = 0
    myword=random.choice(fruits)
    #print (myword)
    for x in fruits:
        print (x)
    for x in fruits[0]:
        print ("_", end = " ")
    while (guesses < 10 and myfruits != myword):
        # for char in myword:
        #     print (char)

        char = input("give me a letter")
        if myword == (input):
            print ("yes!! you win!")
        else:
            print("guess another!")
        guesses += 1
        if char == myword:
            print ("you win!!")
        else:
            print ("guess again!")
        
    answer=input("do you want to play again?")
