# By submitting this assignment, I agree to the following:
# “Aggies do not lie, cheat, or steal, or tolerate those who do”
# “I have not given or received any unauthorized aid on this assignment”
#
# Names: Austin
# Christopher
# Reed
# Eddy
# Section: 468
# Assignment: Lab: Your Checkered Past
# Date: 6 October 2022


rowA=["A",".",".",".",".",".",".",".",".","."]
rowB=["B",".",".",".",".",".",".",".",".","."]
rowC=["C",".",".",".",".",".",".",".",".","."]
rowD=["D",".",".",".",".",".",".",".",".","."]
rowE=["E",".",".",".",".",".",".",".",".","."]
rowF=["F",".",".",".",".",".",".",".",".","."]
rowG=["G",".",".",".",".",".",".",".",".","."]
rowH=["H",".",".",".",".",".",".",".",".","."]
rowI=["I",".",".",".",".",".",".",".",".","."]
board=[rowA,rowB,rowC,rowD,rowF,rowG,rowF]
print("\t\t 1\t 2\t 3\t 4\t 5\t 6\t 7\t 8\t 9")
for r in range(len(board)): #this are the rows
    for i in board[r]:
        print("\t",i,end=" ") #prints out the columns
    print()
want_Stop=input("stop? (Y/N)").upper()
turn_number=0
valid= True
while want_Stop!="Y":
    if turn_number%2==0:
        print("White turn !!\n")
        Wrow=input("what coordinate row do you want (ex: A,B,C)").upper()
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
        if(valid) and board[WrowNum][Wcol]==".":
            board[WrowNum][Wcol]=chr(9679)
        else:
            print("Spot filled or invalid coordinate")
            turn_number-=1
    else:
        print("Black turn !!!?\n")
        Wrow=input("what coordinate row do you want (ex: A,B,C)").upper()
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
        if(valid)and board[WrowNum][Wcol]==".":
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
    want_Stop = input("stop? (Y/N)").upper()

print("what a great game")
#omg you found a funny little mesae , good for you, count to three and ill through a cabage at you