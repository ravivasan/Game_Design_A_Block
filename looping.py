#Ravi Vasan
#os = operating systems
import os
os.system('cls')




# 09/07/2021
# We are going to learn how to use for loop 
star=int(input("how many stars?"))
print("stars",star)
line=star
for i in range(line): 
    for space in range (i):
        print("  ",end=" ")
    for counter in range(star):  #you can use a number or a variable
        print("* ", end=" ")  #print on the same line
        #print(counter+1, end=" ") 
    print()  #print a return creating a new line
    star-=1  #short cut for star=star-1
print("thank you")
