#! /usr/bin/python

#Created by Henrique Rauen (rickgithub@hsj.email)
#Last Modified: Wed Jun 14 10:18:16 2023
class Hangman:
    available_letters = ["abcdefghijklmnopqrstuvwxyz"]
    def __init__(self):
        self._possible_words = ["crazyness"]
        *self._word_to_find = self._possible_words
        self._lives = 5
        self._correctly_guessed_letters = ["_"] * len(self._word_to_find)
        self._wrongly_guessed_letters = []
        self._turn_count = 0
        self._error_count = 0

    def start_game(self):
        while self._lives > 0:
            if "_" in self._correctly_guessed_letters:
                play()
            else:
                _well_played()
                return None
        _game_over()

    def _well_played(self):
        print (f"You found the word {self._word_to_find} in {self._turn_count}
               turns with {self._error_count}")

    def _game_over(self):
        print("game over...")

    def _play(self):
        guessed_letter = input("Please guess a letter: ")
        if _guess_validity(guessed_letter):
            if guessed_letter in self._word_to_find:
               _update_hangman(guessed_letter)
            else:
                self._wrongly_guessed_letters.append(guessed_letter)
                self._error_count += 1
                self._lives += -1
        else:
            _play()

    def _update_hangman(self,letter):
        for index, l in enumerate(self._word_to_find):
            if l == letter:
                self._correctly_guessed_letters[index] = letter

    def _guess_validity(self,x)
        x.lower()
        if x.len() == 1 and x in available_letters:
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
