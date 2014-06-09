#Alexander Wong
#EK128

#If I were to write this again, I would definitely try to use more functions
#-its a little messy right now (but still very much understandable)


import random


#The board will be held in a list

#e will be empty
#o will be a spot where player 'o' has played
#x is a spot where player 'x' has played

board=['e','e','e','e','e','e','e','e','e']

#moves will be referenced by positions 0-8
#012
#345
#678


#print the board
def printboard(board):
    print(board[0:3])
    print(board[3:6])
    print(board[6:9],'\n')



#Check to see if anyone has won
def boardcheck(board):
    #compare all possible game ending situations to see if gameover is false
    
    #check horizontals
    if (board[0]==board[1]==board[2]=='x') or (board[0]==board[1]==board[2]=='o'):
        return True
    elif (board[3]==board[4]==board[5]=='x') or (board[3]==board[4]==board[5]=='o'):
        return True
    elif (board[6]==board[7]==board[8]=='x') or (board[6]==board[7]==board[8]=='o'):
        return True
    #check verticals
    elif (board[0]==board[3]==board[6]=='x') or (board[0]==board[3]==board[6]=='o'):
        return True
    elif (board[1]==board[4]==board[7]=='x') or (board[1]==board[4]==board[7]=='o'):
        return True
    elif (board[2]==board[5]==board[8]=='x') or (board[2]==board[5]==board[8]=='o'):
        return True
    #check diagonals
    elif (board[0]==board[4]==board[8]=='x') or (board[0]==board[4]==board[8]=='o'):
        return True
    elif (board[2]==board[4]==board[6]=='x') or (board[2]==board[4]==board[6]=='o'):
        return True
    else:
        return False


def isEmpty(board,space):
    if board[space]=='e':
        return True
    else:
        return False

def canWin(board,player): #where player is either x or o
    #checks to see if a winning move is possible during a certain turn
    #If there is, it will also return the spot that will result in a win
    
    #horizontal move check
    if (board[0]==board[1]==player) and (isEmpty(board,2)==True):
        spot=2
        return True,spot
    elif (board[1]==board[2]==player) and (isEmpty(board,0)==True):
        spot=0
        return True,spot
    elif (board[0]==board[2]==player) and (isEmpty(board,1)==True):
        spot=1
        return True,spot
    
    elif (board[3]==board[4]==player) and (isEmpty(board,5)==True):
        spot=5
        return True,spot
    elif (board[4]==board[5]==player) and (isEmpty(board,3)==True):
        spot=3
        return True,spot
    elif (board[3]==board[5]==player) and (isEmpty(board,4)==True):
        spot=4
        return True,spot

    elif (board[6]==board[7]==player) and (isEmpty(board,8)==True):
        spot=8
        return True,spot
    elif (board[7]==board[8]==player) and (isEmpty(board,6)==True):
        spot=6
        return True,spot
    elif (board[6]==board[8]==player) and (isEmpty(board,7)==True):
        spot=7
        return True,spot

    #Verticals
    elif (board[0]==board[3]==player) and (isEmpty(board,6)==True):
        spot=6
        return True,spot
    elif (board[3]==board[6]==player) and (isEmpty(board,0)==True):
        spot=0
        return True,spot
    elif (board[0]==board[6]==player) and (isEmpty(board,3)==True):
        spot=3
        return True,spot

    elif (board[1]==board[4]==player) and (isEmpty(board,7)==True):
        spot=7
        return True,spot
    elif (board[4]==board[7]==player) and (isEmpty(board,1)==True):
        spot=1
        return True,spot
    elif (board[1]==board[7]==player) and (isEmpty(board,4)==True):
        spot=4
        return True,spot

    elif (board[2]==board[5]==player) and (isEmpty(board,8)==True):
        spot=8
        return True,spot
    elif (board[5]==board[8]==player) and (isEmpty(board,2)==True):
        spot=2
        return True,spot
    elif (board[2]==board[8]==player) and (isEmpty(board,5)==True):
        spot=5
        return True,spot

    #diagonals
    elif (board[0]==board[4]==player) and (isEmpty(board,8)==True):
        spot=8
        return True,spot
    elif (board[4]==board[8]==player) and (isEmpty(board,0)==True):
        spot=0
        return True,spot
    elif (board[0]==board[8]==player) and (isEmpty(board,4)==True):
        spot=4
        return True,spot

    elif (board[2]==board[4]==player) and (isEmpty(board,6)==True):
        spot=6
        return True,spot
    elif (board[4]==board[6]==player) and (isEmpty(board,2)==True):
        spot=2
        return True,spot
    elif (board[2]==board[6]==player) and (isEmpty(board,4)==True):
        spot=4
        return True,spot
    else:
        return False
    

