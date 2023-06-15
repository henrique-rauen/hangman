#! /usr/bin/python

#Created by Henrique Rauen (rickgithub@hsj.email)
#Last Modified: Thu Jun 15 08:54:57 2023

import utils.game as game
hang = game.Hangman()

#hang.start_game() #Run the demo version with the default 5 lives

#hang.start_game(lives=6) #Sample run the demo with 6 lives
#hang.start_game(False, 6) #Sample run the demo with 6 lives


#hang.start_game(True, 10) #Sample run the full game with 10 lives

hang.start_game(full_mode = True, lives = 5) #Sample run the game in full mode and 5 lives
