# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Austin
# Christopher
# Reed
# Eddy
# Section: 468
# Assignment: Lab: Your Stony Past
# Date: 06 October 2022

print("-----------------------------------RULES OF THE GAME------------------------------------------")
print("At the beginning of the game the board must be bare.\n"
      "Black must start the game then followed by white and then back to\n"
      "black and so on. To make a move, one must place their stone on an empty\n"
      "intersection on the board. A connected group of stones can be captured when\n"
      "all intersections adjacent to the group are occupied by the opposing color.\n"
      "Capture of an enemy will always take prescedence over self capture. In addition\n"
      "to capturing an opponents stones it is also possible to score by surrounding an\n"
      "empty space with stones of all your color. A stone may never be placed with the intention\n"
      "to recreate a former position. Two consectuive passes will end the game. In short,\n"
      "the player with more area will win. To calculate the final score each opponent will\n"
      "each player will  count the number of unoccupied points that are bordered by all of their\n"
      "colored stones and then the player will subtract the number of their stones that were\n"
      "taken by their opponent. The player with the greater score will be declared winner.")
print("-----------------------------------------------------------------------------------------------")

rowA=["A",".",".",".",".",".",".",".",".","."]
rowB=["B",".",".",".",".",".",".",".",".","."]
rowC=["C",".",".",".",".",".",".",".",".","."]
rowD=["D",".",".",".",".",".",".",".",".","."]
rowE=["E",".",".",".",".",".",".",".",".","."]
rowF=["F",".",".",".",".",".",".",".",".","."]
rowG=["G",".",".",".",".",".",".",".",".","."]
rowH=["H",".",".",".",".",".",".",".",".","."]
rowI=["I",".",".",".",".",".",".",".",".","."]
board=[rowA,rowB,rowC,rowD,rowE,rowF,rowG, rowH, rowI]
print("\t\t 1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9")
for r in range(len(board)): #this are the rows
    for i in board[r]:
        print("\t",i,end=" ") #prints out the columns
    print()
want_Stop=input("stop? (Y/N)").upper()  #This is where it is asked at the beginning of a turn if the game is to end.
turn_number=0
valid= True
while want_Stop!="Y":   #Game will continue until the user wants to stop the game
    if turn_number%2==0:    #This if statement will run if it is whites turn
        print("White turn !!\n")
        Wrow=input("what coordinate row do you want (ex: A,B,C)").upper()   #This askes the user where they would like their stone placed
        Wcol=int(input("what coordinate col do you want (ex: 1)"))
        if(Wrow=="A"):
            WrowNum=0
        elif(Wrow=="B"):
            WrowNum=1
        elif(Wrow=="C"):
            WrowNum=2
        elif(Wrow=="D"):
            WrowNum=3
        elif(Wrow=="E"):
            WrowNum=4
        elif(Wrow=="F"):
            WrowNum=5
        elif(Wrow=="G"):
            WrowNum=6
        elif(Wrow=="H"):
            WrowNum=7
        elif(Wrow=="I"):
            WrowNum=8
        else:
            valid=False
            print("Not valid row")
        if Wcol>9 or Wcol==0:
            valid = False
            print("Not valid column")
        if(valid) and board[WrowNum][Wcol]==".":    #This will place a point as long as the spot is not already occupied
            board[WrowNum][Wcol]=chr(9679)
        else:
            print("Spot filled or invalid coordinate")  #If the spot is not legal, this will be displayed.
            turn_number-=1
    else:
        print("Black turn !!!?\n")  #This statement will run if it is balcks turn
        Wrow=input("what coordinate row do you want (ex: A,B,C)").upper()   #These statements ask the user where they want their stone placed
        Wcol=int(input("what coordinate col do you want (ex: 1)"))
        if(Wrow=="A"):
            WrowNum=0
        elif(Wrow=="B"):
            WrowNum=1
        elif(Wrow=="C"):
            WrowNum=2
        elif(Wrow=="D"):
            WrowNum=3
        elif(Wrow=="E"):
            WrowNum=4
        elif(Wrow=="F"):
            WrowNum=5
        elif(Wrow=="G"):
            WrowNum=6
        elif(Wrow=="H"):
            WrowNum=7
        elif(Wrow=="I"):
            WrowNum=8
        else:
            valid=False
            print("Not valid row")
        if Wcol>9 or Wcol==0:
            valid = False
            print("Not valid column")
        if(valid)and board[WrowNum][Wcol]==".": #If the spot selected is a legal spot to play a stone will be placed
            board[WrowNum][Wcol]=chr(9675)
        else:
            print("Spot filled or invalid coordinate")
            turn_number-=1
    turn_number+=1
    valid = True
    print("\t\t 1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9")
    for r in range(len(board)):  # this are the rows
        for i in board[r]:
            print("\t",i, end=" ")  # prints out the columns
        print()
    want_Stop = input("stop? (Y/N)").upper()    #This will continue to ask the users if they want the game to stop or continues

print("what a great game")
