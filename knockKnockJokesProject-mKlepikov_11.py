'''
Program: Knock-Knock Jokes
Author: Mikhail Klepikov
Description: The program that interacts with a user at the Python console to tell "knock-knock" jokes
Revision:
    00 - create input of numbers of joke we want to use.
    01 - create loop to tell jokes
    02 - create list of knock knock jokes
    03 - print start of joke
    04 - create while loop for middle part of joke
    05 - use random and pop function to be able shuffle the jokes and make sure jokes do not repeat 
    06 - create while loop for climax part of joke
    07 - add punctuation stripping from response
    08 - make little print changes and finish program
    09 - second response answer correction
'''
# import function random
import random
# there are no literal constants
# there are no class definitions

# create a list of knock knock jokes that contain start, middle and climax of joke
knock_jokes = [
    {'start': 'Knock-knock!', 'middle': 'Nobel', 'climax': "Nobel…that’s why I knocked!\n"},
    {'start': 'Knock-knock!', 'middle': 'Tank', 'climax': "You’re welcome.\n"},
    {'start': 'Knock-knock!', 'middle': 'Luke', 'climax': "Luke through the peep hole and find out.\n"},
    {'start': 'Knock-knock!', 'middle': 'Figs', 'climax': "Figs the doorbell, it’s not working!\n"},
    {'start': 'Knock-knock!', 'middle': 'Annie', 'climax': "Annie thing you can do, I can do too!\n"},
    {'start': 'Knock-knock!', 'middle': 'Cow says', 'climax': "No, a cow says mooooo!\n"},
    {'start': 'Knock-knock!', 'middle': 'Hal', 'climax': "Hal will you know if you don’t open the door?\n"},
    {'start': 'Knock-knock!', 'middle': 'Alice', 'climax': "Alice fair in love and war\n"},
    {'start': 'Knock-knock!', 'middle': 'Says', 'climax': "Says me!\n"},
    {'start': 'Knock-knock!', 'middle': 'Honey bee', 'climax': "Honey bee a dear and get that for me please!\n"}
]

# announcement on the next line
print(f'Ready to tell a knock-knock joke!\n\nThere are {len(knock_jokes)} available.')

# main program begins on the next line
number = int(input(f'How many jokes would you like me to tell? ')) 
if number == 1: # check do we tell 1 joke or many jokes, or none at all
    print(f'\nReady to tell {number} joke!\n')
elif number < 1:
    print(f'\nInvalid. Please choose more that 0 number of jokes\n')
else:
    print(f'\nReady to tell {number} jokes!\n')

for i in range(number): # creating look for telling jokes
    random.shuffle(knock_jokes) # make program give random joke
    randomJoke = knock_jokes.pop(0) # pop function return the first random joke, so that jokes does not repeat
    print(randomJoke['start']) # print start of joke
    
    suggestion = ["whos there", "who's there", "who is there", "who there", "whos there?", "who's there?", "who is there?", "who there?"] # add suggestion responses which are ok to use, for program to work.
    while True: # create loop to add response of player and check if it is ok for use.
        response = input().lower() # change all characters to lowercase
        if response in suggestion: # add if to check if response if ok
            print(randomJoke['middle']) # print joke "middle"
            break
        else:
            print(f'The correct response is "Who\'s there?".\nTry again.') # if the response different give advise what to input

    while True: # second loop to finish joke
        response = input().lower() # change all characters to lowercase
        if response == randomJoke['middle'].lower() + ' who?': # check if response once again gave us result we need.
            print(randomJoke['climax']) # if result are ok, then we print 'climax' of joke.
            break
        else:
            print(f"I don't understand {response} Please try again.")# if the response different give advise what to input

print('Thanks for playing!') #print the last line and end of program
