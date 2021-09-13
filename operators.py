#Ravi Vasan
#we are going to learn about operators
# + - * / %
#2+2 = 4
#4-1 = 3
#3*6 = 18
#18%2 = 9(no remainder) - this means divide by two and find the remainder
#%= modular(mod)
import os
os.system('cls')

num=int(input("give me a number"))
rem=num%2
#conditional
#when you are asking in a conditional you need ==
if(rem==0):
    print("the number is even ")
else:
    print("the number is odd")
#how to find the last digit in the number = num%10
#how to find the last two digits in teh number = num%100



