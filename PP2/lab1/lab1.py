print("Hello, World!") #Python HOME / Python Intro

import sys
print(sys.version) #Python Get Started

if 5 > 2:
  print("Five is greater than two!") #Python Syntax

#print("Hello, World!")
print("Cheers, Mate!") #Python Comments

x = 5
y = "John"
print(x)
print(y) #Python Variables

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John" #Variable Names

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z) #Assign Multiple Variables

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #Output Variables

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)
myfunc()
print("Python is " + x) #Global Variables

x = 5
print(type(x)) #Data Types

x = 1
y = 35656222554887711
z = -3255522
print(type(x))
print(type(y))
print(type(z)) #Python Numbers

#Python Casting:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2
x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

print("Hello")
print('Hello') #Python Strings

#Slicing Strings:
b = "Hello, World!"
print(b[2:5]) #Get the characters from position 2 to position 5 (not included):


#Modify Strings:
a = "Hello, World!"
print(a.upper())

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"

a = "Hello, World!"
print(a.replace("H", "J"))

a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']


a = "Hello"
b = "World"
c = a + b
print(c) #Concatenate String 


#Format Strings:
age = 36
txt = f"My name is John, I am {age}" #Create an f-string:
print(txt)

price = 59
txt = f"The price is {price} dollars" #Add a placeholder for the price variable:
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars" #Display the price with 2 decimals:
print(txt)


txt = "We are the so-called \"Vikings\" from the north." #Escape Characters