# -*- coding: utf-8 -*-
"""
Program: Letter Grades Project
Author: Mikhail Klepikov
Description: This program compute a letter grade from a numerical score.
Revisions:
    00 - function to perform the calculation of what letter grade the number is
    01 - input the percent of grade
    02 - print result
"""

# there are no import module
# there are no literal constants
# there are no class definitions
def letterGrade(score): # function perform the calculation what letter grade the score is. 
    if score >= 95: # score more than or equal 95 will return "A+"
        return "A+"
    elif score >= 90: 
        return "A"
    elif score >= 85:
        return "A-"
    elif score >= 80:
        return "B+"
    elif score >= 75:
        return "B"
    elif score >= 70:
        return "B-"
    elif score >= 65:
        return "C+"
    elif score >= 60:
        return "C"
    elif score >= 55:
        return "C-"
    else: # score does not fall in parameters in if or elif statement category, so the score is "F"
        return "F"
# announcement on the next line
print("Program to compute a letter grade for a numerical score")
# main program begins on the next line
score = float(input("Enter the numerical score: ")) # put the number of score in percent

if score >= 100 or score < 0:
        print("Invalid")
else:
    print("The letter grade for", score, "percent is", letterGrade(score), ".") # print result




