#homework for 9/9

#challege
# find the last number
# find the last two numbers
# find the last three numbers

import os
os.system('cls')
num=int(input("give me a number"))
rem=num
#conditional
if(rem==num):
    print(rem%10)
else:
    print("fail")

if(rem==num):
    print(rem%100)
else:
    print("fail")

if(rem==num):
    print(rem%1000)
else:
    print("fail")


