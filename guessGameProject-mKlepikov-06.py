# -*- coding: utf-8 -*-
"""
Program: Guessing Game Project
Author: Mikhail Klepikov
Description: The game which goal is to guess anumber within a certain range in the fewest number of guesses.
Revisions:
    00 - import random and math
    01 - create input of maximum number and guesser choosen number .
    02 - create a loop to check guesser number
    03 - add number of guesses feature
    04 - add repeating of loop if guesser chose number not in range
    05 - change names of variables

"""
import random
import math
# there are no literal constants
# there are no class definitions
# there are no functions 

# announcement on the next line
print("Guess the Secret Number\n ")

# main program begins on the next line
nMax = int(input("Enter the maximum number in the range: ")) # input maximum number in the range
number = random.randint(1, nMax) # program chose random number
count = int(math.log2(nMax) + 1) # number of guesses
gNumber = int(input(f"\nTry to guess a secret number from 1 to {nMax} (inclusive).\n\nYou have {count} guesses available.\nEnter your guess: ")) # input you guess number
guess = "guesses"
while number != gNumber: # loop to check the number
    count -= 1
    if gNumber != number and count == 0: # if you don't have any guesses and you still not get number
        print(f"\nSorry, no more guesses available.\nThe secret number was {number}.")
        break
    elif gNumber < number and count != 0: # if you guess number is lesser than secret number and you have more number of guesses
        if count == 1:
            guess = "guess"
        print(f"The secret number is greater than {gNumber}.")
        print(f"You have {count} {guess} available.")
        gNumber = int(input("Enter your guess: "))
    elif gNumber > number and count != 0: # if you guess number is greater than secret number and you have more number of guesses
        if count == 1:
            guess = "guess"
        print(f"The secret number is less than {gNumber}.")
        print(f"You have {count} {guess} available.")
        gNumber = int(input("Enter your guess: "))
    if nMax < gNumber or gNumber < 1: # add this part in case guesser accidently chose number not in range
        print("You choose number that not in the range. Choose number once again")
        gNumber = int(input("Enter your guess: "))
        continue
else: # if you get secret number
    print("Correct. Well done!")
    
