#Import
import time
from tabulate import tabulate

#rules
def rules():
    rules = """
    🎮 Welcome to Tic-Tac-Toe! 🎮

    🎯 Objective:
    Be the first player to get three of your marks (X or O) in a row!
    Rows, columns, or diagonals - choose wisely!

    👥 Players:
    1. Player 1: X
    2. Player 2: O

    📋 Game Setup:
    Players enter their names.
    The board has 9 positions labeled from 1 to 9:
    
      1 | 2 | 3
      ---------
      4 | 5 | 6
      ---------
      7 | 8 | 9

    🕹️ Gameplay:
    1. Players take turns marking their positions.
    2. Choose an empty position (marked by '-') on your turn.
    3. If occupied, you'll need to try again!

    🏆 Winning:
    First player to align three marks wins!
    Their name will be displayed with a congratulatory message.
    Winning player gets 'X' for next round

    🤝 Tie:
    If all positions are filled without a winner, the game ends in a tie.
    The 'X' and 'O' are switched

    📊 Scoring:
    Each win earns the player one point!
    Scores are shown after each round.

    🔄 Continue/End:
    Players can choose to play another round or end the game.
    The player with the most points at the end is the ultimate winner!

    ✅ Valid Input:
    Enter a number from 1 to 9 for your move.
    Invalid inputs will prompt you to try again!
    """
    
    print(rules)
    print("-----------x-----------x-----------")
rules()

# Global Variables
board = ['-','-','-',
         '-','-','-',
         '-','-','-']
currentPlayer = 'X'
winner = None
gameRunning = True
play = 'y'
player1 = input("Enter name of player 1: ")
player2 = input("Enter name of player 2: ")
xPlayer = player1
oPlayer = player2
wPlayer = None
lPlayer = None
p1score = 0
p2score = 0
roundNum = 1
myData =[player1,p1score],[player2,p2score]


# Print game board
def printBoard(board):
    print(f'ROUND: {roundNum}')
    print(f'Player moved: {currentPlayer}')
    print(board[0]+'|'+board[1]+"|"+board[2])
    print(board[3]+'|'+board[4]+"|"+board[5])
    print(board[6]+'|'+board[7]+"|"+board[8])

# Player input
def playerInput():
    while True:
        
        try:
            inp = int(input("Enter a number from 1-9: "))
            if inp >= 1 and inp <= 9 and board[inp-1] == '-':
                board[inp-1] = currentPlayer
                break
            elif inp not in range(1,9):
                print("Invalid input, please enter a number between 1 and 9.")
            
            else:
                print("Invalid move, try again.")
        except ValueError:
            print("Invalid input")
    printBoard(board)

# Check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] != '-' and board[0] == board[1] == board[2]:
        winner = board[0]
        return True
    elif board[3] != '-' and board[3] == board[4] == board[5]:
        winner = board[3]
        return True
    elif board[6] != '-' and board[6] == board[7] == board[8]:
        winner = board[6]
        return True
    return False

def checkVertical(board):
    global winner
    if board[0] != '-' and board[0] == board[3] == board[6]:
        winner = board[0]
        return True
    elif board[1] != '-' and board[1] == board[4] == board[7]:
        winner = board[1]
        return True
    elif board[2] != '-' and board[2] == board[5] == board[8]:
        winner = board[2]
        return True
    return False

def checkDiag(board):
    global winner
    if board[0] != '-' and board[0] == board[4] == board[8]:
        winner = board[0]
        return True
    elif board[2] != '-' and board[2] == board[4] == board[6]:
        winner = board[2]
        return True
    return False

def checkTie(board):
    global gameRunning,xPlayer,player1,player2,oPlayer
    if "-" not in board:
        printBoard(board)
        print("It is a tie!")
        score()
        xPlayer = player2 if xPlayer == player1 else player1
        oPlayer = player2 if oPlayer == player1 else player1
        gameRunning = False

def checkWin():
    global wPlayer,lPlayer,p1score,p2score
    if checkDiag(board) or checkHorizontal(board) or checkVertical(board):
        if winner == 'X':
            wPlayer = xPlayer
            lPlayer = oPlayer
            if xPlayer == player1:
                p1score+=1
            else:
                p2score+=1
        else:
            wPlayer = oPlayer
            lPlayer = xPlayer
            if oPlayer == player1:
                p1score+=1
            else:
                p2score+=1
        print(f'The winner is {wPlayer}!')
        print("Congratulations")
        return True
    return False

# Switch player
def switchPlayer():
    global currentPlayer
    currentPlayer = 'O' if currentPlayer == 'X' else 'X'
    
#score:
def score():
    global myData
    head = ["Player", "Score"]
    myData =[player1,p1score],[player2,p2score]
    print(tabulate(myData, headers=head, tablefmt="grid"))
    
# Game loop
while True:
    if play == 'y':
        # Reset game state for a new game
        board = ['-','-','-',
                 '-','-','-',
                 '-','-','-']
        currentPlayer = 'X'
        winner = None
        gameRunning = True

        # Print initial board
        score()
        print(f"{xPlayer} is 'X'")
        print(f"{oPlayer} is 'O'")
        print(f'ROUND: {roundNum}')
        print(board[0]+'|'+board[1]+"|"+board[2])
        print(board[3]+'|'+board[4]+"|"+board[5])
        print(board[6]+'|'+board[7]+"|"+board[8])

        while gameRunning:
            playerInput()

            if checkWin():
                gameRunning = False
                xPlayer = wPlayer
                oPlayer = lPlayer
                score()
                break

            checkTie(board)

            if gameRunning:
                switchPlayer()

        play = input("Play another? (y/n): ").lower()
    elif play == 'n':
        score()
        if p1score > p2score:
            print(f"Ultimate Winner: {player1}")
        elif p1score == p2score:
            print("It is a tie!!")
        else:
            print(f"Ultimate Winner: {player2}")
        print("Bye Bye Bye!")
        break
    else:
        print("Invalid input, please enter 'y' or 'n'.")
        play = input("Play another? (y/n): ").lower()


time.sleep(3)
