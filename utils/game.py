#! /usr/bin/python

#Created by Henrique Rauen (rickgithub@hsj.email)
#Last Modified: Wed Jun 14 11:29:41 2023
class Hangman:
    available_letters = "abcdefghijklmnopqrstuvwxyz"
    def __init__(self):
        self._possible_words = ["crazyness"]
        *self._word_to_find, = self._possible_words[0]
        self._lives = 5
        self._correctly_guessed_letters = ["_"] * len(self._word_to_find)
        self._wrongly_guessed_letters = []
        self._turn_count = 0
        self._error_count = 0

    def start_game(self):
        print(self._word_to_find)
        while self._lives > 0:
            if "_" in self._correctly_guessed_letters:
                self._play()
            else:
                self._well_played()
                return None
        self._game_over()

    def _well_played(self):
        print (f"You found the word {''.join(self._word_to_find)} in {self._turn_count} turns with {self._error_count} errors!")

    def _game_over(self):
        print("game over...")

    def _play(self):
        guessed_letter = input("Please guess a letter: ").lower()
        if self._guess_validity(guessed_letter):
            self._turn_count += 1
            if guessed_letter in self._word_to_find:
                self._update_hangman(guessed_letter)
            else:
                self._wrongly_guessed_letters.append(guessed_letter)
                self._error_count += 1
                self._lives += -1
                self._show_status()
        else:
            self._play()

    def _update_hangman(self,letter):
        for index, l in enumerate(self._word_to_find):
            if l == letter:
                self._correctly_guessed_letters[index] = letter
        self._show_status()

    def _show_status(self):
        print(f"The status of your guess is: {self._correctly_guessed_letters}")

    def _guess_validity(self,x):
        x.lower()
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
