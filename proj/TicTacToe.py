#logan cannon
#tictactoe
#11/11/2019

#Global Constants
X = "Ω"
O = "Φ"
EMPTY = " "
NUM_SQUARES = 9
TIE = "TIE"

import random

def instruct(): #Works
    """ display game instructions """
    print("""
    Welcome to the greatest intellectual challenge of all time: Tic-Tac-Toe.
    This will be a showdown between your human brain and my silicon processor.

    You will make your move known by entering a number, 1 - 9. The number
    will correspond to the board position as illustrated:


                    1 | 2 | 3
                    ---------
                    4 | 5 | 6
                    ---------
                    7 | 8 | 9

    Prepare yourself, test subject. The ultimate battle is about to begin. \n
    """)

def new_board(): #working
    board = []
    for i in range(NUM_SQUARES):
        board.append(EMPTY)
    return board
def display_board(board): #working
    """Display board on screen."""
    print(str.format("""
    {0} | {1} | {2}
    ---------
    {3} | {4} | {5}
    ---------
    {6} | {7} | {8}
    """,board[0],board[1],board[2],board[3],board[4],board[5],board[6],board[7],board[8]))

def ask_yes_no(question): #working
    """Ask a yes or no question. and give a one letter response back"""
    response = ""
    while response not in ("y","n","yes","no","yeet"):
        response = input(question).lower()
    x = response[0]
    return x
def ask_number(question, low, high): #working
    """Asks a question for a number. and give a one letter response back"""
    response = ""
    while response not in range(low,high):
        response = input(question)
        try:
            response = int(response)
        except:
            print("not a number")
    return response
def assign_piece(): #working
    """Uses ask_yes_no to figure out if the player would like to go first or second"""
    go_first = ask_yes_no("Would you like to go first?")
    if go_first == "y":
        player = X
        comp = O
    elif go_first == "n":
        player = O
        comp = X
    else:
        print("this message should not be seen")
    return player,comp
def switch_turn(turn):
    """Switches turn from the current turn to the other turn
        Pass in the current turn"""
    if turn == X:
        return O
    else:
        return X

def legal_moves(board):#worknig
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves

def player_turn(board,player):#workng
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("what place do you want to put your piece",1,10)-1
        
        if move not in legal:
            print("\nYou suck, for that is taken. You scum of the earth!")
    return move
def winner(board): #working
    "determin the winner of the game"""
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
    if EMPTY not in board:
        return TIE
    return None
def comp_turn(board,comp,player): #working
    copy_board = board[:]
    randint = random.randint(1,10)
    print(randint)
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    shuf_moves = []
    for i in BEST_MOVES:
        shuf_moves.append(i)
        print(shuf_moves)
    if randint > 2:
        random.shuffle(shuf_moves)
        print(shuf_moves)
    print("I shall take square number", end=" ")
    for move in legal_moves(board):
        copy_board[move] = comp
        if winner(copy_board) == comp:
            print(move+1)
            return move
        copy_board[move] = EMPTY
    if randint != 10:
        for move in legal_moves(board):
            copy_board[move] = player
            if winner(copy_board) == player:
                print(move+1)
                return move
            copy_board[move] = EMPTY
    for move in shuf_moves:
        copy_board[move] = comp
        if move in legal_moves(board):
            print(move+1)
            return move
def tictacgame():
    turn = X
    instruct()
    board = new_board()
    display_board(board)
    player,comp = assign_piece()
    while not winner(board):
        if turn == player:
            move = player_turn(board,player)
            board[move] = player
            display_board(board)
            turn = switch_turn(turn)
        elif turn == comp:
            move = comp_turn(board,comp,player)
            board[move] = comp
            display_board(board)
            turn = switch_turn(turn)
        else:
            print("error")
    the_winner = winner(board)
    if the_winner == comp or the_winner == player or the_winner == "TIE":
        if the_winner == "TIE":
            print("Its a tie!")
        if the_winner == player:
            print("Augh! You won this time human!")
        if the_winner == comp:
            print("Bask in my superior glory, human!")


        
            
    
