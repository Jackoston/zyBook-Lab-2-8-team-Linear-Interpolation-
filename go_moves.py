rowA=[".",".",".",".",".",".",".",".","."]
rowB=[".",".",".",".",".",".",".",".","."]
rowC=[".",".",".",".",".",".",".",".","."]
rowD=[".",".",".",".",".",".",".",".","."]
rowE=[".",".",".",".",".",".",".",".","."]
rowF=[".",".",".",".",".",".",".",".","."]
rowG=[".",".",".",".",".",".",".",".","."]
rowH=[".",".",".",".",".",".",".",".","."]
rowI=[".",".",".",".",".",".",".",".","."]
board=[rowA,rowB,rowC,rowD,rowF,rowG,rowF]

for r in range(len(board)):
    for i in board[r]:
        print(i,end=" ")
    print()
want_Stop=input("stop? (Y/N)")
turn_number=0
while want_Stop!="Y":
    if turn_number%2==0:
        #whites turn
    else:
        #blacks turn
    turn_number+=1
