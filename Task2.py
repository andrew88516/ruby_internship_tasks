class XO_game:
    
    '''In this task I used the conversion of the provided two-dimensional array 
    into a one-dimensional one, and went through the predetermined winning 
    combinations using the indexes of the new one-dimensional array'''
    
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    
    def __init__(self, board):
        self.board = []
        for row in board:
            for i in row:
                self.board.append(i)
    
    def get_winner(self):
        for (x, y, z) in XO_game.winning_combinations:
            state = self.board
            if state[x] == state[y] and state[y] == state[z] and (state[x] == 'X' or state[x] == 'O'):
                return state[x]
        return "''"
        
game1 = XO_game([['X','',''], ['','X',''], ['O','','O']])
game2 = XO_game([['','X',''], ['X','X',''], ['O','O','O']])


print(game1.get_winner())
print(game2.get_winner())
