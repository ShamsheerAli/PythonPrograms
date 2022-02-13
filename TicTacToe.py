import os
board=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
player=1
win=1
draw=-1
running=0
stop=1
game=running
mark='x'
def drawboard():
    print("%c  |%c  |%  c"%(board[1],board[2],board[3]))
    print("___|___|___")
    print("%c  |%c  |%  c"%(board[4],board[5],board[6]))
    print("___|___|___")
    print("%c  |%c  |%  c"%(board[7],board[8],board[9]))
    print("   |   |   ")
def checkposition(x):
    if board[x]==" " :
        return True
    else:
        return False
def checkwin():
    global game
    if (board[1]==board[2] and board[3]==board[2] and board[1]!=" "):
        game=win
    elif (board[4]==board[5] and board[5]==board[6] and board[4]!=" "):
        game=win
    elif (board[7]==board[8] and board[8]==board[9] and board[9]!=" "):
        game=win
    elif (board[1]==board[4] and board[4]==board[7] and board[1]!=" "):
        game=win
    elif (board[2]==board[5] and board[5]==board[8] and board[2]!=" "):
        game=win
    elif (board[3]==board[6] and board[6]==board[9] and board[3]!=" "):
        game=win
    elif (board[1]==board[5] and board[5]==board[9] and board[5]!=" "):
        game=win
    elif (board[3]==board[5] and board[5]==board[7] and board[5]!=" "):
        game=win
    elif (board[1]!=" " and board[2]==" " and board[3]!=" " and board[4]!=" " and board[5]!=" " and board[6]!=" " and board[7]!=" " and board[8]!=" " and board[9]!=" "):
        game=draw
    else:
        game=running
print("player 1 [x] ---- player 2 [0]\n")
print()
print()
print("please wait")
t=0
while game==running:
    t+=1
    os.system('cls')
    drawboard()
    if player%2!=0:
        print("player1's chance")
        mark='x'
    else:
        print("player2's chance")
        mark='0'
    choice=int(input("enter the position b/w [1-9] where u want to mark:"))
    if checkposition(choice):
               board[choice]=mark
               player+=1
               checkwin()
               
drawboard()
if game==draw:
    print("game draw")
elif game==win:
    player-=1
    if player%2!=0:
        print("player1 won")
    else:
        print("player2 won")
