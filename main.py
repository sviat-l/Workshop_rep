def intro():
    print("Гра морський бій\nнумерація полів:")
    print("---------------------------------\n\
|a\\1| 2 | 3 | 4 | 5 | 6 | 7 | 8 |\n\
---------------------------------\n\
| b |   |   |   |   |   |   |   |\n\
---------------------------------\n\
| c |   |   |   |   |   |   |   |\n\
---------------------------------\n\
| d |   |   |   |   |   |   |   |\n\
---------------------------------\n\
| e |   |   |   |   |   |   |   |\n\
---------------------------------\n\
| f |   |   |   |   |   |   |   |\n\
---------------------------------\n\
| g |   |   |   |   |   |   |   |\n\
---------------------------------\n\
| h |   |   |   |   |   |   |   |\n\
---------------------------------")

def draw_board():
    for i in range(2):
        board = list(itertools.chain.from_iterable(board))
    print("---------------------------------")
    for i in range(8):
        print("|", board[0 + i * 8], "|", board[1 + i * 8], "|", board[2 + i * 8],\
             "|", board[3 + i * 8], "|", board[4 + i * 8],"|", board[5 + i * 8],"|",\
                  board[6 + i * 8],"|", board[7 + i * 8], "|")
        print("---------------------------------")

def generate_empty_board():
    empty_board = []
    for _ in range(8):
        empty_board.append([])
        for _ in range(8):
            empty_board[-1].append(' ')
    return empty_board

  
def player_input_board():
    set_with_used =set()
    board = generate_empty_board()
    avaliable_ships = [(1,1)]*4 + [(2,1)]*3+ [(3,1)]*2 + [(4,1)]

    board_set = set((i,j) for i in range(8) for j in range(8))
    while avaliable_ships:
        draw_board(board)
        print('available ships list ', avaliable_ships)
        print("print ship info in format 'a1' 'index in ship list'  'orientation'")
        print('Orientation options : "vertical" or "horizontal" ')

        try:
            coord, index_in_ship_list, orientation = input().split()
            ship = avaliable_ships[int(index_in_ship_list)]
        except:
            print('Error1  wrong input\n Try again')
            continue

        if orientation != 'vertical':
            ship = (ship[1], ship[0])

        starting_i = ord(coord[0]) - ord('a')
        starting_j = int(coord[1]) - 1

        set_for_current_ship = set()
        for num in range(ship[0]):
            set_for_current_ship.add((starting_j+num, starting_i))
        for num in range(ship[1]):
            set_for_current_ship.add((starting_j, starting_i + num))

        if  (set_with_used & set_for_current_ship) or (set_with_used-board_set) :
            print('Error2  list out of range\n Try again')
            continue
        avaliable_ships.pop(int(index_in_ship_list))
        set_with_used |= set_for_current_ship
        print(set_with_used)
        for (i,j) in set_with_used:
            print(board)
            board[i][j] = 'X'

    return board


def is_alive(board,attacked):
    alive=False
    for i in range(8):
        for j in range(8):
            if board[i][j]=='X' and attacked[i][j]!=' ':
                alive=True
                break
    return alive

def input_move(attacked1,board1):
    draw_board(attacked1)
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


board1=player_input_board()
board2=player_input_board()
attacked1=generate_empty_board()
attacked2=generate_empty_board()
def main():
    intro()
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