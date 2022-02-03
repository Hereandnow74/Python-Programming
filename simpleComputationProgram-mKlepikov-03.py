# -*- coding: utf-8 -*-
"""
Program: Simple Computation Project <circumference1>
Author: Mikhail Klepikov
Description: This program compute the circumference of the circle with the use of diameter value.
Revisions:
    00 - input value of diameter and calculating circumference
    01 - converting float objects to a string
    02 - print the result
"""
import math # importing math to get a Pi number
# there are no literal constants
# there are no class definitions
# there are no function definitions

# announcement on the next line
print("SIMPLE COMPUTATION PROGRAM <circumference1>")
# main program begins on the next line
diameter = float(input("Enter a number of Diameter: ")) # input the diameter number
circumference = float(diameter * math.pi) # calculating circumference
'''
float() - Convert a string or number to a floating point number, if possible.
'''
d = str(diameter) # convert diameter into string
c = str(circumference) # convert circumference into string
'''
The str() function converts values to a string form.
'''
print("The circumference of a circle of diameter " + d + " is " + c + ".") # print result