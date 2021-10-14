#ravi vasan
#learning about collections in python
#list

#homework
#word guessing game but you ask for one letter at a time

import os, sys, random
os.system ('cls')

def updateWord(word, guesses, turns): #this function checks if the letter is in the word that is being guessed
    count = 0
    for letter in word:
        if letter in guesses:
            print(letter, end = " ")
            count += 1
        else:
            print('_', end = ' ')
            turns-=1
    
    return count

#define fuction for Menu
def Menu():
    print("####################################################################################")
    print("#                                      Menu                                        #")
    print("#                                  1) animals                                      #")
    print("#                                  2) fruits                                       #")
    print("#                                  3) colors                                       #")
    print("#                                  4) scoreboard                                   #")
    print("#                                  5) exit                                         #")
    print("# to play the game, select 1-3. for scoreboard select 4. to exit the game select 5.#")
    print("####################################################################################")

    while 1:
        sel=input("which one would you like to do?")
        try:
            sel = int(sel)
            break
        except ValueError:
            print("this is not an integer, please respond with 1-5")
    return sel

def selWord(sel): #determine which list to randomly choose from
    if sel == 1:
        word = random.choice(animals)
    elif sel == 2:
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


while sel < 4:#control the number of games played
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

    #print(word) #just to check what it is
    updateWord(word, guesses, turns)

    while turns > 0 and letCount < wordCount: #controls the letters guessed and turns
        print()
        newguess = input ("give me a letter, " + name)
        newguess = newguess.lower()
        if newguess in word:
            guesses += newguess
            print ("you guessed one letter")
        else:
            turns -= 1
            print ("sorry, thats wrong. you have ", turns, " turns left")
        letCount = updateWord(word, guesses, turns)
    if turns > 0 :
        print(" ")
        print("you win!!")
        score += 1
        print(score)
    else:
        print("you lose...try again")
        score = score

    score = 3 * wordCount + 5 * turns
    if score > maxscore:
        maxscore = score
    print("this is your new highscore: " + str(maxscore))
    sel = Menu()

    os.system('cls')

myFile = open('scoreboard.txt', 'a') #opens my scoreboard
myFile.write('\n' + name + '\t Highest score:\t' + str(maxscore))

if sel == 4:
    myFile = open("scoreboard.txt", "r")
    print(myFile.read())
    myFile.close()

if sel == 5:
    print(name + ": " + str(maxscore))

#when you finish playing the game add the score to the file
# what is the name of the person who played the game 
# what is their score and make sure that it stays
