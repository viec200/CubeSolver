from pip._vendor.distlib.compat import raw_input
from analyze_corner import analyze_corner
from analyze_edge import analyze_edge


def input():
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
               "T", "U", "V", "W", "X"]
    corner_dict = {}
    print("Input the corner colors.")

    for letter in letters:
        corner_dict[letter] = raw_input("> %s   " % letter)

    edge_dict = {}
    print("Input the edge colors.")

    for letter in letters:
        edge_dict[letter] = raw_input("> %s   " % letter)

    return corner_dict, edge_dict


def build_unsetups(piece_setups):
    piece_unsetups = {}

    for position, setup in piece_setups.items():
        setup_list = setup.split(' ')
        unsetup_list = []
        for index in range(len(setup_list)):
            unsetup_list.append(setup_list[-1 * (index + 1)])
        unsetup = " ".join(unsetup_list)

        piece_unsetups[position] = unsetup

    return piece_unsetups


def initialize_piece(piece_dict, piece_str):
    positions = piece_str.split('_')
    piece = {}
    for position in positions:
        piece[position] = piece_dict[position]
    return piece


def build_piece_soln(solved_piece_list):
    full_soln = {}
    for piece in solved_piece_list:
        for position, soln in piece.items():
            full_soln[position] = soln
    return full_soln


def build_step_list(buffer, piece_list, full_piece_soln):
    current_pos = buffer
    next_pos = full_piece_soln[buffer]
    solved = False
    step_list = []
    new_cycle = False

    while not solved:
        if current_pos != next_pos:
            step_list.append(next_pos)

        remove_pos_list = []
        if not new_cycle:
            for piece in piece_list:
                for position in piece:
                    if current_pos == position:
                        for pos in piece:
                            remove_pos_list.append(pos)
        new_cycle = False

        for pos in remove_pos_list:
            if full_piece_soln[pos] is not None:
                del full_piece_soln[pos]

        current_pos = next_pos
        next_pos = full_piece_soln.get(next_pos)
        if next_pos is None:
            try:
                current_pos = list(full_piece_soln)[0]
                next_pos = full_piece_soln[current_pos]
                new_cycle = True
            except:
                next_pos = None
        if next_pos is None:
            solved = True

    return step_list


def optimize_list(move_list):
    move_list = move_list.split(' ')
    move_list.append("placeholder")

    for move in move_list:
        if move == "":
            move_list.remove("")

    for index in range(len(move_list) - 2, -1, -1):
        current_move = move_list[index]
        next_move = move_list[index + 1]

        if current_move == next_move + "'" or next_move == current_move + "'":
            move_list.pop(index + 1)
            move_list.pop(index)

        if current_move == next_move + "2":
            move_list[index] = next_move + "'"
            move_list.pop(index + 1)
        elif next_move == current_move + "2":
            move_list[index] = current_move + "'"
            move_list.pop(index + 1)
        else:
            current_move_ = current_move.split("'")[0]
            next_move_ = next_move.split("'")[0]

            if current_move_ == next_move_ + "2":
                move_list[index] = next_move_
                move_list.pop(index + 1)
            if next_move_ == current_move_ + "2":
                move_list[index] = current_move_
                move_list.pop(index + 1)

        if current_move == next_move:
            if current_move == current_move.split("2")[0]:
                move_list[index] = current_move.split("'")[0] + "2"
                move_list.pop(index + 1)
            else:
                move_list.pop(index + 1)
                move_list.pop(index)

    move_list.remove("placeholder")
    move_list = " ".join(move_list)
    return move_list


corner_setups = {
    "B": "R2",
    "C": "F2 D",
    "D": "F2",
    "F": "F' D",
    "G": "F'",
    "H": "D' R",
    "I": "F R'",
    "J": "R'",
    "K": "F' R'",
    "L": "F2 R'",
    "M": "F",
    "N": "R' F",
    "O": "R2 F",
    "P": "R F",
    "Q": "R D'",
    "S": "D F'",
    "T": "R",
    "U": "D",
    "V": "",
    "W": "D'",
    "X": "D2"
}

edge_setups = {
    "A": "l2 D' l2",
    "C": "l2 D l2",
    "D": "",
    "E": "L d' L",
    "F": "d' L",
    "G": "L' d' L",
    "H": "d L'",
    "I": "l D' L2",
    "J": "d2 L",
    "K": "l D L2",
    "L": "L'",
    "N": "d L",
    "O": "D' l D L2",
    "P": "d' L'",
    "Q": "l' D L2",
    "R": "L",
    "S": "l' D' L2",
    "T": "d2 L'",
    "U": "D' L2",
    "V": "D2 L2",
    "W": "D L2",
    "X": "L2"
}

