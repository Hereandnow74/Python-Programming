# -*- coding: utf-8 -*-
"""
Program: Linear Prediction Program
Author: Mikhail Klepikov
Description: This program predict the next number in the linear sequence.
Revisions:
    00 - input 1 st and 2nd numbers
    01 - find sequence of numbers and find the 3rd number
    02 - print the result
"""
# there are no import statements
# there are no literal constants
# there are no class definitions
# there are no function definitions

# announcement on the next line
print("Linear Prediction Program:")
# main program begins on the next line
print("Predict the 3d number in a sequence") # print the task 
x = int(input("Enter the first number: ")) # input 1st number
y = int(input("Enter the second number: ")) # input 2nd number
sequence = x - y # find the sequence between 1st and 2nd numbers
z = y - sequence # find the 3rd number
print("The linear sequence is: " + str(x), str(y), str(z)) # print the result
