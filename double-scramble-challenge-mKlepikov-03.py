'''
Program: Double Scrambled Words 
Author: Klepikov Mikhail
Description: This program used to unscramble words.
Revision:
    00 - Create function to rotate each list in z and include list comprehention in it
    01 - Sort the Tuples and provide sort key 
    02 - Print the result
--------------------------------------------------------------------
    Double Scrambled Words
    The variable z contains four encoded common English words.
    Each word is 5 letters long.
    Reveal the words by writing Python code to sort the list by the
    integer value in each tuple.
    Use lambda constructs and list comprehensions where possible.
    *** Note that unlike the previous problem, each item in z is a list.
        Each list has an integer that encodes the position in a different
        location in the list.  The characters are in the correct order but
        you will need to rotate each list so the integers are in the same
        location in each list.  The most convenient location would be at
        index zero because then, you would not need to provide a sort key.
    Example: rotate z[0] so it looks like this: [3, 't', 'n','s', 'a']
'''

z = [['s', 'a', 3, 't', 'n'],['h', 'b', 'c', 1, 'p'],
     ['h', 'y', 'c', 'k', 5],[4, 'c', 'e', 'i', 'l'],
     ['o', 'a', 'h', 2, 'i']]

# Step 1:   Rotate each list in z so the integer is in the zero position
#           without changing the order of the characters.
wordList=[]
for word in z:
    for s in word:
        if type(s) is int:
            k=[word[(x-(len(word)-word.index(s)))% len(word)] for x,y in enumerate(word)]
            wordList.append(k)
            
# Step 2:   Sort the lists based on the integer value in each.
wordList=sorted(wordList,key= lambda a: a[0])
# Step 3:   Use a list comprehension to create a list of characters
#           for each word.
# Stpe 4:   Use the join() method to create a string for each of the
#           four words and print them.

print(f'{"".join([ a[1] for a in wordList])}')
print(f'{"".join([ a[2] for a in wordList])}')
print(f'{"".join([ a[3] for a in wordList])}')
print(f'{"".join([ a[4] for a in wordList])}')
