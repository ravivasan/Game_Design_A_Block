#ravi vasan
#learning about collections in python
#list

#homework
#word guessing game but you ask for one letter at a time

import os, sys, random
os.system ('cls')

def updateWord(word, guesses, turns):
    for letter in word:
        if letter in guesses:
            print(letter, end = " ")
        else:
            print('_', end = ' ')
            turns-=1

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

    while 1:
        sel=input("which one would you like to do?")
        try:
            sel = int(sel)
            break
        except ValueError:
            print("this is not an integer, please respond with 1-4")
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
score = 0
maxscore = 0
name = input("what is your name?")

counter = 0
sel = Menu()
print(sel)

while sel != 4:#control the number of games played
    print ("welcome, " + name)
    print ("guess a letter to see if it is in the word. you have 10 tries.")
    print ("good luck!")

    turns = counter + 2
    counter += 1

    guesses = ' '

    word = selWord(sel)
    word = word.lower()

    wordCount = len(word)
    letCount= 0

    print(word) #just to check what it is
    updateWord(word, guesses, turns)

    while turns > 0 and letCount < wordCount: 
        print()
        newguess = input ("give me a letter, " + name)
        newguess = newguess.lower()
        if newguess in word:
            guesses += newguess
            letCount +=1
            print ("you guessed one letter")
        else:
            turns -= 1
            print ("sorry, thats wrong. you have ", turns, " turns left")
        updateWord(word, guesses, turns)
    if turns > 0 :
        print(" ")
        print("you win!!")
        score += 1
        print(score)
    else:
        print("you lose...try again")
        score = score

    score = 3 + wordCount + 5 * turns
    if score > maxscore:
        maxscore = score
    print(maxscore)
    sel = Menu()

    os.system('cls')
    sel = Menu() 