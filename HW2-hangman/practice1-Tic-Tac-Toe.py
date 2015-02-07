def piece( pos ):
    if moves[pos] == 0:
        return '  '
    if moves[pos] == 1:
        return 'Ｘ'
    if moves[pos] == 2:
        return 'Ｏ'

#function1:開始出招
def playMove():
    ## play a round
    print "Your turn, player ", player
    wheretoplay = int( input("Enter your move (0-8):") )
    if moves[wheretoplay] != 0:
        print("Something already there! You lose a turn!")
    else:
        moves[ wheretoplay ] = player

#function2:列出戰局情況
def printBoard():
    line = piece(0) + "｜" + piece(1) + "｜" + piece(2)
    print line
    print "－－－－－"
    line = piece(3) + "｜" + piece(4) + "｜" + piece(5)
    print line
    print "－－－－－"
    line = piece(6) + "｜" + piece(7) + "｜" + piece(8) 
    print(line)

#function3:是否贏了?
def checkForEnd():      
    #線性檢查(水平)
    for i in [0,3,6]:
        if moves[i] == player and moves[i+1] == player and moves[i+2] == player:
            return True
    #線性檢查(垂直)
    for i in [0,1,2]:
        if moves[i] == player and moves[1+3] == player and moves[i+6] == player:
            return True
    #線性檢查(斜線)
    if moves[0] == player and moves[4] == player and moves[8] == player:
        return True
    if moves[2] == player and moves[4] == player and moves[6] == player:
        return True


#function4:轉換玩家
def swapPlayer():
    global player
    if player == 1:
        player = 2
    else:
        player = 1

#換哪個玩家下棋了?
player= 1
#局盤
moves = [ 0, 0, 0,
          0, 0, 0,
          0, 0, 0 ]
#輸贏情勢
game_over = False
while not game_over :
    #function1:玩家開始畫OOXX
    playMove()
    #function2:列出戰局情況
    printBoard()
    #function3:是否贏了?
    game_over = checkForEnd()
    #function4:轉換玩家
    swapPlayer()


