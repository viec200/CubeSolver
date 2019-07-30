def analyze_corner(corner):
    W_list = ["A E R", "B N Q", "C J M", "D F I"]
    O_list = ["A E R", "D F I", "G L U", "H S X"]
    G_list = ["D F I", "C J M", "K P V", "G L U"]
    R_list = ["C J M", "B N Q", "O T W", "K P V"]
    B_list = ["B N Q", "A E R", "H S X", "O T W"]
    Y_list = ["G L U", "K P V", "O T W", "H S X"]

    relevant_lists = []

    for position, color in corner.items():
        if color == "W":
            relevant_lists.append(W_list)
        elif color == "O":
            relevant_lists.append(O_list)
        elif color == "G":
            relevant_lists.append(G_list)
        elif color == "R":
            relevant_lists.append(R_list)
        elif color == "B":
            relevant_lists.append(B_list)
        else:
            relevant_lists.append(Y_list)

    possibilities = []
    for corner1 in relevant_lists[0]:
        for corner2 in relevant_lists[1]:
            if corner1 == corner2:
                possibilities.append(corner1)

    for index in range(2):
        for corner3 in relevant_lists[2]:
            if possibilities[index] == corner3:
                possibilities.append(corner3)

    correct_corner = possibilities[-1].split(' ')

    W_list = ["A", "B", "C", "D"]
    O_list = ["E", "F", "G", "H"]
    G_list = ["I", "J", "K", "L"]
    R_list = ["M", "N", "O", "P"]
    B_list = ["Q", "R", "S", "T"]
    Y_list = ["U", "V", "W", "X"]

    corner_soln = {}

    def getSoln(x_list):
        for loc1 in correct_corner:
            for loc2 in x_list:
                if loc1 == loc2:
                    return loc1

    for position, color in corner.items():
        if color == "W":
            corner_soln[position] = getSoln(W_list)
        elif color == "O":
            corner_soln[position] = getSoln(O_list)
        elif color == "G":
            corner_soln[position] = getSoln(G_list)
        elif color == "R":
            corner_soln[position] = getSoln(R_list)
        elif color == "B":
            corner_soln[position] = getSoln(B_list)
        else:
            corner_soln[position] = getSoln(Y_list)

    return corner_soln