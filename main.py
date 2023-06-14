#! /usr/bin/python

#Created by Henrique Rauen (rickgithub@hsj.email)
#Last Modified: Wed Jun 14 17:43:44 2023

import utils.game as game

#Run the demo version with only 4 words
"""hang = game.Hangman()
hang.start_game()"""

#Sample run the demo with 6 lives
"""hang = game.Hangman(5)
hang.start_game()"""

#Sample run the game in full mode (with expansive list of words
"""hang = game.Hangman()
hang.start_game(True)"""

#Sample run the game in full mode (with expansive list of words and 10 lives
hang = game.Hangman(7)
hang.start_game(True)
