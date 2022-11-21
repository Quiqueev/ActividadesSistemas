import os, sys, time, string, copy

WIN=10
LOSE=-10

def max(a,b):
    return a if a > b else b

def min(a,b):
    return a if a < b else b

def PrintGameboard(GAMEBOARD, clear = True):
    for rows in GAMEBOARD:
        for cols in rows:
            print(cols, end =" ")
        print("\n")

def ReadChoice():
    while True:
        try:
            line = input()
            x, y = line.split(" ")
            x, y = int(x)-1, int(y)-1
            return x,y
        except:
            return -1, -1

def IsGameTied(GAMEBOARD):
    for i in range(3):
        for j in range(3):
            if GAMEBOARD[i][j] == "_":
                return False
    
    return True

def IsGameDone(GAMEBOARD, choice):
    # ROWS DONE
    if GAMEBOARD[0][0] == choice and GAMEBOARD[0][1] == choice and GAMEBOARD[0][2] == choice:
        return True
    
    if GAMEBOARD[1][0] == choice and GAMEBOARD[1][1] == choice and GAMEBOARD[1][2] == choice:
        return True
    
    if GAMEBOARD[2][0] == choice and GAMEBOARD[2][1] == choice and GAMEBOARD[2][2] == choice:
        return True
    
     # COLUMNS DONE
    if GAMEBOARD[0][0] == choice and GAMEBOARD[1][0] == choice and GAMEBOARD[2][0] == choice:
        return True
    
    if GAMEBOARD[0][1] == choice and GAMEBOARD[1][1] == choice and GAMEBOARD[2][1] == choice:
        return True
    
    if GAMEBOARD[0][2] == choice and GAMEBOARD[1][2] == choice and GAMEBOARD[2][2] == choice:
        return True
    
     # DIAGONAL DONE
    if GAMEBOARD[0][0] == choice and GAMEBOARD[1][1] == choice and GAMEBOARD[2][2] == choice:
        return True
    
    if GAMEBOARD[0][2] == choice and GAMEBOARD[1][1] == choice and GAMEBOARD[2][0] == choice:
        return True

def GetScore(GAMEBOARD):
    if IsGameDone(GAMEBOARD, 'O'):
        return WIN, 'O'
    elif IsGameDone(GAMEBOARD, 'X'):
        return LOSE, 'X'
    else:
        return 0, 0

def GeneratePossibleMoves(GAMEBOARD, choice):
    list_of_moves = []

    for row in range(3):
        for col in range(3):
            if GAMEBOARD[row][col] == '_':
                game = copy.deepcopy(GAMEBOARD)
                game[row][col] = choice
                list_of_moves.append(game)
    return list_of_moves

def GameComplete(score, GAMEBOARD):
    resume = True
    if IsGameTied(GAMEBOARD):
        print ('Tie Game.')
        resume = False
    elif score == LOSE:
        print ('You Win!')
        resume = False
    elif score == WIN:
        print ('You Lose!')
        resume = False

    if resume: return

    PrintGameboard(GAMEBOARD, clear=False)
    sys.exit(0)

def MinMax(GAMEBOARD, depth, maximizingplayer):

    score, choice = GetScore(GAMEBOARD)
    if depth == 0 or score == WIN or score == LOSE:
        return score, GAMEBOARD

    if maximizingplayer:
        best = LOSE
        best_child = None
        games = GeneratePossibleMoves(GAMEBOARD, 'O')
        print(games)
        for child in games:
            v, move = MinMax(child, depth-1, False)
            if v > best-1:
                best_child = child
                best = v
        return best, best_child
    else:
        best = WIN
        best_child = None
        games = GeneratePossibleMoves(GAMEBOARD, 'X')
        # print(games)
        for child in games:
            v, move = MinMax(child, depth-1, True)
            if v <= best:
                best_child = child
                best = v
        return best, best_child
            
def NextMove(GAMEBOARD):
    score, aux = MinMax(GAMEBOARD, 2, True)
    if (aux == None):
        GameComplete(score, [])

    for row in range(3):
        for col in range(3):
            GAMEBOARD[row][col] = aux[row][col]
    
    score, choice = GetScore(GAMEBOARD)
    return score, 'xx'

def main():
    GAMEBOARD = [['_','_','_'],['_','_','_'],['_','_','_']]

    while True:
        PrintGameboard(GAMEBOARD)
        print( "Enter (row, column)\n")
        row,col = ReadChoice()
        if (row, col) == (-1,-1):
            continue

        if GAMEBOARD[row][col] != '_':
            print("Already filled with: ", GAMEBOARD[row][col])
            continue
        GAMEBOARD[row][col] = 'X'

        score, choice = GetScore(GAMEBOARD)
        GameComplete(score, GAMEBOARD)

        score, choice = NextMove(GAMEBOARD)
        GameComplete(score, GAMEBOARD)


if __name__ == "__main__":
    main()