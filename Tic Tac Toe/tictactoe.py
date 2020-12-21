"""
Tic Tac Toe Player
"""

import math
import copy


X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
   count_x = 0

   count_o = 0



   for i in range(3):

        for j in range(3):

            if(board[i][j] ==  "X"):

                count_x +=1

            elif(board[i][j] ==  "O"):

                count_o +=1



   if(count_o < count_x):

        return O

   return X
        
            
   
    #if len(board)
    #raise NotImplementedError


def actions(board):
   actions=set()
   if terminal(board):
       pass
   else:
       for i in range(len(board)):
         for j in range(len(board)):
            if board[i][j]==None:
                actions.add((i,j))
                
   return actions
                
   """
    Returns set of all possible actions (i, j) available on the board.
    """
    #raise NotImplementedError


def result(board, action):
    newBoard=copy.deepcopy(board)
    newBoard[action[0]][action[1]]=player(board)
    
    return newBoard
    
   
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    #Checking row wise
    
    count_x_row =0

    count_o_row =0



    count_x_col = 0

    count_o_col = 0



    count_x_diag = 0

    count_o_diag = 0



    count_x_diag_1 = 0

    count_o_diag_1 = 0

    for i in range(3):

        for j in range(3):

            if(board[i][j] == X):

                count_x_row +=1

            elif(board[i][j] == O):

                count_o_row +=1



            if(board[j][i] == X):

                count_x_col +=1

            elif (board[j][i] == O):

                count_o_col +=1



            if(i == j and board[i][j] == X):

                count_x_diag +=1

            elif (i == j and board[i][j] == O):

                count_o_diag += 1



            if (i+j ==2 and board[i][j] == X):

                count_x_diag_1 +=1

            elif (i+j ==2 and board[i][j] == O):

                count_o_diag_1 +=1



        if (count_o_row == 3 or count_o_col ==3):

            return O

        elif (count_x_row == 3 or count_x_col == 3):

            return X



       

        count_x_row = 0

        count_x_col = 0

        count_o_row = 0

        count_o_col = 0



    if (count_o_diag == 3 or count_o_diag_1 ==3):

        return O

    elif(count_x_diag == 3 or count_x_diag_1 ==3):

        return X

    else:

        return None
        
            
    """
    Returns the winner of the game, if there is one.
    """
    #raise NotImplementedError


def terminal(board):
    
    p=0
    
    for i in range(3):
        for j in range (3):
            if board[i][j]==None:
                p=1
                break
                
    if winner(board)==X or winner(board)==O :
        return True
    elif winner(board)==None:
        if p==0:
            return True
        elif p==1:
            p=0
            return False
            

    """
    Returns True if game is over, False otherwise.
    """
    #raise NotImplementedError


def utility(board):
    
    if winner(board)==X:
        return 1
    elif winner(board)==O:
        return -1
    elif winner(board)==None:
        return 0
    
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    #raise NotImplementedError


def minimax(board):
    
        p = player(board)
        if(p==X):

            value = float("-inf")

            action_select = None

            for action in actions(board):

                minValueResult = minValue(result(board, action))



                if minValueResult > value:

                    value = minValueResult

                    action_select = action



        elif p==O:

        
                value = float("inf")

                action_select = None



                for action in actions(board):

                    maxValueResult = maxValue(result(board, action))



                    if maxValueResult < value:

                        value = maxValueResult

                        action_select = action



        return action_select

    #raise NotImplementedError



def maxValue(board):

        if terminal(board):

            return utility(board)

        v = float('-inf')

        for action in actions(board):

            v = max(v,minValue(result(board, action)))

        return v


def minValue(board):

    if terminal(board):

        return utility(board)

    v = float('inf')

    for action in actions(board):

        v = min(v,maxValue(result(board, action)))

    return v
        
        
        
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
