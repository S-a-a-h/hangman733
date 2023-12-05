'''
Hangman Game

This script allows the user to play the hangman game directly from their CLI.
All files associated with this game are coded in Python and stored as (.py) files. 
This script requires that 'random' be installed in the Python environment which the code is stored in. 

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
    * _play_game - a protected method which ensures that if the number of lives is 0, the game is lost. 
        If not, this method checks that the number of remaining letters is more than 0 in order 
        for the game to continue until a win or loss.
'''

import random 


word_list = ['orange', 'kiwi', 'durian', 'rambutan', 'lime']
word = random.choice(word_list)
list_of_guesses = []
'''
    * word_list - sets the word list from which the computer will randomly choose a word - this can 
        be changed by the user if necessary, and all other code will run according to the user-modified 
        list.
    * word - instructs computer to randomly select a word from the word_list using installed package: 
    'random'.
    * list_of_guesses - creates an empty list which will be appended to as the game is initiated and played.
'''

class Hangman: 
    '''
    Hangman Class 
    -------
    This class is used to represent the game, Hangman. 

    Attributes
    -------
    self.word : str
        the word which the user must guess
    self.word_guessed : list
        a list representing the word which is hidden by '_' for each letter to be guessed by user
    self.num_letters : int 
        the number of unique letters in the word yet to be guessed
    self.num_lives : int
        the number of lives remaining
    self.word_list : list 
        a list containing all words from which the computer will pick one at random to be guessed
    self.list_of_guesses : list 
        a list to keep track of all the previous guesses made by the player 

    Methods
    -------
    __init__(self, word_list, num_lives=5):

        Parameters
        -------
        word_list : list
            word_list from which the computer will randomly select a word and keep it hidden until 
            completely guessed
        num_lives : int
            Set to 5 lives in this game

    _check_guess(self, guess):

        Parameters
        -------
        guess : str
            A lower-case, singlular, alphabetical character

     _update_word_guessed(self, guess):

        Parameters
        -------
        guess : str
            A lower-case, singlular, alphabetical character

    _lives_left(self, guess):

        Parameters
        -------
        guess : str
            A lower-case, singlular, alphabetical character

    ask_for_input(self):

        Parameters
        -------
        None.

    _play_game(self):
        
        Parameters
        -------
        None.
    '''
    print('\nWelcome to Hangman. Give it your best shot!\n')
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


    def _check_guess(self, guess): 
        '''
        This method is used to convert the guess to a a lowercase character, checks that the guess is in 
        the word and updates the word's character list. If the guess is not in the word's character list, 
        _lives_left method is run.

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


    def _update_word_guessed(self, guess):
        '''
        This method is used to update the word's character list which is to be guessed. For each 
        letter in the word, _ is present in order to hide the spelling of the word, so if the guess 
        matches any hidden letter, the _ is replaced with the guess and the number of letters remaining 
        will be reduced by 1 (or by number of times that the guess matches a letter in the word). Notifies
        the user of number of the remaining letters left to be guessed. 

        Args:
            guess (Hangman), the letter to be updated into the word, if correct, or added the guessed_list, 
            if incorrect. 

        Returns:
            None.
        '''
        print(f'Good guess! {guess} is in the word.')
        for _, letter in enumerate(self.word):
            if letter == guess:
                self.word_guessed[_] = guess
        self.num_letters -= 1
        print(self.word_guessed) 
        print(f'There are {self.num_letters} remaining letters in the word.') 


    def _lives_left(self, guess):
        '''
        This method is used to notify the user of the number of remaining lives left corresponding 
        to incorrect guesses. Each incorrect guess reduces the user's lives by 1, after having begun 
        the game with 5 lives. Notifies the user of number of the remaining letters left to be guessed. 

        Args:
            guess (Hangman), the letter to be updated into the guessed_list. 

        Returns:
            None.
        '''
        self.num_lives -= 1
        print(f'Sorry, {guess} is not in the word. Try again. \nYou have {self.num_lives} lives left.')
        print(self.word_guessed) 
        print(f'There are {self.num_letters} remaining letters in the word.') 


    def ask_for_input(self):
        '''
        This method is used to ask the user for an input which is known as the guess. In the 
        while loop, the guess is validated if it is a single, alphabetical character, or, notifies 
        the user if it matches a previous input. If it is an incorrect guess, _check_guess method is 
        called and this incorrect guess is added to the list of previous guesses. Then, the while loop
        is broken.

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
                self.list_of_guesses.append(guess)
            break
                

    def _play_game(self):
        '''
        This method is used to play the game. In the while loop, the number of lives is evaluated so 
        if all lives are lost, the game is lost and the while loop is broken. However, if sufficient
        lives are remaining, the user is prompted to continue playing the game. If all letters in the 
        word have been guessed, the game is won and thw while loop is broken.   

        Args:
            None.

        Returns:
            None.
        '''  
        while True:
            if self.num_lives <= 0:
                print('You lost...')
                break
            elif self.num_letters > 0:
                self.ask_for_input()
            else:
                print('Congratulations! You have won the game!')
                break


help(Hangman)
game = Hangman(word_list)
game._play_game()
'''
    * help() - built-in Python function that provides accurate signature for argument passed in. 
        help(Hangman) provides docstrings before initating the game.
    * game - sets an instance of the Hangman class with word_list as it's parameter.
    * game._play_game() - calls the _play_game method from the Hangman class. Initiates the game.
'''

