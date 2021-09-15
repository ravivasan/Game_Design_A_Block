#Homework for 9/13
#Ravi Vasan
#different types of data types

#string
#userInput = string 'str'

# i="hello"
# print("hello")
# for i in "hello":
#     print(i)

# a="Hello,world"
# print(len(a))

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")
else:
    print("Error, 'free' is not present")


#Slicing
b="Hello, World!"
print(b[2:5])

b="Hello, World!"
print(b[:5])

b="Hello, World!"
print(b[2:])

    #Negative Indexing
b="Hello, World!"
print(b[-5:-2])









#formatting
#places strings where {} are
print("formatting")
quantity = 3
itemno = 567
price = 49.95

order = "i want {0} of item number {1} for {2} dollars"
print(order.format(quantity, itemno, price))

