import numpy as np
import matplotlib.pyplot as plt

class ConnectFour:
    def __init__(self):
        self.board = np.zeros((6, 7))
        self.winner = 0 
        self.colors = {1: 'red', 2: 'yellow'}
        self.max_moves = 42 
        self.winner_row = 0 
        self.winner_column = 0
        
    def drop_piece(self, player_number, column):
        if(self.board[:, column] != 0).all() or column > 6 or column < 0:
            return -1, False
        else:
            for i in range(5, -1, -1):
                if self.board[i, column] == 0:
                    self.board[i, column] = player_number
                    return i, True
                
    def check_winner(self, row, column):
        player = self.board[row, column] 
        if column <= 3 and (self.board[row, column: column+4] == player).all():
            self.winner_row = row
            self.winner_column = column 
            return True, "horizontal"
        if row <= 2 and (self.board[row:row+4, column] == player).all():
            self.winner_row = row
            self.winner_column = column
            return True, "vertical"
        if row <= 2 and column <= 3 and (self.board[row:row+4, column:column+4].diagonal() == player).all():
            self.winner_row = row
            self.winner_column = column
            return True, "diagonal (\\)"
        if row <= 2 and column >= 3 and (np.fliplr(self.board[row:row+4, column-3:column+1]).diagonal() == player).all():
            self.winner_row = row
            self.winner_column = column
            return True, "diagonal (/)"
        return False, None
    
    def show_board(self):
        plt.figure(figsize= (6, 7))
        for i in range(6):
            for j in range(7):
                if self.board[i, j] == 0:
                    color = 'white'
                else:
                    color = self.colors[self.board[i, j]]
                plt.scatter(j, i, color= color, s= 100)
        plt.gca().invert_yaxis()
        plt.xticks(range(7), [])
        plt.yticks(range(6), [])
        
        if self.winner != 0:
            print(f"Player {self.winner} wins with a {self.check_winner(self.winner_row, self.winner_column)[1]}line!")
        plt.show()
        
    def play(self, player_number, column):
        if player_number not in [1, 2]:
             raise ValueError("Player number must be 1 or 2")
        row, success = self.drop_piece(player_number, column)
        if success:
            if self.check_winner(row, column)[0]:
                self.winner = player_number
                self.show_board()
                return player_number
            elif np.count_nonzero(self.board) == self.max_moves:
                print("It's a tie!")
                self.show_board()
                return -1
            else:
                self.show_board()
                return None
        else:
            print("Column is full. Please choose another column.")
            return None

def test_game():
    game = ConnectFour()
    game.show_board()
    
    # Scenario 1: Player 1 wins with vertical lines
    game.play(1, 3)
    game.play(2, 4)
    game.play(1, 3)
    game.play(2, 4)
    game.play(1, 3)
    game.play(2, 4)
    game.play(1, 3)
    
    # Scenario 2: Player 2 wins with horizontal lines 
    game.play(1, 0)
    game.play(2, 0)
    game.play(1, 1)
    game.play(2, 0)
    game.play(1, 2)
    game.play(2, 0)
    game.play(1, 3)
    game.play(2, 0)
    
    # Scenario 3: Player 1 wins with diaginal lines (from bottom-left to top-right)
    game.play(1, 0)
    game.play(2, 1)
    game.play(1, 1)
    game.play(2, 2)
    game.play(1, 2)
    game.play(2, 3)
    game.play(1, 2)
    game.play(2, 3)
    game.play(1, 3)
    game.play(2, 4)
    game.play(1, 3)
    
    # Scenario 4 Player 2 wins with diaginal lines (from bottom-right to top-left)
    moves = [(1, 6), (2, 5), (1, 5), (2, 4), (1, 4), (2, 3), (1, 4), (2, 3), (1, 3)]
    for move in moves:
        game.play(*move)
    
test_game()