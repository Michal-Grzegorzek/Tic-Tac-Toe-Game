field_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

answers = []
p2_answers = []

print('Welcome in Tic Tac Toe Game!')


def game_table():
    print(f'\n{field_list[0]}  |  {field_list[1]}  |  {field_list[2]}\n'
          f'-------------\n'
          f'{field_list[3]}  |  {field_list[4]}  |  {field_list[5]}\n'
          f'-------------\n'
          f'{field_list[6]}  |  {field_list[7]}  |  {field_list[8]}\n')


def check_position_x(pos):
    try:
        if 9 < int(pos) or int(pos) < 0:
            print('The position is off the table game!')
            next_field = input('Player move no.1 (X), enter new position:')
            check_position_x(next_field)

    except ValueError:
        print("Use only numbers!")
        next_field = input('Player move no.1 (X), enter new position:')
        check_position_x(next_field)

    for z in answers:
        if z == pos:
            print('The field is already taken')
            next_field = input('Player move no.1 (X), enter new position:')
            check_position_x(next_field)

    for i in field_list:
        if i == pos:
            field_list[int(i)-1] = 'X'
            answers.append(pos)



def check_position_y(pos):

    try:
        if 9 < int(pos) or int(pos) < 0:
            print('The position is off the table game!')
            next_field = input('Player move no.2 (O), enter new position:')
            check_position_y(next_field)

    except ValueError:
        print("Use only numbers!")
        next_field = input('Player move no.2 (O), enter new position:')
        check_position_y(next_field)

    for z in answers:
        if z == pos:
            print('The field is already taken')
            next_field = input('Player move no.2 (O), enter new position:')
            check_position_y(next_field)

    for i in field_list:
        if i == pos:
            field_list[int(i) - 1] = 'O'
            answers.append(pos)


def check_win():
    if field_list[0] == field_list[1] == field_list[2] or \
            field_list[3] == field_list[4] == field_list[5] or \
            field_list[6] == field_list[7] == field_list[8] or \
            field_list[0] == field_list[3] == field_list[6] or \
            field_list[1] == field_list[4] == field_list[7] or \
            field_list[2] == field_list[5] == field_list[8] or \
            field_list[0] == field_list[4] == field_list[8] or \
            field_list[2] == field_list[4] == field_list[6]:
        return True


game_table()


for x in range(5):

    X_move = input('Player move no.1 (X), enter position:')

    check_position_x(X_move)

    game_table()

    if check_win():
        print('Player # 1 (X) has won!')
        break

    if x == 4:
        print('Draw!')
        break

    Y_move = input('Player move no.2 (O), enter position:')

    check_position_y(Y_move)

    if check_win():
        print('Player # 2 (O) has won!')
        break

    game_table()
