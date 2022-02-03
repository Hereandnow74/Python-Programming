'''
Program: Language Translation, 
Author: Klepikov Mikhail
Description: This program used to translate the words from English to French, Spanish and German and uses dictionaries instead of lists.
Revision:
    00 - Announcements and cretion of the dictionary with words, colors and translation
    01 - Asking user to the input word and chose language of translation
    02 - Printing result if word and language are right
'''
# there are no import module
# there are no literal constants
# there are no class definitions
# there are no functions

# announcement on the next line
print("Language Translator")

# main program begins on the next line
colors = {} # create empty dictionary
colors['red'] = {} # add key 'red' pairs with empty dictionary
colors['red'].update({'french':'rouge'}) # update with french
colors['red'].update({'spanish':'rojo'}) # update with spanish
colors['red'].update({'german':'rot'}) # update with german
# add green
colors['green'] = {} # add key 'red' pairs with empty dictionary
colors['green'].update({'french':'vert'}) # update with french
colors['green'].update({'spanish':'verde'}) # update with spanish
colors['green'].update({'german':'grun'}) # update with german
# add yellow
colors['yellow'] = {} # add key 'red' pairs with empty dictionary
colors['yellow'].update({'french':'jaune'}) # update with french
colors['yellow'].update({'spanish':'amarillo'}) # update with spanish
colors['yellow'].update({'german':'gelb'}) # update with german
# add blue
colors['blue'] = {} # add key 'red' pairs with empty dictionary
colors['blue'].update({'french':'bleu'}) # update with french
colors['blue'].update({'spanish':'azul'}) # update with spanish
colors['blue'].update({'german':'blau'}) # update with german

# create a while loop to translate words
while True:
    print(f"Available English words are: {'; '.join(colors)}")
    words = input("\nPlease enter a color in English: ") #input word for translation
    try: # using try except to continue program
        if words.lower() in colors.keys(): # word is in colors dictionary
                print(f"\nAvailable language translations are: {'; '.join(colors['red'])}")
                language = input("\nPlease enter a language from the list: ") # input word for translation
                if words.lower() == 'blue' and language.lower() == 'french': # create if and elif loop to check words and language
                    print("works")
                    print(f'\nThe word "{words}" in {language.capitalize()} is ' + colors['blue'].get('french')+ '.\n')
                    break
                elif words.lower() == 'blue' and language.lower() == 'spanish':
                    print(f'\nThe word "{words}" in {language.capitalize()} is ' + colors['blue'].get('spanish')+ '.\n')
                    break
                elif words.lower() == 'blue' and language.lower() == 'german':
                    print(f'\nThe word "{words}" in {language.capitalize()} is ' + colors['blue'].get('german')+ '.\n')
                    break
                elif words.lower() == 'green' and language.lower() == 'french':
                    print(f'\nThe word "{words}" in {language.capitalize()} is ' + colors['green'].get('french')+ '.\n')
                    break
                elif words.lower() == 'green' and language.lower() == 'spanish':
                    print(f'\nThe word "{words}" in {language.capitalize()} is ' + colors['green'].get('spanish')+ '.\n')
                    break
                elif words.lower() == 'green' and language.lower() == 'german':
                    print(f'\nThe word "{words}" in {language.capitalize()} is ' + colors['green'].get('german')+ '.\n')
                    break
                elif words.lower() == 'yellow' and language.lower() == 'french':
                    print(f'\nThe word "{words}" in {language.capitalize()} is ' + colors['yellow'].get('french')+ '.\n')
                    break
                elif words.lower() == 'yellow' and language.lower() == 'spanish':
                    print(f'\nThe word "{words}" in {language.capitalize()} is ' + colors['yellow'].get('spanish')+ '.\n')
                    break
                elif words.lower() == 'yellow' and language.lower() == 'german':
                    print(f'\nThe word "{words}" in {language.capitalize()} is ' + colors['yellow'].get('german')+ '.\n')
                    break
                elif words.lower() == 'red' and language.lower() == 'french':
                    print(f'\nThe word "{words}" in {language.capitalize()} is ' + colors['red'].get('french')+ '.\n')
                    break
                elif words.lower() == 'red' and language.lower() == 'spanish':
                    print(f'\nThe word "{words}" in {language.capitalize()} is ' + colors['red'].get('spanish')+ '.\n')
                    break
                elif words.lower() == 'red' and language.lower() == 'german':
                    print(f'\nThe word "{words}" in {language.capitalize()} is ' + colors['red'].get('german')+ '.\n')
                    break
    except:
        break
