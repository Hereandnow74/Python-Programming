'''
Program: Language Translation, using Lists
Author: Klepikov Mikhail
Description: This program used to translate the words from English to French and vice-versa
Revision:
    00 - Announcements and cretion of the lists with english and french words
    01 - Asking user to the input word
    02 - Printing result if word in dictionary
    03 - Adding "if...else" to add word in dictionary
'''
# there are no import module
# there are no literal constants
# there are no class definitions
# there are no functions

# announcement on the next line
print("Program to translate words from English to French and vice-versa")

# main program begins on the next line
english = ['chicken','salt','apple','earth','bean','water','milk']
french = ['poulet','sel','pomme','terre','haricot','eau','lait']

# create a while loop to translate words
while True:
    words = input("\nEnter an English or French words to translate: ") #input word for translation
    if not words:
        print("Exiting ...") # Exiting from program if no words inputed by user
        break
    try: # using try except to continue program
        if words.lower() in english: # word is in english
            print(f"The English word '{words}' is '{french[english.index(words)]}' in French")
        elif words.lower() in french: # word is in french
            print(f"The French word '{words}' is '{english[french.index(words)]}' in English")
        else: # word does not exist in english and french 'dictionary'.
            print(f"The word '{words}' was not found in English or French word lists")
            response = input(f"Would you like to add '{words}' to the lists? <y>es or <n>o? ") # choosing between <y> and <n>
            if response.lower() == 'y': # if choose is <y>, we doing another if loop to add word in dictionary
                language = input(f"What language is '{words}' in? <E>nglish or <F>rench? ")
                if language.lower() == 'e': # If word in English, then add in French dict.
                    response = input(f"What is the French word for '{words}'? ")
                    english.append(words) # adding {words} in english dictionary
                    french.append(response) # adding {response} in french dictionary
                elif language.lower() == 'f': # If word in French, then add in English dict.
                    response = input(f"What is the English word for '{words}'? ")
                    french.append(words) # adding {words} in french dictionary
                    english.append(response) # adding {response} in english dictionary
                else: # if we answer incorrect, then stop the program
                    print("Exiting ...")
    except:
        break
