# The Hangman game

## This is a simple command line 'Hangman' game.
You will need to guess the correct word within the maximum number of lives in order to win.

## Installation
This game requires python 3.10.6 or higher (possibly compatible with previous versions but untested).\
In order to install you can either clone this repository or download the files separately. It's important to note that if you decide to download the files separately, their directory tree must remain unaltered.

### Features
- This game has a demo mode that uses a 4 word list and has a full mode where the words are read from a file with almost 1000 words (included in this distribution). You can add new words to the file as long as each word occupy a single line.
- You can change the game difficulty by changing the number of lives.
### Usage
```Hangman.start_game()```\
The ```start_game()``` function has 2 optional parameters: ```full``` (boolean) and  ```lives``` (int). Default is ```full=False``` and ```lives=5```. If you want to run the game in full mode use ```start_game(full=True)```, to change the number of lives use ```start_game(lives=5)```.\
The file ```main.py``` comes with 3 sample usages of the game. If you run the file as is, it will run in full mode with 5 lives.
In order to run the file just type ```python3 main.py```

## Made by Henrique Rauen
Created on 14/jun/2023 as part of the becode AI operator training
