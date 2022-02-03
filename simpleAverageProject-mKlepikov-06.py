# -*- coding: utf-8 -*-
"""
Program: Simple Average Project
Author: Mikhail Klepikov
Description: This program use a loop and an accumulation pattern to calculate the average of a
sequence of numbers.
Revisions:
    00 - input number of numbers you would like to average
    01 - create a list "l"
    02 - create a loop to add numbers in list
    03 - add count into a loop to count what number is in sequence of numbers
    04 - count the average of numbers
    05 - print result
"""

# there are no import module
# there are no literal constants
# there are no class definitions
# there are no functions 

# announcement on the next line
print("Program to compute the average of the numbers provided.")
# main program begins on the next line
num = int(input("How many numbers would you like to average? ")) # put the quantity of numbers you would like to average
c = 0 # will use this parameter to count the sequence of numbers
l=[] # creating list for numbers
for i in range(0, num): # creating a loop with "num" quantity of numbers
    c = c + 1 # add +1 to count for every loop
    number = int(input("Enter number " + str(c) + ": ")) # input the number you want to be added in sequence of numbers for calculating the average
    l.append(number) # add number into list
average = sum(l) / num # calculate the average from a sum of "l" list of numbers by dividing by quantity of numbers
print("The average is " + str(average) +".") # print result