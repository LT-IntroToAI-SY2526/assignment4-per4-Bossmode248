# Assignment 4 - Writeup

In assignment 4 we created a basic tic tac toe game so that we could learn object oriented programming. Respond to the following questions.

## Reflection Questions

1. What was the most difficult part to tic-tac-toe?
The hardest part of TicTacToe for me was trying to figure out why the program wasn't making the board an attribute and how to make all the win conditions. I just couldn't figure it out. Most of the other stuff I didn't struggle much with, just using my notes for help and previous knowledge of java.
2. Explain how you would add a computer player to the game.
by adding a while loop with in the game while loop that detects when its their turn. Maybe make all its inputs completely random using the number generator. 

3. If you add a computer player, explain (doesn't have to be super technical) how you might get the computer player to play the best move every time. *Note - I am not grading this for a correct answer, I just want to know your thoughts on how you might accomplish it.
I would make it the bot detects when a win condition is near compleation either for them or the player, and place based off that. Maybe give it a while loop constantly going through the win conditions, showing which place is best to go either for the bot to win or to block the player. If the player places at index 2, the bot will find all conditions that can be won using index 2, then play based off that. 