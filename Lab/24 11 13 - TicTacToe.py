import os
import sys
import time

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def title(gamezero):
    clear()
    print('\n888   d8b        888                   888' +
          '\n888   Y8P        888                   888' +
          '\n888              888                   888' +
          '\n888888888 .d8888b888888 8888b.  .d8888b888888 .d88b.  .d88b' +
          '\n888   888d88P"   888       "88bd88P"   888   d88""88bd8P  Y8b' +
          '\n888   888888     888   .d888888888     888   888  88888888888' +
          '\nY88b. 888Y88b.   Y88b. 888  888Y88b.   Y88b. Y88..88PY8b.' +
          '\n "Y888888 "Y8888P "Y888"Y888888 "Y8888P "Y888 "Y88P"  "Y8888\n'
          )

    while gamezero == True:
        bar = [
            '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░', 
            '▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░', 
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░', 
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░░', 
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░░░░░░░░░░',
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░',
            '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'
            ]

        for i in range(7):
            b = bar[i]
            print ("|" + b + "|", end="\r")
            time.sleep(0.25)
        time.sleep(0.5)
        clear()

        gamezero = False
    
    return gamezero

def gameGrid(grid):  

    numgrid = []
    c = 0
    for r in grid:
        nr = []
        for cell in r:
            if cell == '':
                c += 1
                nr.append(str(c))
            else:
                c += 1
                nr.append('▓')
        numgrid.append(nr)

    print("\n╔"+ ('═'*3 + '╦')*2 + '═'*3 +"╗" + ' '*30 + "╔"+ ('═'*3 + '╦')*2 + '═'*3 +"╗")

    for i in range(3):
        row = []
        numrow = []
        for j in range(3):
            numrow.append(numgrid[i][j])
            if grid[i][j] == '':
                row.append(' ')
            else:
                row.append(grid[i][j])
        

        print('║ ' + row[0] + ' ║ ' + row[1] + ' ║ ' + row[2] + ' ║' + ' '*30 + '║ ' + numrow[0] + ' ║ ' + numrow[1] + ' ║ ' + numrow[2] + ' ║')
        if i < 2:
            print('╠' + ('═'*3 + '╬')*2 + '═'*3 + '╣' + ' '*30 + '╠' + ('═'*3 + '╬')*2 + '═'*3 + '╣')

    print("╚"+ ('═'*3 + '╩')*2 + '═'*3 +"╝" + ' '*30 + "╚"+ ('═'*3 + '╩')*2 + '═'*3 +"╝")

def playermove(grid, symbol):
    valid = False
    while valid == False:
        i = input("\nPlayer [" + symbol + "] > select cell: ")
        if '1' <= i <= '9':
            i = int(i)
            row = (i-1)//3
            col = (i-1)%3
            if grid[row][col] == '':
                grid[row][col] = symbol
                valid = True
            else:
                err_cne(grid)
        elif i == '0' or i == 'q':
            sys.exit(0)
        else:
            err_icn(grid)
    
    clear()
    return grid

def err_cne(grid):
    clear()
    print("\n╔"+("═"*30)+"╗\n║  Cell not empty! Try again.  ║\n║  Press Enter to continue...  ║\n╚"+("═"*30)+"╝")
    input('')
    clear()
    gameGrid(grid)
    return

def err_icn(grid):
    clear()
    print("\n╔"+("═"*30)+"╗\n║     Invalid cell number!     ║\n║  Press Enter to continue...  ║\n╚"+("═"*30)+"╝")
    input('')
    clear()
    gameGrid(grid)
    return

def err_inv():
    clear()
    print("\n╔"+("═"*30)+"╗\n║     Invalid cell number!     ║\n║  Press Enter to continue...  ║\n╚"+("═"*30)+"╝")
    input('')
    clear()
    return

def gamestatus(grid, symbol, gamezero):
    end = False

    if win(grid, symbol):
        clear()
        print("\n╔"+("═"*30)+"╗\n║      Player["+symbol+"] has won!      ║\n║  Press Enter to continue...  ║\n╚"+("═"*30)+"╝")
        input('')
        end = newgame(grid, gamezero, end)
    
    if tie(grid):
        clear()
        print("\n╔"+("═"*30)+"╗\n║          It's a tie!         ║\n║  Press Enter to continue...  ║\n╚"+("═"*30)+"╝")
        input('')                       
        end = newgame(grid, gamezero, end)
    
    return end

def win(grid, symbol):
    w = False

    for r in range(3):
        if(grid[r][0] == symbol and grid[r][1] == symbol and grid[r][2] == symbol):
            w = True
        
    for c in range(3):    
        if(grid[0][c] == symbol and grid[1][c] == symbol and grid[2][2] == symbol):
            w = True

    if(
        (grid[0][0] == symbol and grid[1][1] == symbol and grid[2][2] == symbol) or
        (grid[0][2] == symbol and grid[1][1] == symbol and grid[2][0] == symbol)
    ):
        w = True

    return w

def tie(grid):
    t = True
    for row in grid:
        for col in row:
            if col == '':
                t = False
    return t

def emptygrid(grid):
    clear()
    gameGrid(grid)

    for i in range(3):
        i = 2 - i
        for j in range(3):
            j = 2 - j
            grid[i][j] = '▓'
            time.sleep(0.15)    
            clear()
            gameGrid(grid)

    for i in range(3):
        i = 2 - i
        for j in range(3):
            j = 2 - j
            grid[i][j] = ''
            time.sleep(0.15)    
            clear()
            gameGrid(grid)


def newgame(grid, gamezero, end):
    end = 'miao'
    while not type(end) == bool:
        title(gamezero)
        p = input(' '*11+'Would you like to play again? (Y/N) > ')
        p = p.lower()
        print(end="\r")
        if p == 'y':
            clear()
            print('\n88b 88 888888 Yb        dP      dP""b8    db    8b    d8 888888\n88Yb88 88__    Yb  db  dP      dP   `"   dPYb   88b  d88 88__\n88 Y88 88""     YbdPYbdP       Yb  "88  dP__Yb  88YbdP88 88""\n88  Y8 888888    YP  YP         YboodP dP""""Yb 88 YY 88 888888\n')
            end = False
            time.sleep(1)
            emptygrid(grid)
        elif p == 'n':
            clear()
            print('\n dP""b8  dP"Yb   dP"Yb  8888b.  88""Yb Yb  dP 888888 d8b\ndP   `" dP   Yb dP   Yb  8I  Yb 88__dP  YbdP  88__   Y8P\nYb  "88 Yb   dP Yb   dP  8I  dY 88""Yb   8P   88""   `""\n YboodP  YbodP   YbodP  8888Y"  88oodP  dP    888888 (8)\n')
            end = True
            time.sleep(1.5)
            clear()
        else:
            err_inv()
    
    return end

# MAIN
symbol = 'XO'

grid = []
for i in range(3):
    grid.append(['']*3)

turn = 0
endgame = False
gamezero = True

gamezero = title(gamezero)
gameGrid(grid)

# LOOP
while not endgame:
    if turn == 0:
        turn = 1
    else:
        turn = 0
    
    playermove(grid, symbol[turn])
    gameGrid(grid)
    endgame = gamestatus(grid, symbol[turn], gamezero)