# Clue-Solver
Algorithm for solving the mystery in the board game, Clue.  
Instructions for usage:  
1. Enter the number of players. The program will create the players player1, player2, etc. depending on how many players you have, excluding yourself. Designate each of your opponents as player1, player2, etc.
1. Then, you will be prompted to enter your own cards. When entering cards, remove all prefixes (e.g. Mr.), and write in lower case. Type done when finished
1. For every suggestion made, enter the player that is suggesting (e.g. player1, player2, etc.). If it is not yourself, enter the 3 cards that were suggested. Then, enter each player that revealed a card other than yourself. Type done when finished.
1. If you are making a suggestion, type "me" when asked who is suggesting. Then type the card that you suggest and the player that gave you that card, or none. Do this 3 times (once for each card suggested)
1. The show keyword: When asked "Who is suggesting?", you can type "show", which will print a table containing each card and the players that could possible have that card
