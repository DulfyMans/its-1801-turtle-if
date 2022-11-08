"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

casper = turtle.Turtle()

# for c in ['red', 'green', 'blue', 'yellow']:
#     t.color(c)
#     t.forward(75)
#     t.left(90)
numberStr = input("Type a number:")
print ("You just typed: " + numberStr)
# Remember numberStr is stored as variable of type string
# This means we cannot use numberStr in mathematical equation

# Convert numberStr to integer variable called numberInt

numberInt = int(numberStr)

# Declare a value to be used in comparison

b = 6 # b is number not string

if numberInt > b:
  print("You just typed a number greater than " + str(b) )
elif numberInt < b:
  print("You just typed a number less than " + str(b) ) 
else:
  print("You just typed " + str(b) + "!!!")