def computermove(board,player):

    #random corner logic (see corner move below)
    corners=[0,2,6,8]
    randomcorner1=random.choice(corners)
    corners.remove(randomcorner1)
    randomcorner2=random.choice(corners)
    corners.remove(randomcorner2)
    randomcorner3=random.choice(corners)
    corners.remove(randomcorner3)
    randomcorner4=corners[0]

    #random side logic (see side move below)
    sides=[1,3,5,7]
    rside1=random.choice(sides)
    sides.remove(rside1)
    rside2=random.choice(sides)
    sides.remove(rside2)
    rside3=random.choice(sides)
    sides.remove(rside3)
    rside4=sides[0]

    
    #If can't win, will check if can block
    #if can't block, will select intelligent move
    if canWin(board,player)==False: #will block in a specific order...note that if the opponent can win in multiple ways, it doesn't matter which spot is blocked first


        #determine who is being block based on what player is taking their turn
        if player=='x':
          blockwho='o'
        else:
          blockwho='x'


        #horizontal move check
        if (board[0]==board[1]==blockwho) and (isEmpty(board,2)==True):
            return 2
        elif (board[1]==board[2]==blockwho) and (isEmpty(board,0)==True):
            return 0
        elif (board[0]==board[2]==blockwho) and (isEmpty(board,1)==True):
            return 1
        
        elif (board[3]==board[4]==blockwho) and (isEmpty(board,5)==True):
            return 5
        elif (board[4]==board[5]==blockwho) and (isEmpty(board,3)==True):
            return 3
        elif (board[3]==board[5]==blockwho) and (isEmpty(board,4)==True):
            return 4

        elif (board[6]==board[7]==blockwho) and (isEmpty(board,8)==True):
            return 8
        elif (board[7]==board[8]==blockwho) and (isEmpty(board,6)==True):
            return 6
        elif (board[6]==board[8]==blockwho) and (isEmpty(board,7)==True):
            return 7

        #Verticals
        elif (board[0]==board[3]==blockwho) and (isEmpty(board,6)==True):
            return 6
        elif (board[3]==board[6]==blockwho) and (isEmpty(board,0)==True):
            return 0
        elif (board[0]==board[6]==blockwho) and (isEmpty(board,3)==True):
            return 3

        elif (board[1]==board[4]==blockwho) and (isEmpty(board,7)==True):
            return 7
        elif (board[4]==board[7]==blockwho) and (isEmpty(board,1)==True):
            return 1
        elif (board[1]==board[7]==blockwho) and (isEmpty(board,4)==True):
            return 4

        elif (board[2]==board[5]==blockwho) and (isEmpty(board,8)==True):
            return 8
        elif (board[5]==board[8]==blockwho) and (isEmpty(board,2)==True):
            return 2
        elif (board[2]==board[8]==blockwho) and (isEmpty(board,5)==True):
            return 5

        #diagonals
        elif (board[0]==board[4]==blockwho) and (isEmpty(board,8)==True):
            return 8
        elif (board[4]==board[8]==blockwho) and (isEmpty(board,0)==True):
            return 0
        elif (board[0]==board[8]==blockwho) and (isEmpty(board,4)==True):
            return 4

        elif (board[2]==board[4]==blockwho) and (isEmpty(board,6)==True):
            return 6
        elif (board[4]==board[6]==blockwho) and (isEmpty(board,2)==True):
            return 2
        elif (board[2]==board[6]==blockwho) and (isEmpty(board,4)==True):
            return 4

        #-------------------
        #Moves if not 'easy'

        #if opponent moves corner for first move, computer must choose center
        elif (board[0]==blockwho) and (board[1]==board[2]==board[3]==board[4]==board[5]==board[6]==board[7]==board[8]=='e'):
            return 4
        elif (board[2]==blockwho) and (board[0]==board[1]==board[3]==board[4]==board[5]==board[6]==board[7]==board[8]=='e'):
            return 4
        elif (board[6]==blockwho) and (board[0]==board[1]==board[2]==board[3]==board[4]==board[5]==board[7]==board[8]=='e'):
            return 4
        elif (board[8]==blockwho) and (board[0]==board[1]==board[2]==board[3]==board[4]==board[5]==board[6]==board[7]=='e'):
            return 4

        #if center taken, take corner
        elif (board[4] != 'e') and (board[0]==board[1]==board[2]==board[3]==board[5]==board[6]==board[7]==board[8]=='e'):
            return random.choice([0,2,6,8])


        #special case if opponent has two opposite corners and player has center, need to play a side!
        elif (board[4]==player) and (board[0]==board[8]==blockwho) and (board[1]==board[2]==board[5]==board[3]==board[6]==board[7]=='e'):
            return random.choice([1,3,5,7]) 
        elif (board[4]==player) and (board[2]==board[6]==blockwho) and (board[0]==board[1]==board[3]==board[5]==board[7]==board[8]=='e'):
            return random.choice([1,3,5,7])

                
        #if corner NOT taken already, take random corner 

        elif board[randomcorner1] == 'e':
            return randomcorner1
        elif board[randomcorner2] == 'e':
            return randomcorner2
        elif board[randomcorner3] == 'e':
            return randomcorner3
        elif board [randomcorner4] == 'e':
            return randomcorner4

        #center
        elif board[4] == 'e':
            return 4

        #random sides:

        elif board[rside1] == 'e':
            return rside1
        elif board[rside2] == 'e':
            return rside2
        elif board[rside3] == 'e':
            return rside3
        elif board[rside4] == 'e':
            return rside4
        else:
            return 'No moves'

    elif (canWin(board,player)[0])==True: #if canWin, play winning move
        return canWin(board,player)[1]
          

