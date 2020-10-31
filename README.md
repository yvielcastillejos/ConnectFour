# ConnectFour
In this repository, I will attempt to make an AI TicTacToe using the minimax algorithm. This serves as an easy review of the Minimax Algorithm. In this game, the player starts first and goes against an AI with 3 level of difficulties. The first level corresponds to a depth of 1 in the minimax algorithm, the second level corresponds to a 2 and the third level corresponds to a 4. Notice how in the 3rd level, the time it takes for the AI to move is longer (This is especially true if I put 5, the AI would take about 30 seconds to make a guess.)

## The Game:
- To run the game, launch ```pyplay.py```

### Level 1 with depth of 1
<img src="https://github.com/yvielcastillejos/ConnectFour/blob/master/L1.gif" height = "500" width = "500">

### Level 2 with depth of 2

<img src="https://github.com/yvielcastillejos/ConnectFour/blob/master/L2.gif" height = 500 width = 500>

### Level 3 with depth of 3

<img src="https://github.com/yvielcastillejos/ConnectFour/blob/master/L3.gif" height = 500 width = 500>

- The gif conversion from video cut off the AI winning; however, for level 3, it was almost impossible to win (as I am really bad at the game).

## Acknowledgement
I used the evaluate function below
[1] https://softwareengineering.stackexchange.com/questions/263514/why-does-this-evaluation-function-work-in-a-connect-four-game-in-java

I followed the pseudo code defined in wikipedia
[2] https://en.wikipedia.org/wiki/Minimax
