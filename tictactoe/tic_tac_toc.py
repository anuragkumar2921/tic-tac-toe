import itertools
from colorama import Fore, Back, Style

game_size = int(input("enter the game board size : "))
game = [[0 for i in range(game_size)] for i in range(game_size)]


def win_validation(game_map):
    h = horizontal_winner(game_map)
    v = vertical_winner(game_map)
    d = diagonal_winner(game_map)
    d_r = diagonal_rev_winner(game_map)
    return h & v & d & d_r


def all_same(l):
    if l.count(l[0]) == len(l) and l[0] != 0:
        return True
    else:
        return False


def horizontal_winner(game_map):
    for row in game_map:
        if all_same(row):
            print(f"player {row[0]} is the winner horizontal (--)!!")
            return False
        return True


def diagonal_rev_winner(game_map):
    elements = []
    for row, col in enumerate(reversed(range(len(game_map)))):
        elements.append(game_map[row][col])

    if all_same(elements):
        print(f"player {elements[0]} is the winner diagonal (/) !!")
        return False
    return True


def diagonal_winner(game_map):
    elements = []
    for i in range(len(game_map)):
        elements.append(game_map[i][i])

    if all_same(elements):
        print(f"player {elements[0]} is the winner diagonal (\\)!!")
        return False
    return True


def vertical_winner(game_map):
    for col in range(len(game_map)):
        check = []
        for row in game_map:
            check.append(row[col])

        if all_same(check):
            print(f"player {check[0]} is the winner vertical (|)!!")
            return False
    return True


def game_board(game_map, player=0, row=0, col=0, just_display=False):
    try:
        if game_map[row][col] != 0:
            print("illegal move!!")
            return False
        if not just_display:
            game_map[row][col] = player
        print("   " + "  ".join([str(i) for i in range(len(game_map))]))

        for c, row in enumerate(game_map):
            colored_row = ""
            for item in row:
                if item == 0:
                    colored_row += "   "
                elif item == 1:
                    colored_row += Back.GREEN + '   ' + Style.RESET_ALL
                elif item == 2:
                    colored_row += Back.MAGENTA + '   ' + Style.RESET_ALL
            print(c, colored_row)
        return True
    except IndexError as e:
        print("Index out of range : ", e)
    except Exception as e:
        print("something went wrong : ", e)


play = True
game_board(game, just_display=True)
current_player_iter = itertools.cycle([1, 2])
current_player = next(current_player_iter)
fair_play = False
while play:
    if fair_play:
        current_player = next(current_player_iter)
    print(f"player : {current_player} turn now")
    row_choice = int(input("enter input row in (0,1,2) : "))
    col_choice = int(input("enter input column in (0, 1, 2) : "))
    fair_play = game_board(game, current_player, row_choice, col_choice)
    if not fair_play:
        continue
    play = win_validation(game)
