import random

positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
moves = ['', '', '', '', '', '', '', '', '']
current_player = None
computer_player = None


def init_game():
    global positions, moves, current_player, computer_player
    positions = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    moves = ['', '', '', '', '', '', '', '', '']
    computer_player = None
    current_player = None


def get_board(p, m):
    return f'''
    ???????{" ":9}?? ???
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
    ???????? ?????? ??????? ??!
    {get_board(positions, moves)}
    ???? ????? ???? ???? ???????? ??! ''')


def get_move(player):
    move = None

    while move not in positions:
        move = int(input(f'''??????? {player}, ????????? ??????? ??: '''))
    return move


def update_positions(move):
    positions[move - 1] = ''


def update_moves(move, player):
    moves[move - 1] = player


# ????????? ?????? ?????? ??????? ????????
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


def get_computer_player():
    return random.choice('X', 'O')


def get_computer_move():
    available_positions = list(filter(lambda item: item != '', positions))
    random_index = random.randint(0, len(available_positions) - 1)
    return available_positions[random_index]


while True:
    start_game()
    current_player = get_first_player()
    computer_player = get_computer_player()

    while True:
        move = get_move(
            current_player
        ) if current_player != computer_player else get_computer_move()
        update_positions(move)
        update_moves(move, current_player)
        print(get_board(positions, moves))
        game_status = check_game()

        if game_status == 'DECIDED':
            print(f'??????? ???????. ??????? {current_player} ??????.')
            break

        if game_status == 'TIE':
            print(f'??????? ???????. ??????? ???????.')
            break

        current_player = 'O' if current_player == 'X' else 'X'

    if input(f'????? ???????? ??? Y, ??????? ??? N ????? ??! ') == 'N':
        break
    init_game()
