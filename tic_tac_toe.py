from __future__ import print_function

li = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
row = ' '
col = ' '
usr = 0
print("Welcome to the tic tac toe game...")


# Printing the table

def table():
    i = 0
    print("\n\n\n")
    while i < 3:
        j = 0
        while j < 3:
            if j is 0 or j is 1:
                print("%s|" % li[i][j], end='')
            else:
                print("%s" % li[i][j], end='')
            j += 1
        print("")
        i += 1
    print("\n\n\n")


table()


# Take User Input.

def usr_input(inp):
    print("\nPlayer: %s --> Enter the row you want to insert: " % inp, end='')
    global row
    row = input()
    # if row > 2 or row < 0:
    #     print("\nTry again with correct value.")
    #     usr_input(inp)
    print("\nPlayer: %s --> Enter the column you want to insert: " % inp, end='')
    global col
    col = input()
    # if col > 2 or col < 0:
    #     print("\nTry again with correct value.")
    #     usr_input(inp)
    if li[int(row)][int(col)] is ' ':
        li[int(row)][int(col)] = str(inp)
    else:
        print("\n\nThis position is already occupied....Try again..\n\n")
        usr_input(inp)


# Checking for the Winner!!

# Checking for the diagonal 0-1-2

def dig_0_1_2(p):
    # For diagonal 0-1-2
    li_0 = li[0][0]
    li_1 = li[1][1]
    li_2 = li[2][2]
    if li_0 is str(p) and li_1 is str(p) and li_2 is str(p):
        return True
    else:
        return False


# Checking for the diagonal 2-1-0

def dig_2_1_0(p):
    # For the diagonal 2-1-0
    li_0 = li[2][0]
    li_1 = li[1][1]
    li_2 = li[0][2]
    if li_0 is str(p) and li_1 is str(p) and li_2 is str(p):
        return True
    else:
        return False


# Checking for the columns

def column(p):
    # For columns
    i = 0
    j = 0
    count = 0
    while i < 3:
        li_col = [item[i] for item in li]

        while j < 3:
            if li_col[j] is str(p):
                count += 1
            else:
                count = 0
                break
            j += 1
        if count is 3:
            return True
        i += 1
    if count is 3:
        return True
    else:
        return False


# Check for the Row matching
def rows(p):
    # For rows
    count = 0
    for li_row in li:
        for item in li_row:
            if item is str(p):
                count += 1
                continue
            else:
                count = 0
                break

        if count is 3:
            return True

    if count is 3:
        return True
    else:
        return False


# Checking for the winner!

def check(p):
    if rows(p) is True:
        print("\n\nPlayer: %s --> Won the game...... by matching rows" % p)
        exit(0)
    if column(p) is True:
        print("\n\nPlayer: %s --> Won the game...... by matching columns" % p)
        exit(0)
    if dig_0_1_2(p) is True:
        print("\n\nPlayer: %s --> Won the game...... by matching diagonal 0-1-2" % p)
        exit(0)
    if dig_2_1_0(p) is True:
        print("\n\nPlayer: %s --> Won the game...... by matching diagonal 2-1-0" % p)
        exit(0)


def game_tie():
    i = 0
    count = 0
    while i < 3:
        if ' ' not in li[i]:
            count += 1
        i += 1
    if count is 3:
        print("\n\n\nGame tied between \'0\' and \'1\'.....Try again.")
        exit(0)


# Game Initialization

def init():
    global usr
    i = 0
    while i < 9:
        if usr is 0:
            usr_input(0)
            table()
            check(0)
            game_tie()
            usr = 1
        else:
            usr_input(1)
            table()
            check(0)
            game_tie()
            usr = 0
    i += 1


init()
