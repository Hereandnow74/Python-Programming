# -*- coding: utf-8 -*-
"""
Program: Cypher Project
Author: Mikhail Klepikov
Description: Create an encryption scheme where each letter in the alphabet is represented by a number.
Revisions:
    00 - input word which you want to encrypt
    01 - add lower case 
    01 - create a list @number
    02 - create a loop to add integer that represent character in the list
    03 - using ord() to get integer of character and add it in the list
    04 - print result
"""

# there are no import module
# there are no literal constants
# there are no class definitions
# there are no functions 

# announcement on the next line
print("Program to encode a word.")
# main program begins on the next line
word = input("Enter a word: ") # input the word you want to encode
wordlow = word.lower() # returns copy of word string as a string where all characters are lower case.
number = [] # create a list 
for char in wordlow: # loop for to put number of characters in the list
    encr = ord(char) - 97 # using ord() function to get a number in the list
    '''
    ord() - Given a string representing one Unicode character, 
    return an integer representing the Unicode code point of that character.
    For example, ord('a') returns the integer 97 and ord('€') (Euro sign) returns 8364. 
    This is the inverse of chr().
    '''
    number.append(encr) # adding integer representing the character in the list
print("The code for “" + word + "” is:", *number, sep = " ") # print the list, without brackets, while separating it with space