# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:02:20 2021

@author: Михаил
"""
# MPLx 7.4	51283
i = names.index(max(names))
names[i], names[-1] = names[-1], names[i]
print(names)
# MPLx 7.4	51257
i = 0
odds = []
while i <= n:
        if i % 2 != 0:
                odds.append(i)
        i += 1
# MPLx 7.4	51258
odds = []
for i in range(m, n + 1):
        if i % 2 != 0:
                odds.append(i)
        i += 1
# MPLx 7.4	51262
new_list = []
for i in my_list:
        if i % 2 == 0:
                new_list.append(i)
        i += 1

# 7.11pp	71438
numbers = input("Enter ten numbers:")
list = []
for i in numbers:
    if (i not in list) and (i != " "):
        list.insert(len(list), i)
print(*list, sep=" ")

# Snakify Assignments

# Sum of Cubes
N = int(input())
i = 1
sum = 0
for i in range(0, N+1):
    sum = sum + (i ** 3)
    i += 1
print(sum)


# Factorial
n = int(input())
f = 1
if n <= 0:
    f = 1
else:    
   for i in range(1, n + 1):    
       f = f * i    
print(f)

# The Number of Words
s = str(input())
w = s.split()
words = len(w)
print(words)

# The Two Halves
s = str(input())
w = s.split()
words = len(w)
print(words)

# Even Indices
a=input()
print(*(a.split()[::2]), sep=" ")

# Even Elements
a = input()
n = a.split()
for i in n:
    i = int(i)
    if i % 2 == 0:
       print(i, end = " ")

# Greater than Previous
a = [int(i) for i in input().split()]
c = []
for i in range(1, len(a)):
    if a[i] > a[i-1]:
        c.append(a[i])
print(*c, sep = " ")


