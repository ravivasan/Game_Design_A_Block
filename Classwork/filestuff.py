#Ravi Vasan
#10/7/21
#we are going to learn how to:
#   open() a file
#   write to a file "w"
#   read from a file "r"
#   append to a file "a"
#   close() a file
import os, time
os.system('cls')

#to create a file you must declare an object so we can open a file
#when you open a file you need to use "w"
myFile = open("score.txt", "w")#before you can write anything you need to distinguish the file option and open it before making commands to it
myFile.write("hello there, my name is ravi \t what is yours?")
myFile.close()
#always close a file when you are done using it
myFile = open ("score.txt", "w")
myFile.write("and now we will play a game")
myFile.close()
#read and print the file
Filemy = open("score.txt", "r")
print(Filemy.read())
Filemy.close()
score = 450
anotherFile = open("score.txt", "a")
anotherFile.write("\n he highest score: \t" + str(score))
anotherFile.close()


