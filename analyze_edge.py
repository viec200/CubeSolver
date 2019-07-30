def analyze_edge(edge):
    W_list = ["A Q", "B M", "C I", "D E"]
    O_list = ["D E", "F L", "G X", "H R"]
    G_list = ["C I", "J P", "K U", "F L"]
    R_list = ["B M", "N T", "O V", "J P"]
    B_list = ["A Q", "H R", "S W", "N T"]
    Y_list = ["K U", "O V", "S W", "G X"]

    relevant_lists = []

    for position, color in edge.items():
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

    correct_edge = ""

    for edge1 in relevant_lists[0]:
        for edge2 in relevant_lists[1]:
            if edge1 == edge2:
                correct_edge = edge1.split(' ')

    W_list = ["A", "B", "C", "D"]
    O_list = ["E", "F", "G", "H"]
    G_list = ["I", "J", "K", "L"]
    R_list = ["M", "N", "O", "P"]
    B_list = ["Q", "R", "S", "T"]
    Y_list = ["U", "V", "W", "X"]

    edge_soln = {}

    def getSoln(x_list):
        for loc1 in correct_edge:
            for loc2 in x_list:
                if loc1 == loc2:
                    return loc1

    for position, color in edge.items():
        if color == "W":
            edge_soln[position] = getSoln(W_list)
        elif color == "O":
            edge_soln[position] = getSoln(O_list)
        elif color == "G":
            edge_soln[position] = getSoln(G_list)
        elif color == "R":
            edge_soln[position] = getSoln(R_list)
        elif color == "B":
            edge_soln[position] = getSoln(B_list)
        else:
            edge_soln[position] = getSoln(Y_list)

    return edge_soln