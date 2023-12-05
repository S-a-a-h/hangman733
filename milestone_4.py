import random 

#creates list of words from which a random is selected by computer 
word_list = ['orange', 'kiwi', 'durian', 'rambutan', 'lime']
word = random.choice(word_list)

#ask_for_input function
def ask_for_input():
    while True:
        guess = input('Enter a single letter: ')
        if len(guess) == 1 and guess.isalpha():
            print(guess)
            break
        else: 
            print('Invalid letter. Please, enter a single alphabetical character.')
    check_guess(guess)

#check_guess function
def check_guess(self, guess):
    guess.lower()
    if guess in word:
        print(f'Good guess! {guess} is in the word.')
    else:
        print(f'Sorry, {guess} is not in the word. Try again.')


#milestone_4.py: class creation

#Hangman Class creation
word_list = ['orange', 'kiwi', 'durian', 'rambutan', 'lime']
word = random.choice(word_list)
list_of_guesses = []

#Hangman contains 4 methods as of 5/12/23
class Hangman: 
    def __init__(self, word_list, num_lives=5):
        self.word = word
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = list_of_guesses


    def check_guess(self, guess): #check_guess method
        guess = guess.lower()
        if guess in self.word:
            self.update_word_guessed(guess)
        else:
            self.lives_left(guess)


    def update_word_guessed(self, guess): #update_word_guessed method 
        print(f'Good guess! {guess} is in the word.')
        for _, letter in enumerate(self.word): #for loop in check_guess method that replaces _ with the guessed letter if it's a match
            if letter == guess:
                self.word_guessed[_] = guess
        self.num_letters -= 1


    def lives_left(self, guess): #lives_left method
        print(f'Sorry, {guess} is not in the word. Try again. \nYou have {self.num_lives} lives left.')


    def ask_for_input(self): #ask_for_input method
        while True:
            guess = input('Enter a single letter: ')
            if not (len(guess) == 1 and guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')    
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self.check_guess(guess)
                self.list_of_guesses.append(guess)
                break
                

print('Welcome to Hangman. Give it your best shot!')
hangman = Hangman(word_list)
hangman.ask_for_input()
print(hangman.word_guessed) 
print(f'There are {hangman.num_letters} remaining letters in the word.') 

