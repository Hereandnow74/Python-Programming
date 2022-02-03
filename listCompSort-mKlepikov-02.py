'''
Program: Simple List Comprehension & Sorting
Author: Klepikov Mikhail
Description: Complete the list comprehension exercises here.
Any functions you write must also have
(1) a docstring that describes the input parameters and the value returned
(2) at least two significant tests that verify the function
Revision:
    00 - Complete these exercises
    01 - Use a docstrings to describe the input parameters and additional checking 
'''
###### 1. List comprehension analysis
### Code
def linc(a,b=2):
    return [x + b for x in a if type(x) is int] # for loop where for every 'x' value in 'a' list if 'x' is int we count 'x + b'
x = [1,2,'3',4]
y = linc(x)  # [3,4,6]
z = linc(x,1) # [2,3,5]
print(x)
print(y)
print(z)
'''
Checking result:
print(x) give us [1, 2, '3', 4]
print(y) give us [3, 4, 6]
print(z) give us [2, 3, 5]
'''
###### 2. the listInc() function
def listInc(a):
    return [x + 1 for x in a if type(x) is int] # for loop where for every 'x' value in 'a' list if 'x' is int we count 'x + 1'
### listInc() tests
assert listInc([7,2,4,8]) == [8,3,5,9], 'listInc failed [7,2,4,8]'
assert listInc([9,-1,0.0,5]) == [10,0,6], 'listInc failed [9,-1,0.0,5]'
print('listInc is OK\n')
'''
Checking result:

print(listInc([7,2,4,8])) give us [8, 3, 5, 9]
print(listInc([9,-1,0.0,5])) give us [10, 0, 6]
'''
###### 3. the listOut() function
def listOut(a):
    return [print(x) for x in a] # for loop where we print every 'x' value in 'a' list one by one
### listOut() tests
listOut([7,2,'OK',8])
print()
listOut([[1,2],2.0,'$',8])
print()
'''
Checking result:
7
2
OK
8

[1, 2]
2.0
$
8
'''
###### 4. statements that move items between lists
### end of A to beginning of B
a,b = [1,2,3], [4,5,6]
b.insert(0,a.pop()) # using insert method we remove an item a from 'a' list and insert it in 'b' list at the specified index '0'
print(a,b)
### beginning of A to end of B
a,b = [1,2,3], [4,5,6]
b.append(a.pop(0)) # using pop() method we remove an item at a specified index value from a list in this case it index '0'
print(a,b,'\n')
'''
Checking result:
[1, 2] [3, 4, 5, 6]
[2, 3] [4, 5, 6, 1] 
'''
###### 5a. the rotateForward() function
def rotateForward(a):
### YOUR CODE HERE
    return [a[(i - 1) % len(a)]
               for i, x in enumerate(a)] # using for i, x in enumerate(a) loop, we count a[(i - 1) % len(a)]
### rotateForward() tests
assert rotateForward([1,2,3,4]) == [4,1,2,3], 'rotateForward failed'
print('rotateForward ok\n')

'''
Checking result:
print(rotateForward([1,2,3,4])) give us [4, 1, 2, 3]
'''
###### 5b. the rotateBackward() function
def rotateBackward(a):
    return [a[(i + 1) % len(a)]
               for i, x in enumerate(a)] # using for i, x in enumerate(a) loop, we count a[(i + 1) % len(a)]
### rotateForward() tests
assert rotateBackward([1,2,3,4]) == [2,3,4,1,], 'rotateBackward failed'
print('rotateBackward ok\n')

'''
Checking:
print(rotateBackward([1,2,3,4])) give us [2, 3, 4, 1]
'''

###### 6. Analysis of iSort()
def iSort(x,n=2):
    return sorted(x,key=lambda a: a[n]) # finishing functuin with sorted() function that returns a sorted list of specified parameters.
x = [(1,'one','uno'),(2,'two','dos'),(3,'three','tres')]
print(iSort(x))
print(iSort(x,1))
print()

'''
Checking:
print(iSort(x)) give us [(2, 'two', 'dos'), (3, 'three', 'tres'), (1, 'one', 'uno')]
print(iSort(x,1)) give us [(1, 'one', 'uno'), (3, 'three', 'tres'), (2, 'two', 'dos')]
'''

###### 7. Length sorting
z = ['bzz','z','cz','azzz']
z.sort(reverse = True) # using sort() method with (reverse = True) to sort in reverse to get ['z', 'cz', 'bzz', 'azzz'] 
print(z,'\n')

'''
Checking:
print(z,'\n') gave us ['z', 'cz', 'bzz', 'azzz'] 
'''
###### 8. the backSort() function
def backSort(a):
    return sorted(a,key=lambda a: a[-1]) # finishing functuin with sorted() function that returns a sorted list of specified parameters.
### backSort() tests
assert backSort(['red','yellow','blue','green','black']) == \
       ['red', 'blue', 'black', 'green', 'yellow'], 'backSort FAILED'
print('backSort OK')

'''
Checking:
print(backSort(['red','yellow','blue','green','black'])) gave us ['red', 'blue', 'black', 'green', 'yellow']
'''

