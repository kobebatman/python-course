import random

positions = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
moves = ['', '', '', '', '', '', '', '', '']
current_player = None

def init_game():
	global positions, moves, current_player
	positions = [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
	moves = ['', '', '', '', '', '', '', '', '']
	current_player = None

def get_board(p, m):
    return f'''
    БАЙРЛАЛ{" ":9}ҮР ДҮН

    {p[0]:^3}|{p[1]:^3}|{p[2]:^3}{" ":5}{m[0]:^3}|{m[1]:^3}|{m[2]:^3}
    --- --- ---{" ":5}--- --- ---
    {p[3]:^3}|{p[4]:^3}|{p[5]:^3}{" ":5}{m[3]:^3}|{m[4]:^3}|{m[5]:^3}
    --- --- ---{" ":5}--- --- ---
    {p[6]:^3}|{p[7]:^3}|{p[8]:^3}{" ":5}{m[6]:^3}|{m[7]:^3}|{m[8]:^3}
    '''

def get_first_player():
    return 'X' if bool(random.randint(0, 1)) else 'O'

def start_game():
    input(f'''
    ТОГЛООМД ТАВТАЙ МОРИЛНО УУ!
    {get_board(positions, moves)}
    ЯМАР НЭГЭН ТОВЧ ДАРЖ ЭХЛҮҮЛНЭ ҮҮ! ''')

def get_move(player):
    move = None
    
    while move not in positions:
        move = int(input(f'''ТОГЛОГЧ {player}, БАЙРЛАЛАА ОРУУЛНА УУ: '''))
    return move

def update_positions(move):
    positions[move - 1] = ''

def update_moves(move, player):
    moves[move - 1] = player

# Тоглоомын тухайн мөчийн төлвийг буцаадаг
def check_game():
    # check rows
    for row in range(1, 8, 3):
        prev_state = moves[row - 1]
        is_same = True

        for step in range(0, 3):
            is_same = is_same and (moves[row + step - 1] == prev_state)
            prev_state = moves[row + step - 1]

        if is_same and prev_state != '':
            return 'DECIDED'
    
    # check columns
    for col in range(1, 4):
        prev_state = moves[col - 1]
        is_same = True

        for step in range(0, 7, 3):
            is_same = is_same and (moves[col + step - 1] == prev_state)
            prev_state = moves[col + step - 1]

        if is_same and prev_state != '':
            return 'DECIDED'

    # check diagonal-1
    prev_state = moves[0]
    is_same = True
    for k in range(1, 10, 4):
        is_same = is_same and (moves[k - 1] == prev_state)
        prev_state = moves[k - 1]
    if is_same and prev_state != '':
        return 'DECIDED'

    # check diagonal-2
    prev_state = moves[2]
    is_same = True
    for k in range(3, 8, 2):
        is_same = is_same and (moves[k - 1] == prev_state)
        prev_state = moves[k - 1]
    if is_same and prev_state != '':
        return 'DECIDED'

    # is tied or not?
    if moves.count('') == 0:
        return 'TIE'

    return 'NOT-YET'

while True:
    start_game()
    current_player = get_first_player()

    while True:
        move = get_move(current_player)
        update_positions(move)
        update_moves(move, current_player)
        print(get_board(positions, moves))
        game_status = check_game()

        if game_status == 'DECIDED':
            print(f'ТОГЛООМ ДУУСЛАА. ТОГЛОГЧ {current_player} ХОЖЛОО.')
            break

        if game_status == 'TIE':
            print(f'ТОГЛООМ ДУУСЛАА. ТОГЛОЛТ ТЭНЦЛЭЭ.')
            break

        current_player = 'O' if current_player == 'X' else 'X'
    
    if input(f'ДАХИН ЭХЛҮҮЛЭХ БОЛ Y, ДУУСГАХ БОЛ N ДАРНА УУ! ') == 'N':
        break
    
	init_game()