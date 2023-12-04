import random 

#creates list of words from which a random is selected by computer 
word_list = ['orange', 'kiwi', 'durian', 'rambutan', 'lime']
word = random.choice(word_list)

#asks user for input 
def ask_for_input():
    while True:
        guess = input('Enter a single letter: ')
        if len(guess) == 1 and guess.isalpha():
            print(guess)
            break
        else: 
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

#checks if the guessed letter is in the word
def check_guess(guess):
    guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')


ask_for_input()

