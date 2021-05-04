from copy import deepcopy

global current_state
visited=[]
ss = [[2, 8, 3], [1, 5, 4], [7, 6, 0]]
gs = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

def heuristic(state):
    noteaual = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                continue
            if state[i][j] != gs[i][j]:
                noteaual += 1
    return noteaual

def index(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return [i, j]


def up(state, x, y):
    s = deepcopy(state)
    if 0 < x <= 2:
        s[x][y], s[x - 1][y] = s[x - 1][y], s[x][y]
        print("up")
        for i in range(3):
            print(s[i][0], s[i][1], s[i][2])
        print("goal state")
        for i in range(3):
            print(gs[i][0], gs[i][1], gs[i][2])
        if current_state != s and s not in visited:
            return [s, heuristic(s)]
        return [[], -1]
    return [[], -1]

def down(state, x, y):
    s = deepcopy(state)
    if 0 <= x < 2:
        s[x][y], s[x + 1][y] = s[x + 1][y], s[x][y]
        print("down")
        for i in range(3):
            print(s[i][0], s[i][1], s[i][2])
        print("goal state")
        for i in range(3):
            print(gs[i][0], gs[i][1], gs[i][2])
        if current_state != s and s not in visited:
            return [s, heuristic(s)]
        return [[], -1]
    return [[], -1]

def right(state, x, y):
    s = deepcopy(state)
    if 0 <= y < 2:
        s[x][y], s[x][y + 1] = s[x][y + 1], s[x][y]
        print("right")
        for i in range(3):
            print(s[i][0], s[i][1], s[i][2])
        print("goal state")
        for i in range(3):
            print(gs[i][0], gs[i][1], gs[i][2])
        if current_state != s and s not in visited:
            return [s, heuristic(s)]
        return [[], -1]
    return [[], -1]

def left(state, x, y):
    s = deepcopy(state)
    if 0 < y <= 2:
        s[x][y], s[x][y - 1] = s[x][y - 1], s[x][y]
        print("left")
        for i in range(3):
            print(s[i][0], s[i][1], s[i][2])
        print("goal state")
        for i in range(3):
            print(gs[i][0], gs[i][1], gs[i][2])
        if current_state != s and s not in visited:
            return [s, heuristic(s)]
        return [[], -1]
    return [[], -1]

if __name__ == '__main__':
    current_state = ss
    while current_state != gs:
        print(f"Current state: {current_state}")
        visited.append(current_state)
        ind = index(current_state)
        h1 = left(current_state, ind[0], ind[1])
        h2 = right(current_state, ind[0], ind[1])
        h3 = up(current_state, ind[0], ind[1])
        h4 = down(current_state, ind[0], ind[1])
        hvalues = [{"h": "h1", "value": h1[1], "state": h1[0]}, {"h": "h2", "value": h2[1], "state": h2[0]},
                   {"h": "h3", "value": h3[1], "state": h3[0]}, {"h": "h4", "value": h4[1], "state": h4[0]}]
        hvalues_sorted = sorted(hvalues, key=lambda i: i["value"], reverse=True)
        flag = 0
        for i in range(len(hvalues_sorted)):
            if hvalues_sorted[i]["value"] == -1:
                continue
            if heuristic(current_state) > hvalues_sorted[i]["value"]:
                current_state = hvalues_sorted[i]["state"]
                flag = 1
                break
        if flag == 0:
            print("Goal state cannot be found!")
            break

    print(f"Total Moves: {len(visited)}")
