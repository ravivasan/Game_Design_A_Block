#Ravi Vasan
#9/15
#
# We are going to learn how to use random numbers
# We are also learning how to make a small game that will guess the numbers

import os #brings up a bunch of different helpful tools
import random #random is similar and has a lot of different functions
#import brings in a chunk of program that someone else did for us


os.system('cls')
random.seed(20)

#this loop was to play with random numbers
for i in range(10):
    randy = random.randint(3,5)
    print(randy)
    randy2 = random.random()
    randy2 *=100
    print(int(randy2))

#arrays in python are called lists
#lists are signified by []
# [ , , ,]

fruits = ["apple", "banana", "berries"]
myfruits = random.choices(fruits)
print(myfruits)








