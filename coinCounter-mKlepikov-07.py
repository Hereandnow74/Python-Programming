# -*- coding: utf-8 -*-
"""
Program: Coin Counter Project
Author: Mikhail Klepikov
Description: 
    Revisions:
    00 - input coin string
    01 - turn input into lowercase and count coins
    02 - append count amount of each coin to numbers list
    03 - append values of each coin to values list
    04 - append values of each coin to values list
    05 - create for loop to print values from coins, values, numbers, amount lists
    06 - print results in form of table
"""

# there are no import module
# there are no literal constants
# there are no class definitions
# there are no functions 

# announcement on the next line
print("Program to count coins and calculate values")

# main program begins on the next line
coin = input("Enter coin string: ")
coin_l = coin.lower() # turn string into lowercase string
pennies = coin_l.count("p") # sorting pennis and concatenating with the string.
nickels = coin_l.count("n") # sorting nickels and concatenating with the string.
dimes = coin_l.count("d") # sorting dimes and concatenating with the string.
quarters = coin_l.count("q") #s orting quarters and concatenating with the string.
halfdollars = coin_l.count("h") # sorting half-dollars and concatenating with the string.

# create list of Numbers
numbers = []
numbers.append(pennies) # add pennies to numbers list
numbers.append(nickels) # add nickels to numbers list
numbers.append(dimes) # add dimes to numbers list 
numbers.append(quarters) # add quarters to numbers list
numbers.append(halfdollars) # add halfdollars to numbers list

# create list of Coins
coins = []
coins.append('Pennies')
coins.append('Nickles')
coins.append('Dimes')
coins.append('Quarters')
coins.append('Half-dollars')

# assign value to each coin
pennies_value = 0.01
nickels_value = 0.05
dimes_value = 0.10
quarters_value = 0.25
halfdollars_value = 0.50

# create list of Values
values = []
values.append(pennies_value) # add pennies_value to values list
values.append(nickels_value) # add nickels_value to values list
values.append(dimes_value) # add dimes_value to values list
values.append(quarters_value) # add quarters_value to values list
values.append(halfdollars_value) # add halfdollars_value to values list

# calculate Amounts of each coin
pennies_amount = pennies * pennies_value # calculate amount of Pennies
nickels_amount = nickels * nickels_value # calculate amount of Nickles
dimes_amount = dimes * dimes_value # calculate amount of Dimes
quarters_amount = quarters * quarters_value # calculate amount of Qurters
halfdollars_amount = halfdollars * halfdollars_value # calculate amount of Half-dollars

# create list of amount
amount = []
amount.append(pennies_amount) # add to list amount of Pennies
amount.append(nickels_amount) # add to list amount of Nickles
amount.append(dimes_amount) # add to list amount of Dimes
amount.append(quarters_amount) # add to list amount of Qurters
amount.append(halfdollars_amount) # add to list amount of Half-dollars

totalAmount = sum(amount) # calculate Total amount

# print results
# print header with 'Coin Counter Report' in center
print("\n====================================\n",
      f"{'Coin Counter Report':^35}",
      "\n====================================\n")
# print names of columns
print(f"{'Coin':<15}{'Value'}{'Number':^10}{'Amount':>5}")
print(f"{'====':<15}{'====='}{'======':^10}{'======':>5}")

# loop take values from the lists print them with adjustments
for item_coin, item_value, item_number, item_amount in zip(coins, values, numbers, amount):
    print(f"{f'{item_coin:<15}${item_value:.2f}{item_number:^10}${item_amount:5.2f}':>30}")
    
# print Total amount with adjustments
print(f"{f'Total amount: ${totalAmount:5.2f}':>36}")


