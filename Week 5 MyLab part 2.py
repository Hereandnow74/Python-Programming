# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 16:02:20 2021

@author: Михаил
"""
# MPLx 7.4	51283

# MPLx 7.4	51257

# MPLx 7.4	51258

# MPLx 7.4	51262


# 7.11pp	71438
numbers = input("Enter ten numbers:")
list = []
for i in numbers:
    if (i not in list) and (i != " "):
        list.insert(len(list), i)
print(*list, sep=" ")






