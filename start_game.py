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
