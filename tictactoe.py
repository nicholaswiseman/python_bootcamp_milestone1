def tictactoe():
    repeat = 1
    while repeat:
        spaces=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        win = False
        [p1,p2] = setup()
        print(f'Player One is {p1} and Player Two is {p2}')
        print('Player One Goes First')
        printboard(spaces)
        while 1:
            current_player = p1
            picking(p1,spaces)
            if checkwin(spaces):
                break
            if checkdraw(spaces):
                break
            current_player = p2
            picking(p2, spaces)
            if checkwin(spaces):
                break
            if checkdraw(spaces):
                break
        if checkwin(spaces):
            print(f'\n{current_player} wins!')
        elif checkdraw(spaces):
            print("Tis a draw!")
        repeat = playagain()

def setup():
    while 1:
        p1_team = input("Player One Pick Your Team:")
        if p1_team.upper()=='X':
            p2_team ='O'
            break
        elif p1_team.upper()=='O':
            p2_team ='X'
            break
        else:
            print('Please pick X or O!')
    return [p1_team.upper(),p2_team.upper()]

def printboard(spaces):
    print(f' {spaces[7]} | {spaces[8]} | {spaces[9]}')
    print('-----------')
    print(f' {spaces[4]} | {spaces[5]} | {spaces[6]}')
    print('-----------')
    print(f' {spaces[1]} | {spaces[2]} | {spaces[3]}')

def picking(player,spaces):
    done = False
    while not done:
        space = input('Pick Your Space: ')
        if space not in ['1','2','3','4','5','6','7','8','9']:
            print("That's not a space!")
        elif spaces[int(space)]!=' ':
            print("That space is already taken!")
        else:
            spaces[int(space)] = player
            printboard(spaces)
            done = True

def checkwin(spaces):
# first check rows
    if spaces[1]==spaces[2]==spaces[3] and (spaces[1]=='X' or spaces[1] == 'O'):
        return True
    elif spaces[4]==spaces[5]==spaces[6] and (spaces[4]=='X' or spaces[4] == 'O'):
        return True
    elif spaces[7]==spaces[8]==spaces[9] and (spaces[7]=='X' or spaces[7] == 'O'):
        return True
# now check columns
    elif spaces[1]==spaces[4]==spaces[7] and (spaces[1]=='X' or spaces[1] == 'O'):
        return True
    elif spaces[2]==spaces[5]==spaces[8] and (spaces[2]=='X' or spaces[2] == 'O'):
        return True
    elif spaces[3]==spaces[6]==spaces[9] and (spaces[3]=='X' or spaces[3] == 'O'):
        return True
# now diagonals
    elif spaces[1]==spaces[5]==spaces[9] and (spaces[1]=='X' or spaces[1] == 'O'):
        return True
    elif spaces[3]==spaces[5]==spaces[7] and (spaces[3]=='X' or spaces[3] == 'O'):
        return True
    else:
        return False

def checkdraw(spaces):
    if (spaces[1]==' ' or spaces[2]==' ' or spaces[3]==' ' or spaces[4]==' ' or spaces[5]==' ' or spaces[6]==' ' or spaces[7]==' ' or spaces[8]==' ' or spaces[9]==' '): 
        return False
    else:
        return True
def playagain():
    again = input('\nPlay Again? (y/n): ')
    return (again == 'Y' or again =='y' or again == 'yes' or again == 'Yes')

tictactoe()