def tiecheck(board):
    if (board[0] !='e') and (board[1] !='e') and (board[2] !='e') and (board[3] !='e') and (board[4] !='e') and (board[5] !='e') and (board[6] !='e') and (board[7] !='e') and (board[8] !='e'):
        return True
    else:
        return False


#Choose what type of game to play
print('What kind of game would you like?')
print('[1] Two player')
print('[2] Player vs.Computer')
print('[3] Computer vs. Computer (simulations)')
gametype=int(input('Enter 1, 2, or 3\n'))



#Variable initialization
gameover=False
numberofmoves=0



#----------------------------------------------------------
#2-PLAYER GAME
#----------------------------------------------------------
if gametype==1:
    while gameover==False:


        printboard(board)
            
        #player turns
        print("Player X's turn")
        #enter the position you want to play
        xmove=input('Enter a number corresponding to the board:\n012\n345\n678\n')        
        #modifies the board with player x's move
        board[int(xmove)]='x'

        if boardcheck(board)==True:
            print('Player X wins!')
            break
        if tiecheck(board)==True:
            print('Tie game.')
            break
        
        #print the board
        printboard(board)
        
        print("Player O's turn")
        omove=input('Enter a number corresponding to the board:\n012\n345\n678\n')
        board[int(omove)]='o'

        if boardcheck(board)==True:
            print('Player O wins!')
            break
        if tiecheck(board)==True:
            print('Tie game.')
            break


#NOTE*** I have not implemented player so that it allows any combination of human/computer
#At this point, human can only be player 'x' and the computer can only be player 'o'
        
        
#---------------------------------------------------------
#PLAYER VS. COMPUTER
#---------------------------------------------------------
elif gametype==2:
    while gameover==False:

        printboard(board)

        xmove=input('Enter a number corresponding to the board:\n012\n345\n678\n')
        board[int(xmove)]='x'

        if boardcheck(board)==True:
            print('You win!')
            break
        if tiecheck(board)==True:
            print('Tie game.')
            break
        
        omove=computermove(board,'o')
        board[int(omove)]='o'

        if boardcheck(board)==True:
            printboard(board)
            print()
            print('The computer won.')
            break
        if tiecheck(board)==True:
            print('Tie game.')
            break

#---------------------------------------------------------   
#COMPUTER GAME (SIMULATION)
#---------------------------------------------------------
elif gametype==3:

    xwin=0
    owin=0
    tie=0

    simulations=int(input('How many simulations?\n'))


    for s in range(simulations):

        #board reset
        board=['e','e','e','e','e','e','e','e','e']

        while gameover==False:
                
            #Computer X's turn
            xmove=computermove(board,'x')
            #modifies the board with player x's move
            board[int(xmove)]='x'

            if boardcheck(board)==True:
                xwin=xwin+1
                break
            if tiecheck(board)==True:
                tie=tie+1
                break

            #Computer O's turn
            omove=computermove(board,'o')
            board[int(omove)]='o'

            if boardcheck(board)==True:
                owin=owin+1
                break
            if tiecheck(board)==True:
                tie=tie+1
                break

    print('X won',xwin,'times')
    print('O won',owin,'times')
    print('ties:',tie)
