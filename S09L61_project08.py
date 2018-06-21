# Tic Tac Toe Game ;-)

### First to design the board, which has 3x3 space so 9 spaces
# We define a empty list with 9 spaces in a very nice way
board = ["   " for i in range(9) ] 



## Also we need to somehow print the board list in a more simmilar way than in the game so we create a function for it

def print_board():
    row1 = "| {} | {} | {} |".format(board[0],board[1],board[2])
    row2 = "| {} | {} | {} |".format(board[3],board[4],board[5])
    row3 = "| {} | {} | {} |".format(board[6],board[7],board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()

## We create a function for occupying the space in the board, meaning a move from one of the uiserrs
def player_move(icon):

    #First we translate the number of the player
    if "X" in icon:
        player_number = 1
    else:
        player_number = 2
        
    print("Player{} is your turn ...".format(player_number))
    choice =  int(input("Enter your move (1-9): ").strip())
    if board[choice -1] == "   ":
        board[choice -1 ] = icon
    else:
        print()
        print("That place is taken!")
    

# We also need one function which will check if there is a victory from either one of the players
def is_victory(icon):
    # how to know if one user won? So wee need all the row1 or row2 or row3 or positions (0,4,8) or (2,4,6) or (0,3,6) or (1,4,7) or (2,5,8)
    if \
       ( icon in board[0] and icon in board[1] and icon in board[2] ) or \
       ( icon in board[3] and icon in board[4] and icon in board[5] ) or \
       ( icon in board[6] and icon in board[7] and icon in board[8] ) or \
       ( icon in board[0] and icon in board[4] and icon in board[8] ) or \
       ( icon in board[2] and icon in board[4] and icon in board[6] ) or \
       ( icon in board[0] and icon in board[3] and icon in board[6] ) or \
       ( icon in board[1] and icon in board[4] and icon in board[7] ) or \
       ( icon in board[2] and icon in board[5] and icon in board[8] ):
        return True
    else:
        return False
    

# Also it can happen that the game is a draw so we will need to check it
def is_draw():
    # Draw is happening when there wasn't a win and there is no empty spaces in the board
    if "   " in board:
        return False
    else:
        return True
        

## here we go this is the game loop
while True:
    print_board()
    player_move(" X ")
    print_board()
    
    if is_victory("X"):
        print("Player X wins ... ! Congratulations !!")
        break # So we finish the loop and go out from the game
    #At we check if is a draw
    elif is_draw():
        print_board()
        print("It was a draw, both players WIN :) ")
        break
        
    player_move(" O ")
    if is_victory("O"):
        print_board()
        print("Player O wins ... ! Congratulations !!")
        break # So we finish the loop and go out from the game
    elif is_draw():
        print("It was a draw, both players WIN :) ")
        break

    

        
