from IPython.display import clear_output
import random

# To display the board
def print_board(board):
    clear_output()
    print("***************** GOOD LUCK ***********************")
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(" | |")
    print("-----")
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(" | |")
    print("-----")
    print(board[1]+'|'+board[2]+'|'+board[3])
    print(" | |")
 

# To let the players choose their markers

def player_choose_marker():
    marker_p1 = ' '
    
    # To repeat the loop till a valid entry is entered
    while marker_p1 !='X' and marker_p1 != 'O':
      marker_p1 = input("Player 1, Please choose 'X' or 'O'")
    
    # To assign the marker chosen by Player 1 to Player 1 and the other one to Player 2
    if marker_p1 == 'X':
      marker_p2 = 'O'
    elif marker_p1 == 'O':
      marker_p2 = 'X'
        
    return(marker_p1, marker_p2)

# To get the player's marker to make a mark on the board

def place_marker(board, marker,position):
    board [position] = marker
    
# To check if a player has won

def check_for_win(board,mark):  
      
      flag = False 
    
# row check

      i = 1
      while i <= 9:
    
        if(board[i] == board[i + 1] == board [i+2] == mark):
          flag = True
          break
        i = i + 3
    
    
# column check

      i = 1

      while i <= 3:
    
        if (board[i] == board [i+3] == board[i+6] == mark): 
          flag = True
          break
        i = i + 1
    
# diagonals check

      if (board[1]== board[5]== board[9] == mark) or (board[3] == board[5] == board[7]==mark):
        flag = True
            
      return flag
    
    
# To randomly decide which player goes first
def who_plays_first():

    if random.randint(0,1) == 0:
        return("Player 1")
    else:
        return("Player 2")
    
    
# To check if there is empty space on the board
def empty_space(board, position):
    return board[position] == " "

# To check if the board is full at the moment

def full_board_check(board):
    flag = True
    for i in range(1,10):
        if empty_space(board,i):
            return False
    return True

# To let the players choose the positions they want to play

def player_choice(board):
    position = 0
    
    while position not in range(1,10) or not empty_space(board,position):
        position = int(input("Please choose a position 1 - 9 "))
    
    return position

# To give the players an option to either continue to a new game, or to quit the game, once a game is over

def replay():
    choice =  ""
    while choice !='Y' and choice !='N':
        choice = input("Please enter Y if you want to continue or N if you do not wish to continue")
    return choice

print("Welcome to TIC TAC TOE ")
while True:
  
  # Initializing the board with blank spaces
  board = [" "] * 10 

  # Letting the players choose their markers
  p1_marker, p2_marker = player_choose_marker()
  
  # To let the game randomly choose which player is to go first and let the players know  
  turn = who_plays_first()
  print(turn, " will go first")

  # To check if the players are ready to play
  play_game = input("Ready to play? y or n?")
  
  if play_game == 'y':
    game_on = True
  elif play_game == 'n':
    game_on = False
  
  while game_on:    
    if turn == 'Player 1':
        # display board
        print_board(board)
        
        # player choice for position
        position = player_choice(board)
        
        # Place the marker on the position
        place_marker(board,p1_marker,position)
        
        #Check if Player 1 has won
        if check_for_win(board, p1_marker):
            print_board(board)
            print("Player 1 has won ")
            game_on = False
        
        # To check for a tie
        elif full_board_check(board):
            print_board(board)
            print("The game is a tie")
            game_on = False
        else:
            turn = 'Player 2'
    else:
            
        print_board(board)
        
        # Player choice for position
        position = player_choice(board)
        
        # Place the marker on the position
        place_marker(board,p2_marker,position)
        
        #Check if Player 2 has won
        if check_for_win(board,p2_marker):
            print_board(board)
            print("Player 2 has won ")
            game_on = False
        
        # To check for a tie
        elif full_board_check(board):
            print_board(board)
            print("The game is a tie")
            game_on = False
        else:
            turn = 'Player 1'
        
   
  if replay() == 'N':
    break
        