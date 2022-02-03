'''
Program: Ultimate Language Translation Project
Author: Mikhail Klepikov
Description: Program that translate words using a vocabulary file from english to french or from french to english.
Revisions: 
    00 - open vocabulary
    01 - create main loop to translate the words
    02 - create loop to add words in vocabulary
    03 - add functions
    04 - add vocabulary creation if file not exist
'''
# there are no import
# there are no literal constants
# there are no class definitions

# Announcement on the next line
print("\nProgram to translate words from English to french and vice-versa")

# Main program begins on the next line
try: # open vocabulary.txt file
        open('vocabulary.txt')
        
except FileNotFoundError: # if vocabulary.txt file not exist, program will create it
        print(f'File vocabulary.txt is not exist. File will be created...')
        open('vocabulary.txt',"a")
        
with open('vocabulary.txt',mode ='r') as f: # program opens the vocabulary file and then reads the data using the readlines() method.  
        data = f.readlines()
        newDict = dict([item.split() for item in data if not item =='\n']) # convert data in dictionary

# Functions
def ExtendVocabulary(newDict,w1,w2): # function took words and them into dictionary
        newDict[w1] = w2
        newDict[w2] = w1
        return newDict

def addWords(filename,newDict): # function to add words in .txt file
        with open(filename,'a') as f:
                for item in list(newDict)[-2:-1]:
                        f.write(f'\n{item} {newDict[item]}')

# Main loop starts here                
while True:
        try:
                translate = input("\nPlease, Enter the word to translate: ").lower() # input word for translation
                if not translate:                                        # break, if word not chosen
                        print("Exiting the program...")
                        break
                elif  translate in  newDict.keys():                    # If word in english, print translation in french
                        englishWord = newDict[translate]
                        print(f"English word \'{translate}\' is translated as \'{englishWord}\' in French.")
                        continue
                elif  translate in  newDict.values():                    # If word in french, print translation in english
                        frenchWord = list(newDict.keys())[list(newDict.values()).index(translate)]
                        print(f"French word \'{translate}\' is translated as \'{frenchWord}\' in English.")
                        continue
                else:                                            # If word not exist in vocabulary print the messege
                        print(f"The word \'{translate}\' is not in vocabulary.") 
                # Ask user if he/she would like to add word to vocabulary        
                response = input(f"Add \'{translate}\' word to the vocabulary? Answer: <yes> or <no> ... ").lower() # Add lowercase
                if response == "yes":                         # User select <yes>
                                langResponse = input(f"What language \'{translate}\' word is? Answer: <English> or <French> ... ").lower() # add lowercase
                                if langResponse == "english":                     # Word in english, execute this loop
                                        newFrench = input(f"What is the French translation for \'{translate}\'? ").lower() # Add lowercase
                                        newDict = ExtendVocabulary(newDict,translate,newFrench)    # Using ExtendVocabulary function
                                        addWords('vocabulary.txt',newDict) # Using addWords function
                                        print(f'Word \'{translate}\' and it`s translation was added to vocabulary.')
                                        continue
                                elif langResponse == "french":                    # Word in french, execute this loop
                                        newEnglish = input(f"What is the English translation for \'{translate}\'? ").lower() # Add lowercase
                                        newDict = ExtendVocabulary(newDict,newEnglish,translate) # Using ExtendVocabulary function
                                        addWords('vocabulary.txt',newDict) # Using addWords function
                                        print(f'Word \'{translate}\' and it`s translation was added to vocabulary.')
                                        continue
                                else:
                                        print(" \nUnexpected Language..") # Wrong language was choosen by user
                elif response == "no": # User selected <no>
                        print(f" \n\'{translate}\' was not added to vocabulary.") 
                else: # Wrong answer by user
                        print(f" \nPlease, choose <yes> or <no> next time...")
        except:
                break
