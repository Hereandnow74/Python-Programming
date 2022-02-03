# -*- coding: utf-8 -*-
"""
Program: Average Revisited Project
Author: Mikhail Klepikov
Description: This program collect the numbers and compute the average without
knowing how many numbers to expect.
Revisions:
    00 - input number of numbers you would like to average
    01 - create a loop sum numbers
    02 - count the average of numbers
    03 - print result
    04 - second attempt on program to get solution in 6 lines of code. (put previous version in Triple-quoted comment at the end of the program code)
    05 - create a new while loop
    06 - print result
"""
# there are no import module
# there are no literal constants
# there are no class definitions
# there are no functions 

# announcement on the next line
print("\nProgram to compute the average of the numbers provided.\n\nEnter each number followed by <enter>.\nWhen you are done, just hit <enter> in response to the prompt.\n ")
# main program begins on the next line
sum, count = 0, 0
# creating a loop, that ask for a number, and if there in no input then break the loop.
while i := input("Enter a number: "):
    sum += float(i) # accumulate the value that entered to sum
    count += 1 # accumulate the number that entered to count
# print output with calculation using f-string format
print('\nYou entered ' + str(count) + ' numbers.\nThe average is ' + str(sum / count) + '.')

'''
This is my first attempt on the task. Before I got it how to make 6 lines of code.

# announcement on the next line
print("Program to compute the average of the numbers provided.\n\n"
      "Enter each number followed by <enter>.\n"
      "When you are done, just hit <enter> in response to the prompt.\n")
# main program begins on the next line
count = 0
sum = 0
# creating a loop
while True:
    number = input("Enter number: ") # input numbers
    if (number == "") or (number == " "): # if number "" or " " then break the loop
       break 
    else: # else sum numbers
        num = float(number)
        sum += num
        count += 1
average = sum / count # calculate the average from a sum of numbers by dividing by quantity of numbers
print("\n")
print("You entered " + str(count) + " numbers.")
print("The average is " + str(average) +".") # print result
'''
