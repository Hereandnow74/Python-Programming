# -*- coding: utf-8 -*-
"""
Program: Text Graph Project
Author: Mikhail Klepikov
Description: 
    Revisions:
    00 - input numbers
    01 - turn input in the list
    01 - create a loop
    02 - create if to add in graph form only positive numbers tha are less than 50 or else print "?"
    04 - print results
"""

# there are no import module
# there are no literal constants
# there are no class definitions
# there are no functions 

# announcement on the next line
print("TextGraph: Draw a bar graph using characters")
# main program begins on the next line
data = input("Enter up to 10 positive whole numbers less than 50: ")
numbers = data.split() # split numbers we put in data in list
for i in range(min(len(numbers),10)): # create a loop (only 10 numbers is accepted)
    n = numbers[i]
    if n.isdigit() and int(n) > 0 and int(n) < 50: # making sure that we create a graph only for positive numbers which a less than 50
        bar = int(n) * '=' # turning number into graph
        print(bar) # print result
    else:
        print("?") # print result 