# tictactoe_sol.py
"""
Tic-tac-toe game
"""

def display_grid(grid):
    """
    Display the grid.
    Each cell is 3 characters long: a character that identifies the
    status of the cell ('X', 'O', or '.') between two blank spaces
    """

    for i in range(len(grid)):
        row = []
        for j in range(len(grid[i])):
            if grid[i][j] == '':
                row.append(' ')
            else:
                row.append(grid[i][j])
        print(' '+row[0]+' | '+row[1]+' | '+row[2])
        if i < 2:
            print('-'*11)

def moves_grid(grid):
    """
    Return the possible moves on *grid* in a grid with 
    the cell number if the cell is empty in *grid*.
    The cells are identified as:
     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9
     
    Example:
    If in *grid* the cells 1 and 5 are already occupied,
    that is if *grid* is [['X', '', ''], ['', 'O', ''], ['', '', '']]
    the function returns the list [['', 2, 3], [4, '', 6], [7, 8, 9]].
    """

    moves = []
    counter = 0
    for row in grid:
        r = []
        for cell in row:
            counter = counter + 1
            if cell == '':
                r.append(str(counter))
            else:
                r.append('#')
        moves.append(r)
    return moves

            
def player_move(grid, player):
    """
    Read the move of the player.
    Only legal moves in grid are allowed.
    The variable player contains the symbol of the player.
    It modifies the given grid and the resulting grid is returned.
    The cells are identified as:
     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9
    """
    
    # build the grid of the possible moves
    moves = moves_grid(grid)

    legal_move = False
    while not legal_move:
        display_grid(grid)
        print('Please, player ', player, ' input your move as:')       
        display_grid(moves) 
        m = input('Selected move: ')
        if  '1' <= m <= '9':
            m = int(m)
            row = (m-1)//3
            col = (m-1)%3
            if grid[row][col] == '':
                # legal move
                grid[row][col] = player
                legal_move = True
            else:
                print('The cell # ', m, ' is not empty (-', grid[row][col], '-). Try again.')
        else:
            print(m, ' is an invalid cell identifier. Try again.')
    
    return grid

def win(grid, player):
    """
    Test if the grid represents a victory for player.
    """

    # it would be shorter to list all the possible winning conditions than
    # writing the rule using for. However:

    it_wins = False

    # horizontal victory
    for i in range(3):
        it_wins = it_wins or \
                  (grid[i][0] == player and \
                   grid[i][1] == player and \
                   grid[i][2] == player)
        
    # vertical victory
    for i in range(3):
        it_wins = it_wins or \
                  (grid[0][i] == player and \
                   grid[1][i] == player and \
                   grid[2][i] == player)
        
    # diagonal victory
    it_wins = it_wins or\
              (grid[0][0] == player and
               grid[1][1] == player and
               grid[2][2] == player)\
               or \
               (grid[0][2] == player and
                grid[1][1] == player and
                grid[2][0] == player)

    return it_wins

   
def grid_full(grid):
    """
    Test if all the cells of the given grid are not empty.
    """

    full = True
    for row in grid:
        for c in row:
            if c == '':
                full = False
    return full


    
# players symbol
players = 'XO'

# The grid represents the game board.
# It is structured as a 3x3 matrix, that is here represented as
# a 3-element list containing three 3-element lists.
# Each element is a cell and contains the character of one of the players,
# if the cell has been already occupied, or the empty string, otherwise.
# NOTE: the visualization procedure would be simplified if instead of the
#       empty string a blank character is used as placeholder
#       (e.g., ' ', '-',  or '.')

# The grid is initialized as a list of three lists., each containing
# three empty strings
# grid = [['']*3]*3 # this is wrong!!! Three copies of the same list
grid = []
for i in range(3):
    grid.append(['']*3)

# The game is palyed in turns in which the players alternatively
# occupy a cell.

endgame = False
turn = 0 # the player id (0 or 1) that can play in the current turn 

while not endgame:
    # the turn is assigned to the next player
    if turn == 0:
        turn = 1
    else:
        turn = 0
    # alternatively:
    # turn = (turn + 1) % 2 
    # or
    # turn = int(not(turn))

    # player[turn] can move
    grid = player_move(grid, players[turn])
  
    display_grid(grid)

    # test if players[turn] wins
    if win(grid, players[turn]):
        print("\nplayer ", players[turn], " wins!\nCongratulations!!!\n")
        endgame = True

    # test if any other move is possible
    if grid_full(grid):
        print("\nIt's a tie game!\nCongratulations to both!\n")
        endgame = True