corner_unsetups = {
    "B": "R2",
    "C": "D' F2",
    "D": "F2",
    "F": "D' F",
    "G": "F",
    "H": "R' D",
    "I": "R F'",
    "J": "R",
    "K": "R F",
    "L": "R F2",
    "M": "F'",
    "N": "F' R",
    "O": "F' R2",
    "P": "F' R'",
    "Q": "D R'",
    "S": "F D'",
    "T": "R'",
    "U": "D'",
    "V": "",
    "W": "D",
    "X": "D2"
}

edge_unsetups = {
    "A": "l2 D l2",
    "C": "l2 D' l2",
    "D": "",
    "E": "L' d L'",
    "F": "L' d",
    "G": "L' d L",
    "H": "L d'",
    "I": "L2 D l'",
    "J": "L' d2",
    "K": "L2 D' l'",
    "L": "L",
    "N": "L' d'",
    "O": "L2 D' l' D",
    "P": "L d",
    "Q": "L2 D' l",
    "R": "L'",
    "S": "L2 D l",
    "T": "L d2",
    "U": "L2 D",
    "V": "L2 D2",
    "W": "L2 D'",
    "X": "L2"
}

corner_swap = "R U' R' U' R U R' F' R U R' U' R' F R"
edge_swap = "R U R' U' R' F R2 U' R' U' R U R' F'"

corner_dict, edge_dict = input()

A_E_R = initialize_piece(corner_dict, "A_E_R")
B_N_Q = initialize_piece(corner_dict, "B_N_Q")
C_J_M = initialize_piece(corner_dict, "C_J_M")
D_F_I = initialize_piece(corner_dict, "D_F_I")
G_L_U = initialize_piece(corner_dict, "G_L_U")
K_P_V = initialize_piece(corner_dict, "K_P_V")
O_T_W = initialize_piece(corner_dict, "O_T_W")
H_S_X = initialize_piece(corner_dict, "H_S_X")

A_Q = initialize_piece(edge_dict, "A_Q")
B_M = initialize_piece(edge_dict, "B_M")
C_I = initialize_piece(edge_dict, "C_I")
D_E = initialize_piece(edge_dict, "D_E")
F_L = initialize_piece(edge_dict, "F_L")
G_X = initialize_piece(edge_dict, "G_X")
H_R = initialize_piece(edge_dict, "H_R")
J_P = initialize_piece(edge_dict, "J_P")
K_U = initialize_piece(edge_dict, "K_U")
N_T = initialize_piece(edge_dict, "N_T")
O_V = initialize_piece(edge_dict, "O_V")
S_W = initialize_piece(edge_dict, "S_W")

corner_list = [A_E_R, B_N_Q, C_J_M, D_F_I, G_L_U, K_P_V, O_T_W, H_S_X]
corner_soln_list = []

edge_list = [A_Q, B_M, C_I, D_E, F_L, G_X, H_R, J_P, K_U, N_T, O_V, S_W]
edge_soln_list = []

for corner in corner_list:
    corner_soln_list.append(analyze_corner(corner))

for edge in edge_list:
    edge_soln_list.append(analyze_edge(edge))

full_corner_soln = build_piece_soln(corner_soln_list)
full_edge_soln = build_piece_soln(edge_soln_list)

corner_step_list = build_step_list("E", corner_list, full_corner_soln)
for letter in corner_step_list:
    if letter == "A" or letter == "E" or letter == "R":
        corner_step_list.remove(letter)

edge_step_list = build_step_list("B", edge_list, full_edge_soln)
for letter in edge_step_list:
    if letter == "B" or letter == "M":
        edge_step_list.remove(letter)

parity = True
if len(corner_step_list) % 2 == 0:
    parity = False

corner_move_list = []
edge_move_list = []

for letter in corner_step_list:
    corner_move_list.append(corner_setups[letter])
    corner_move_list.append(corner_swap)
    corner_move_list.append(corner_unsetups[letter])

for letter in edge_step_list:
    edge_move_list.append(edge_setups[letter])
    edge_move_list.append(edge_swap)
    edge_move_list.append(edge_unsetups[letter])

corner_move_list = " ".join(corner_move_list)
edge_move_list = " ".join(edge_move_list)

full_move_list = ""
if parity:
    full_move_list = corner_move_list + " R U' R' U' R U R D R' U' R D' R' U2 R' U' " + edge_move_list
else:
    full_move_list = corner_move_list + " " + edge_move_list

full_move_list = optimize_list(full_move_list)

print("Here is the solution. Assume the green side is facing you and the white side is facing up.")
print(full_move_list)
print("\nSolved in %d moves." % len(full_move_list.split(" ")))
