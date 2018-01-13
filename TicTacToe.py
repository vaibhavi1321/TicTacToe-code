#Welcome to tic tac toe game, I am working with python 3 
#step 1. Write a function which print a board for developing this game. So, get a 3 by 3 representation
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print('         |        |        ')
    print('      '+board[7]+' |    '+board[8]+'  |     '+board[9]+'   ')
    print('-------------------------')
    print('        |         |        ')
    print('     '+board[4]+' |    '+board[5]+'   |   '+board[6]+'   ')
    print('-------------------------')
    print('        |         |        ')
    print('     '+board[1]+' |    '+board[2]+'   |    '+board[3]+'   ')
#Step 2. Write a function which will take player input and mark it as 'X' or 'O'
def player_input():
    marker=' '
    while not (marker=='O' or marker=='X'):
        marker=input("player 1: Do you want X or O:").upper()
        if marker=='X':
            return ('X','O')
        else:
            return('O','X')
#Step 3. Write a function which assigns marker at desired position in a board
def place_marker(board,marker,position):
    board[position]=marker
#Step 4. Write a function which will check if marker will won or not
def win_check(board,marker):
    return ((board[7]==marker and board[8]==marker and board[9]==marker) or
           (board[4]==marker and board[5]==marker and board[6]==marker) or
           (board[1]==marker and board[2]==marker and board[3]==marker) or
           (board[1]==marker and board[4]==marker and board[7]==marker) or
           (board[2]==marker and board[5]==marker and board[8]==marker) or 
           (board[3]==marker and board[6]==marker and board[9]==marker) or 
           (board[1]==marker and board[5]==marker and board[9]==marker) or 
           (board[7]==marker and board[5]==marker and board[3]==marker))

#Step 5. Write a function to check randomly that which player goes first
import random
def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"
#Step 6. Check whether board has any space available freely or not
def space_check(board,position):
    return board[position]==' '
#Step 7. Write a function to check whether board is full or not
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
#Step 8. Ask player to enter next position to give a mark 
def player_choice(board):
    position=' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board,int(position)):
        position=input("Choose next move to enter position from [1-9]:")
    return int(position) #This is important to casting as the value it will get from the  '1 2 3 4 5 6 7 8 9'.split() will convert it into list of string values so to convert it into integer we need to do casting
#Step 9. Ask player if they want to replay
def replay():
    return input("Do you wanna play again? Enter Yes or No: ").lower().startswith('y')

#Step 10. Call all the function print("Welcome, Tic Tac Toe") while True: theBoard=[' ']*10 player1_mark, player2_mark=player_input() #it will call function at step 2 turn=choose_first() #it will call function at step 5, To choose which player will go first print(turn + "will go first") game_on=True while game_on:

    #Here, if statement will work for Player 1
    if turn=="Player 1": #Make sure the "Player 1" string should match the string in function at step 5 (Important)
        display_board(theBoard) #Go to Step 1
        position=player_choice(theBoard) #Go to Step 8
        place_marker(theBoard,player1_mark,position) #Go to step 3
        if win_check(theBoard,player1_mark): #Go to Step 4
            display_board(theBoard)
            print("Congratulations, Player 1 won the game!!")
            game_on=False
        else:
            if full_board_check(theBoard): #Go to Step 7
                display_board(theBoard)
                print("The game is a draw")
                break
            else:
                turn="Player 2"  #Make sure the "Player 2" string should match the string in function at step 5 (Important)
    #NOTE: Else statement is for Player 2, And code will be same as if statement above. However, only change value from Player1_mark to Player2_mark
    else:
        if turn=="Player 2": #Make sure the "Player 2" string should match the string in function at step 5 (Important)
            display_board(theBoard) #Go to Step 1
            position=player_choice(theBoard) #Go to Step 8
            place_marker(theBoard,player2_mark,position) #Go to step 3
            if win_check(theBoard,player2_mark): #Go to Step 4
                display_board(theBoard)
                print("Congratulations, Player 2 won the game!!")
                game_on=False
            else:
                if full_board_check(theBoard): #Go to Step 7
                    display_board(theBoard)
                    print("The game is a draw")
                    break
                else:
                    turn="Player 1"  #Make sure the "Player 1" string should match the string in function at step 5 (Important)

if not replay():
    break