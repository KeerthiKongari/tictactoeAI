def board_display():
    print("---------")
    print("|", board[0],  board[1], board[2], "|")
    print("|", board[3],  board[4], board[5], "|")
    print("|", board[6],  board[7], board[8], "|")
    print("---------")

def whos_turn():
    count = 0
    c = 0
    empty = 0 
    for v in board:
        if v == 'X':
            count += 1
        elif v == 'O':
            c += 1
        else:
            empty += 1
    if count == c:
        return 'X'
    elif count > c:
        value = count - c
        if value == 1:
            return 'O'
    elif c > count:
        value = c - count
        if value == 1:
            return 'X'

def empty():
    empt = 0
    for v in board:
        if v == '_':
            empt += 1
    if empt == 0:
        print("Draw")
    else:
        print("Game not finished")

def winner():
    r1 = (board[0] == "X" and board[1] == "X" and board[2] == "X")
    r2 = (board[3] == "X" and board[4] == "X" and board[5] == "X")
    r3 = (board[6] == "X" and board[7] == "X" and board[8] == "X")
    v1 = (board[0] == "X" and board[4] == "X" and board[8] == "X")
    v2 = (board[2] == "X" and board[4] == "X" and board[6] == "X")
    c1 = (board[0] == "X" and board[3] == "X" and board[6] == "X")
    c2 = (board[1] == "X" and board[4] == "X" and board[7] == "X")
    c3 = (board[2] == "X" and board[5] == "X" and board[8] == "X")
    ro1 = (board[0] == "O" and board[1] == "O" and board[2] == "O")
    ro2 = (board[3] == "O" and board[4] == "O" and board[5] == "O")
    ro3 = (board[6] == "O" and board[7] == "O" and board[8] == "O")
    vo1 = (board[0] == "O" and board[4] == "O" and board[8] == "O")
    vo2 = (board[2] == "O" and board[4] == "O" and board[6] == "O")
    co1 = (board[0] == "O" and board[3] == "O" and board[6] == "O")
    co2 = (board[1] == "O" and board[4] == "O" and board[7] == "O")
    co3 = (board[2] == "O" and board[5] == "O" and board[8] == "O")
    if ro1 or ro2 or ro3 or vo1 or vo2 or co1 or co2 or co3:
        print("O wins")
    elif r1 or r2 or r3 or v1 or v2 or c1 or c2 or c3:
        print("X wins")
    else:
        empty()

val = input("Enter Cells")
board = [val[0], val[1], val[2], val[3], val[4], val[5], val[6], val[7], val[8]]
board_display()
x = whos_turn()
while True:
    move= input("Enter Coordinates").split(" ")
    if move[0].isalpha() or move[1].isalpha():
        print("You should enter numbers!")
    elif int(move[0]) < 0 or int(move[0]) > 3 or int(move[1]) < 1 or int(move[1]) > 3:
        print("Coordinates should be from 1 to 3!")
    else:
        if int(move[0]) == 1 and int(move[1]) == 3:
            if board[0] == 'X' or board[0] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                board[0] = x
                board_display()
                winner()
                break
        elif int(move[0]) == 2 and int(move[1]) == 3:
            if board[1] == 'X' or board[1] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                board[1] = x
                board_display()
                winner()
                break
        elif int(move[0]) == 3 and int(move[1]) == 3:
            if board[2] == 'X' or board[2] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                board[2] = x
                board_display()
                winner()
                break
        elif int(move[0]) == 1 and int(move[1]) == 2:
            if board[3] == 'X' or board[3] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                board[3] = x
                board_display()
                winner()
                break
        elif int(move[0]) == 2 and int(move[1]) == 2:
            if board[4] == 'X' or board[4] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                board[4] = x
                board_display()
                winner()
                break
        elif int(move[0]) == 3 and int(move[1]) == 2:
            if board[5] == 'X' or board[5] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                board[5] = x
                board_display()
                winner()
                break
        elif int(move[0]) == 1 and int(move[1]) == 1:
            if board[6] == 'X' or board[6] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                board[6] = x
                board_display()
                winner()
                break
        elif int(move[0]) == 2 and int(move[1]) == 1:
            if board[7] == 'X' or board[7] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                board[7] = x
                board_display()
                winner()
                break
        elif int(move[0]) == 3 and int(move[1]) == 1:
            if board[8] == 'X' or board[8] == 'O':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                board[8] = x
                board_display()
                winner()
                break


