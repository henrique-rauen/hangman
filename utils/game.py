#! /usr/bin/python

#Created by Henrique Rauen (rickgithub@hsj.email)
#Last Modified: Wed Jun 14 17:44:15 2023
from random import choice

class Hangman:
    """Class Hangman. Has a single public method to start the game:
    'start_game'. Has an optional parameter 'lives', default set to 5"""
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    def __init__(self, lives=5):
        self._lives = lives
        self._wrongly_guessed_letters = []
        self._turn_count = 0
        self._error_count = 0

    def _set_up_words(self, use_list):
        """Set up the list of possible words and choose one to be the one
        played in this game"""
        if use_list:
            word_list = open("utils/word_list.txt")
            self._possible_words =[a[:-1] for a in  word_list.readlines()]
            word_list.close()
        else:
            self._possible_words = ["becode", "learning",
                                    "mathematics", "sessions"]
        *self._word_to_find, = choice(self._possible_words).lower()
        self._correctly_guessed_letters = ["_"] * len(self._word_to_find)

    def start_game(self, use_list=None):
        """Public. Start and run the game"""
        self._set_up_words(use_list) #Chooses a word based on parameter 'list'
        print(f"You have {self._lives} lives, good luck!")
        while self._lives > 0:
            if "_" in self._correctly_guessed_letters:
                self._play()
            else:
                self._well_played()
                return None
        self._game_over()

    def _well_played(self):
        """Local. Present the winning message and run required end
        of game commands"""
        print (f"You found the word {''.join(self._word_to_find)} in {self._turn_count} turns with {self._error_count} errors!")

    def _game_over(self):
        """Local. Present the losing message and run required end
        of game commands"""
        print("game over...")
        print(f"Your word was {''.join(self._word_to_find)}")

    def _play(self):
        """Local. runs a player turn"""
        guessed_letter = input("Please guess a letter: ").lower()
        if self._guess_validity(guessed_letter):
            self._turn_count += 1
            if guessed_letter in self._word_to_find:
                print("Good Guess!")
                self._update_hangman(guessed_letter)
            else:
                print("Bad Guess... :(")
                self._wrongly_guessed_letters.append(guessed_letter)
                self._error_count += 1
                self._lives += -1
            self._show_status()
        else:
            #Player made invalid input, starts over the turn
            self._play()

    def _update_hangman(self,letter):
        """Local. Updates the hangman with the new found letter"""
        for index, l in enumerate(self._word_to_find):
            if l == letter:
                self._correctly_guessed_letters[index] = letter

    def _show_status(self):
        """Local. Show the status of the current game (the hangman status)"""
        status = " ".join(self._correctly_guessed_letters)
        print(f"You still have {self._lives} lives and the status of your guess is: {status}")

    def _guess_validity(self, x):
        """Local. Checks the validity of the user guess, must be single letter and
        not have been guessed before"""
        if len(x) == 1 and x in self.available_letters:
            if (x not in self._wrongly_guessed_letters and
                x not in self._correctly_guessed_letters):
                validity = True
            else:
                print("This letter has already been guessed! Try again.")
                validity = False
        else:
            print("Incorrect input, must be a single valid letter")
            validity =  False
        return validity
