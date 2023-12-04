import random

#List of fruits
word_list = ['orange', 'kiwi', 'durian', 'rambutan', 'lime']
print(word_list)

#Create the random.choice method and pass the word_list variable into the choice method + assigned to word var.
word = random.choice(word_list)
print(word)

guess = input('Enter a single letter: ')

#Create an if statement that checks if the length of the input is equal to 1 and the input is alphabetical.
if len(guess) == 1 and guess.isalpha():
    print('Good guess!')
else:
    print('Oops! That is not a valid input.')