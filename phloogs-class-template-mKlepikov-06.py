'''
Program: Dr. Phloog's Class Project
Author: Mikhail Klepikov
Purpose: Program to calculate grades for Dr. Phloog
         Drops lowest 1 out of every 3 grades and
         computes the letter grade (X < 80%, Z >90%, for Y everyone else)
Revisions: 
    00 - calculate how many grades we need to exclude and sort the grades list
    01 - exclude the appropriate number of low grades
    02 - create loop to calculate sum of grades
    03 - compute the average by dividing sum by lenght of fGrades list
    04 - create if/elif/else function to get result
    05 - return result
'''

def findGrade(grades):
    # ENTER YOUR CODE HERE
    # it should compute the average grade after lowest
    # 1 out of 3 grades have been dropped and 
    # a letter grade based on the average.
    # use the float variable "average" for the average
    # and the string variable "letter" for the grade
    
	exclude = (len(grades) // 3) # calculate how many grades we need to exclude as 1 out of 3 grades have been dropped
	grades.sort() # Sort grades to get increasing order of grades in list
	fGrades = grades[exclude:] # create new lesst by slicing excluded marks from grades list
	
	sum = 0 # create sum and define it as zero
	for grade in fGrades: # create loop to get the sum of grades in fGrades list
		sum += grade
	
	average = float(sum / len(fGrades)) # calculate average using sum of grades and length of fGrades list
	
	if average < 80: # using if/elif/else we define the letter grade (less than 80 = X, more than 90 = Z and between 80 and 90 = Y)
		letter = "X"
	elif average > 90:
		letter = "Z"
	else:
		letter = "Y"
	return (average, letter) # THIS RETURNS YOUR RESULTS

'''
DO NOT MODIFY ANY OF THE CODE BELOW
WHEN YOU RUN THE PROGRAM YOUR RESULTS SHOULD BE ...
 80.00 --> Y 
 75.00 --> X 
 91.86 --> Z 
 79.86 --> X 
 85.17 --> Y 

'''
print('Program to calculate grades for Dr. Phloog\n')
# CODE TO TEST THE FUNCTION
grades = []
grades.append([50,100,60]) # [80.00,'Y']
grades.append([50,100,50,50,100,50,50,100,50]) # [75.00,'X']
grades.append([65,100,22,89,0,100,92,78,87,97]) # [91.86,'Z']
grades.append([90,70,60,100,65,95,27,55,79,60]) # [79.86,'X']
grades.append([65,100,22,89,45,92,78,87]) # [85.17,'Y']
for item in grades:
    grade = findGrade(item)
    print(f"{grade[0]:6.2f} --> {grade[1]} ")   
