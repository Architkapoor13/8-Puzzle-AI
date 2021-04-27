from copy import deepcopy
open_list = []
visited = []
def index(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return [i, j]

def goal_test(current_state, goal_state):
    if current_state == goal_state:
        return True
    else:
        return False

def up(current_state, i, j):
    state = deepcopy(current_state)
    if 0 < i <= 2:
        state[i - 1][j], state[i][j] = state[i][j], state[i - 1][j]
        if state not in visited:
            open_list.insert(0, state)
    else:
        pass


def down(current_state, i, j):
    state = deepcopy(current_state)
    if 0 <= i < 2:
        state[i + 1][j], state[i][j] = state[i][j], state[i + 1][j]
        if state not in visited:
            open_list.insert(0, state)
    else:
        pass


def right(current_state, i, j):
    state = deepcopy(current_state)
    if 0 <= j < 2:
        state[i][j + 1], state[i][j] = state[i][j], state[i][j + 1]
        if state not in visited:
            open_list.insert(0, state)
    else:
        pass

def left(current_state, i, j):
    state = deepcopy(current_state)
    if 0 < j <= 2:
        state[i][j - 1], state[i][j] = state[i][j], state[i][j - 1]
        if state not in visited:
            open_list.insert(0, state)
    else:
        pass


if __name__ == "__main__":
    start_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    goal_state = [[2, 8, 1], [0, 4, 3], [7, 6, 5]]
    # start_state = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
    # goal_state = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    print(f"Finding the state = {goal_state}")
    open_list.append(start_state)
    moves = 0
    while len(open_list) != 0:
        s = deepcopy(open_list[0])
        open_list.pop(0)
        if goal_test(s, goal_state):
            print(f"found: {s}")
            break

        zero_index = index(s)
        up(s, zero_index[0], zero_index[1])
        right(s, zero_index[0], zero_index[1])
        down(s, zero_index[0], zero_index[1])
        left(s, zero_index[0], zero_index[1])

        visited.append(s)
        moves += 1

    print(f"Total number of moves: {moves + 1}")