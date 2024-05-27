# Connect Four Game Implementation

Connect Four (also known as Connect 4, Four Up, Plot Four, Find Four, Captain's Mistress, Four in a Row, Drop Four, and Gravities in the Soviet Union) is a two-player connection board game, in which the players choose a color and then take turns dropping colored tokens into a seven-column, six-row vertically suspended grid. The pieces fall straight down, occupying the lowest available space within the column. The objective of the game is to be the first to form a horizontal or vertical line of four of one's own tokens. For this lab, the winner will be only the first one who forms a horizontal or vertical line. The diagonal will be a stretch goal.

We will build a Connect Four game with the help of the `numpy` and `matplotlib` libraries. Player one will be represented as number 1, and player two as number 2.

## Class Definition

We will create a class called `ConnectFour` with the following methods:

### Constructor

Attributes:
- `board`: A 6x7 array of zeros representing the game board.
- `winner`: An attribute to keep track of the winner (0 if no winner).

### Methods

#### `drop_piece`

Parameters:
- `player_number`: The player number (1 or 2).
- `column`: The column where the player will put the token.

Functionality:
- Find the first available place in the column to put the token.
- Return the row and a boolean indicating if there is a place available.

#### `check_winner`

Parameters:
- `row`: The row of the last placed token.
- `column`: The column of the last placed token.

Functionality:
- Check if there is a winner by forming a horizontal or vertical line.
- Return a boolean indicating if there is a winner.

#### `show_board`

Functionality:
- Display the board using `imshow()` from `pyplot`.
- Ensure each player's token has a different color.

#### `play`

Parameters:
- `player_number`: The player number (1 or 2).
- `column`: The column where the player will drop the token.

Functionality:
- Check if the player number is valid (1 or 2).
- Drop a piece.
- Check if there is a winner.
- Display the board.