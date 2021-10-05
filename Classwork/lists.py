#ravi vasan
#learning about collections in python
#list

#homework
#word guessing game but you ask for one letter at a time

import os, sys, random
os.system ('cls')

def updateWord(fruits, guesses):
    for letter in fruits:
        if letter in guesses:
            print(letter, end = " ")
        else:
            print('_', end = ' ')

#define fuction for Menu
def Menu():
    print("##########################################################")
    print("#                          Menu                          #")
    print("#                      1) animals                        #")
    print("#                      2) fruits                         #")
    print("#                      3) colors                         #")
    print("#                      4) exit                           #")
    print("# to play the game, select 1-3. to exit the game selet 4.#")
    print("##########################################################")
    sel=input("what would you like to do?")
    # try:
    # except:
    sel=int(sel)
    return sel
def selWord(sel):
    if sel ==1:
        word = random.choice(animals)
    elif sel ==2:
        word = random.choice(fruits)
    else:
        word = random.choice(colors)
    return word
colors = ('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet')
animals = ('lion', 'tiger', 'dog', 'cat', 'monkey', 'giraffe', 'penguin')
fruits = ('apple', 'banana', 'strawberry', 'blueberry', 'grape', 'watermelon', 'orange')

print ("welcome")
print ("guess a letter to see if it is in the word. you have 10 tries.")
name = input("what is your name?")
counter = 0
sel = Menu()
answer=input(name + ", do you want to play the game?")
while sel != 4:
    print
    print ("good luck!")

while ('y' in answer):#control the number of games played
    turns = 10
    counter += 1

    guesses = ' '

    myword=random.choice(fruits)
    myword = myword.lower()

    mywordCount = len(myword)
    letCount= 0

    print(myword)
    updateWord(fruits, guesses)

    while turns > 0 and letCount > mywordCount: 
        print()
        newguess = input ("give me a letter, " + name)
        newguess = newguess.lower()
        if newguess in myword:
                guesses += newguess
            letCount +=1
            print ("you guessed one letter")
        else:
            turns -= 1
            print ("sorry, thats wrong. you have ", turns, " turns left")
        updateWord(fruits, guesses)

    answer = input(name + ", do you want to play again?")
    os.system('cls')
    sel = Menu()
 