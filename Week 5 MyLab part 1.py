# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:27:54 2021

@author: Михаил
"""

# 2.2.13	51286
sum = 0
for i in range(1, n+1, distance):
	sum += i
    
# 2.2.13	51268
is_ascending = True
for i in range(1, len(numbers)):
    if numbers[i] >= numbers[i-1]:
        is_ascending = True
    else:
        is_ascending = False

# 2.2.13	51269
is_prime = True
for i in range(2,n):
    if (n % 2) == 0:
        is_prime = False
    else:
        is_prime = True

# MPLx 4-1	51863
((x >= "0") and (x <= "9")) or ((x >= "A") and (x <= "F")) or ((x >= "a") and (x <= "f"))

# MPLx 4-1	51864
not (x >= "A" and x <= "Z")
# MPLx 4-1	51865
not x.isalpha()
# MPLx 6-1	51148
max(population1, population2)
# MPLx 6-1	51149
max(max(population1, population2), max(population3, population4))

