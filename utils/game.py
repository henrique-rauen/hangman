#! /usr/bin/python

#Created by Henrique Rauen (rickgithub@hsj.email)
#Last Modified: Thu Jun 15 08:47:06 2023
from random import choice
from os import system
from os import name

class Hangman:
    """Class Hangman. Has a single public method to start the game:
    'start_game'. Has an optional parameter 'lives', default set to 5"""
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    def __init__(self):
        self._wrongly_guessed_words = []
        self._turn_count = 0
        self._error_count = 0
        self._draw_list = ["\n---|\n   |\n   |\n   |\n   |\n___|",
        "\n---|\nó  |\n   |\n   |\n   |\n___|",
        "\n---|\nó  |\n/  |\n   |\n   |\n___|",
        "\n---|\nó  |\n/\ |\n   |\n   |\n___|",
        "\n---|\nó  |\n/\ |\n/  |\n   |\n___|",
        "\n---|\nó  |\n/\ |\n/\ |\n   |\n___|"]

    def _set_up_words(self, full_mode):
        """Set up the list of possible words and choose one to be the one
        played in this game"""
        if full_mode:
            word_list = open("utils/word_list.txt")
            self._possible_words =[a[:-1] for a in  word_list.readlines()]
            word_list.close()
        else:
            self._possible_words = ["becode", "learning",
                                    "mathematics", "sessions"]
        *self._word_to_find, = choice(self._possible_words).lower()
        self._correctly_guessed_words = ["_"] * len(self._word_to_find)

    def start_game(self, full_mode=None, lives=5):
        self._lives = lives
        """Public. Start and run the game"""
        self._set_up_words(full_mode) #Chooses a word based on parameter 'list'
        while self._lives > 0:
            if "_" in self._correctly_guessed_words:
                self._play()
            else:
                self._well_played()
                return None
        self._show_status()
        self._game_over()

    def _well_played(self):
        """Local. Present the winning message and run required end
        of game commands"""
        print (f"You found the word {''.join(self._word_to_find).upper()} in {self._turn_count} turns with {self._error_count} errors!")
        self._play_again()

    def _game_over(self):
        """Local. Present the losing message and run required end
        of game commands"""
        print("game over...")
        print(f"Your word was {''.join(self._word_to_find)}")
        self._play_again()

    def _play_again(self):
        if input("Would you like to play again? (y/n) ") == "y":
            lives = input("How many lives do you want? ")
            if lives.isnumeric():
                self.__init__()
                self.start_game(True,int(lives))
            else:
                print("Oooops, not a number")
                self._play_again()

    def _play(self):
        """Local. runs a player turn"""
        self._show_status()
        guess = input("Please guess a letter or type a word to guess it: ").lower()
        if guess.isalpha():
            self._turn_count += 1
            if len(guess) == 1:
                if guess in self._word_to_find:
                    self._update_hangman(guess)
                elif guess not in self._wrongly_guessed_words:
                    self._wrongly_guessed_words.append(guess)
                    self._error_count += 1
                    self._lives += -1
            else:
                if guess == "".join(self._word_to_find):
                    self._correctly_guessed_words = self._word_to_find
                else:
                    self._error_count += 1
        else:
            #Player made invalid input, starts over the turn
            self._play()

    def _update_hangman(self,letter):
        """Local. Updates the hangman with the new found letter"""
        for index, l in enumerate(self._word_to_find):
            if l == letter:
                self._correctly_guessed_words[index] = letter

    def _show_status(self):
        """Local. Show the status of the current game (the hangman status)"""
        system("cls" if name == "nt" else "clear")
        status = " ".join(self._correctly_guessed_words).upper()
        if self._lives <= 5:
            print(self._draw_list[-self._lives-1])
        print(f"You have already guessed these letters: {' '.join(self._wrongly_guessed_words).upper()}")
        print(f"You still have {self._lives} lives and the status of your guess is: {status}")

    def _guess_validity(self, x):
        """Local. Checks the validity of the user guess, must either (be single letter and
        not have been guessed before) OR be a word guess"""
        if len(x) == 1 and x in self.available_letters:
            if (x not in self._wrongly_guessed_words and
                x not in self._correctly_guessed_words):
                validity = True
            else:
                validity = False
        elif x.isalpha():
            validity = True
        else:
            validity =  False
        return validity
