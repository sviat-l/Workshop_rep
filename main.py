def is_alive(board,attacked):
    alive=False
    for i in range(8):
        for j in range(8):
            if board[i][j]=='X' and attacked[i][j]!=' ':
                alive=True
                break
    return alive

def output_field():
    for i in range(2):
        board = list(itertools.chain.from_iterable(board))
    print("---------------------------------")
    for i in range(8):
        print("|", board[0 + i * 8], "|", board[1 + i * 8], "|", board[2 + i * 8],\
             "|", board[3 + i * 8], "|", board[4 + i * 8],"|", board[5 + i * 8],"|",\
                  board[6 + i * 8],"|", board[7 + i * 8], "|")
        print("---------------------------------")

def input_move(attacked1,board1):
    output_field(attacked1)
    move=input('Your move:')
    coor1=ord(move[0])-ord('a')
    coor2=int(move[1])-1
    while attacked1[coor1][coor2] in ['.','x']:
        move=input('Wrong move. Your move:')
        coor1=ord(move[0])-ord('a')
        coor2=int(move[1])-1
    return coor1,coor2

def make_move(move,board,attacked):
    if board[move[0]][move[1]]=='X':
        bool1 = True
        for j1 in range(-1,2,2):
            for j2 in range(-1,2,2):
                if attacked[move[0]+j1][move[1]+j2]==' ' and board[move[0]+j1][move[1]+j2]=='X':
                    bool1=False
        if bool1:
            print('You killed ma boy...')
            attacked[move[0]][move[1]]='x'
        else:
            print('You hit him')
            attacked[move[0]][move[1]]='x'
    
    if board[move[0]][move[1]]==' ':
        print("You missed")
        attacked[move[0]][move[1]]='.'

def is_hit(move,board,attacked):
    if board[move[0]][move[1]]=='X':
        return True
    return False

def main()
    k=1

    while is_alive(board1,attacked1) and is_alive(board2,attacked2):
        if k==1:
            move=input_move(attacked1,board1)
            attacked1=make_move(move,board1,attacked1)
            if not is_hit(move,board1,attacked1):
                k=2
        if k==2:
            move=input_move(attacked2)
            attacked2=make_move(move,board2,attacked2)
            if not is_hit(move,board2,attacked2):
                k=1

    if is_alive(board1,attacked1):
        print('First player is a winner. Congratulations')
    else:
        print('Second player is a winner. Congratulations')

if __name__=='__main__':
    main()