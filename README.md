# The Hangman game

## This is a simple command line 'Hangman' game.
You will need to guess the correct word within the maximum number of lives in order to win.

## Installation
This game requires python 3.10.6 or higher (possibly compatible with previous versions but untested).\
In order to install you can either clone this repository or download the files separately. It's important to note that if you decide to download the files separately, their directory tree must remain unaltered.

### Features
- This game has a default demo mode that uses a 4 word list and has a full mode where the words are read from a file with almost 1000 words (included in this distribution). You can add new words to the file as long as each word occupy a single line.
- You can change the game difficulty by changing the number of lives.
### Usage
You can run the game on "demo mode" by instantiating a Hangman object ```hang=Hangman``` and calling ```hang.start_game()```. If you want to run the game in full mode use ```Hang.start_game(True)```, to change the number of lives instantiate the ```Hangman``` class with the number of desired lives as a parameters, for example ```hang = Hangman(5)```.\
The file ```main.py``` comes with 4 sample usages of the game, from demo mode with default number of lives (5) to full mode with an arbitrary number of lives. If you run the file as is, it will run in full mode with 7 lives.
In order to run the file just type ```python3 main.py```

## Made by Henrique Rauen
Created on 14/jun/2023 as part of the becode AI operator training
