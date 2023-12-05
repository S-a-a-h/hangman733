'''
Hangman Game

This script allows the user to play the hangman game directly from their CLI.
All files associated to this game are coded in Python and stored as (.py). 
This script requires that 'random' be installed with the Python environment which the code is stored in. 

This file can be imported as a class containing the following methods:
    * _check_guess - a protected method which converts the guessed letter to lowercase, 
        checks if the the guess is in the word and checks how many lives are remaining after the guess.
    * _update_word_guessed - a protected method which updates the word with the guess, if correct, or 
        reduces the number of lives left by 1 if incorrect.
    * _lives_left - a protected method which prints remaining number of lives only if the guess is 
        incorrect. 
    * ask_for_input - a public method which asks the user for a single, alphabetical letter as a guess
        and validates it before checking it via _check_guess method and adding the guess to a list of
        previous guesses so as to avoid repitition in the game. 
'''

import random 


#Hangman Class creation
word_list = ['orange', 'kiwi', 'durian', 'rambutan', 'lime']
word = random.choice(word_list)
list_of_guesses = []
'''
Sets the word list from which the computer will randomly choose a word as well as setting an 
empty list which will be appended to as the game goes on.
'''

#Hangman contains 4 methods as of 5/12/23
class Hangman: 
    """
    Hangman Class 
    -------
    This class is used to represent the game, Hangman. 

    Attributes
    -------
    word_list : list
        word_list from which the computer will randomly select a word and keep it hidden until 
        completely guessed
    num_lives : int
        Set to 5 lives in this game
    """
    def __init__(self, word_list, num_lives=5):
        '''
        See help(Hangman) for accurate signature
        '''
        self.word = word
        self.word_guessed = ['_' for _ in self.word]
        self.num_letters = len(set(self.word))
        self.num_lives = num_lives
        self.word_list = word_list
        self.list_of_guesses = list_of_guesses


    def _check_guess(self, guess): #check_guess method
        '''
        This function is used to convert the guess to a a lowercase character, checks that the guess is
        in the word and updates the word's characters' list. 
        If the guess is not in the word's characters' list, _lives_left method is run.

        Args:
            guess (Hangman), the letter to be checked. 

        Returns:
            None.
        '''
        guess = guess.lower()
        if guess in self.word:
            self._update_word_guessed(guess)
        else:
            self._lives_left(guess)


    def _update_word_guessed(self, guess): #update_word_guessed method 
        '''
        This function is used to update the word's characters' list which is to be guessed. For each 
        letter in the word, _ is present in order to hide the spelling of the word, so if the guess 
        matches the hidden letter, the _ is replaced with the guess and the number of letters remaining will
        be reduced by 1 (or however many times the guess matches a letter in the word).

        Args:
            guess (Hangman), the letter to be updated into the word or the guessed_list. 

        Returns:
            None.
        '''
        print(f'Good guess! {guess} is in the word.')
        for _, letter in enumerate(self.word): #for loop in check_guess method that replaces _ with the guessed letter if it's a match
            if letter == guess:
                self.word_guessed[_] = guess
        self.num_letters -= 1


    def _lives_left(self, guess): #lives_left method
        '''
        This function is used to update the user of the number of remaining lives 
        corresponding to incorrect guesses. Each incorrect guess reduces the lives by 1. 

        Args:
            guess (Hangman), the letter to be updated into the guessed_list. 

        Returns:
            None.
        '''
        print(f'Sorry, {guess} is not in the word. Try again. \nYou have {self.num_lives} lives left.')


    def ask_for_input(self): #ask_for_input method
        '''
        This function is used to ask the user for an input which is known as the guess. In the 
        while loop, the guess is validated if it is a single, alphabetical character or, notifies 
        the user if it matches a previous input or, if it is an incorrect guess, runs the code in
        _check_guess method and adds the guess to the list of guesses after which the while loop is
        broken.

        Args:
            None.

        Returns:
            None.
        '''  
        while True:
            guess = input('Enter a single letter: ')
            if not (len(guess) == 1 and guess.isalpha()):
                print('Invalid letter. Please, enter a single alphabetical character.')    
            elif guess in self.list_of_guesses:
                print('You already tried that letter!')
            else:
                self._check_guess(guess)
                self.list_of_guesses.append(guess) #adds incorrect guess to list
                break
                
#aesthetics of the game
print('Welcome to Hangman. Give it your best shot!')
hangman = Hangman(word_list)
hangman.ask_for_input()
print(hangman.word_guessed) 
print(f'There are {hangman.num_letters} remaining letters in the word.') 

#TODO: Allow input to run continuously until game over (lives_left = 0)