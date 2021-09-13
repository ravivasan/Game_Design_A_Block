#Ravi Vasan
#9/13
#This is about data Type
# how strings work

import os
os.system('cls')
#integers = int (- 0 +) 4 bytes
# also integers = long (- 0 +) 8 bytes
#real
    #float (- 0 +) 4 bytes
        #if there's a decimal on an integer or number it is float
    #double (- 0 +) 8 bytes
#boolean = T-F 
userInput=(input("type something"))
print (type(userInput))
try:
    int(userInput)
    check=True
except ValueError:
    check=False

print(check)
if(check):
    #i will be back
    print()
else:
    print(len(userInput))
for i in userInput:
    print(i)

if len(userInput>3):
    print(userInput[3])



# if(type(userInput)==int):
#     print("you gave me an integer")
# else:
#     print("Your input is not an integer")
# intUser=int(userInput)
# print("this is the integer calue of User Input", intUser)
