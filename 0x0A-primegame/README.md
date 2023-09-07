# 0x0A-primegame
```Algorithm``` ```Python```

## Requirements
### General
* Allowed editors: ```vi```, ```vim```, ```emacs```
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS using ```python3``` (version 3.4.3)
* All your files should end with a new line
* The first line of all your files should be exactly ```#!/usr/bin/python3```
* A ```README.md``` file, at the root of the folder of the project, is mandatory
* Your code should use the ```PEP 8``` style (version 1.7.x)
* All your files must be executable

## Tasks
### Mandatory
**[0-prime_game.py](0-prime_game.py)** - Maria and Ben are playing a game. Given a set of consecutive integers starting from 1 up to and including n, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game. They play ```x``` rounds of the game, where ```n``` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is. Returns: 1 if Maria wins the game, 0 if Maria loses the game. If the winner cannot be determined, return ```None```. Prototype: ```def isWinner(x, nums)```. ```x``` is the number of rounds and ```nums``` is an array of ```n```. ```n``` does not change. For ```n``` and ```x```: ```1 <= x <= 10```, ```1 <= n <= 10**5```. All ```n``` are unique. Returns: 1 if Maria wins the game, 0 if Maria loses the game. If the winner cannot be determined, return ```None```.
```
