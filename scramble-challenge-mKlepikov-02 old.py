'''
Program: Scrambled Words 
Author: Klepikov Mikhail
Description: This program used to unscramble words.
Revision:
    00 - Sort the Tuples and provide sort key
    01 - Create a list comprehention
    02 - Print the result
--------------------------------------------------------------------
    Scrambled Words
    The source code below defines four encoded common English words.
    Each word is 7 letters long.
    Reveal the words by writing Python code to sort the list by the
    integer value in each tuple.
    Use lambda constructs and list comprehensions in your solution.
'''
z = [('v', 'c', 'l', 6, 'r'), ('i', 'a', 'i', 4, 't'),
     ('a', 'f', 'g', 1, 'p'), ('h', 'n', 'r', 3, 's'),
     ('e', 'e', 'a', 7, 'e'), ('c', 'i', 'o', 2, 'a'),
     ('e', 'n', 'l', 5, 'u')]


# Step 1:   Sort the tuples based on the integer value in each.  Use a
#           lambda construct to provide the sort key.

zSort = sorted(z, key = lambda a: a[3]) # sort the list with lambda

# Step 2:   Use a list comprehension to create a list of characters
#           for each word.

compList = [[each[a] for each in zSort] for a in range(len(zSort[0]))] # Use a list comprehension to create a list of characters

# Step 3:   Use the join() method to create a string for each of the
#           four words and print them.

# print 4 words
print(''.join(compList[0]), ''.join(compList[1]), ''.join(compList[2]), ''.join(compList[4]))
