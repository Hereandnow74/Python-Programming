# -*- coding: utf-8 -*-
"""
Program: Percent in class
Author: Mikhail Klepikov
Description: This program count percent of males and females in class.
Revisions:
    00 - input males and females numbers
    01 - find number of 1% in class
    02 - count males and females percentage
    03 - print the result
"""
# there are no import statements
# there are no literal constants
# there are no class definitions
# there are no function definitions
# main program begins on the next line
m = int(input("Entre number of males: ")) # input males number in class
f = int(input("Entre number of females: ")) # input females number in class
p = 100 / (m + f) # find the number of 1% in class
mper = int(round(p * m)) # find the percentage of males in class
fper = int(round(p * f)) # find the percentage of females in class
print ("Percent males: " + str(mper) + "%") # print result of males percentage
print ("Percent females: " + str(fper) + "%") # print result of females percentage