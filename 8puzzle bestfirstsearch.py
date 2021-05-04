from copy import deepcopy
open_list = []
visited = []

ss = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
gs = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
# ss = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
# gs = [[2, 8, 3], [1, 6, 4], [7, 0, 5]]

def printpath():
    i = 0
    while(i < len(visited)):
        state = visited[i]
        print("state: ")
        for j in range(3):
            print(state[j][0], state[j][1], state[j][2])

        i += 1

def checkgoal(state, goal):
    if state == goal:
        return True
    return False

def index(state):
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                return [i, j]

def heuristic(state):
    incorrectpos = 0
    for i in range(len(state)):
        for j in range(len(state[0])):
            if state[i][j] == 0:
                continue
            if state[i][j] != gs[i][j]:
                incorrectpos += 1
    return incorrectpos

def up(state, x, y):
    s = deepcopy(state)
    if 0 < x <= 2:
        temp = s[x][y]
        s[x][y] = s[x - 1][y]
        s[x - 1][y] = temp
        if s in open_list or s in visited:
            return [s, -1]
        h = heuristic(s)
        return [s, h]
    return [s, -1]

def down(state, x, y):
    s = deepcopy(state)
    if 0 <= x < 2:
        temp = s[x][y]
        s[x][y] = s[x + 1][y]
        s[x + 1][y] = temp
        if s in open_list or s in visited:
            return [s, -1]
        h = heuristic(s)

        return [s, h]
    return [s, -1]

def right(state, x, y):
    s = deepcopy(state)
    if 0 <= y < 2:
        temp = s[x][y]
        s[x][y] = s[x][y + 1]
        s[x][y + 1] = temp
        if s in open_list or s in visited:
            return [s, -1]
        h = heuristic(s)
        return [s, h]
    return [s, -1]

def left(state, x, y):
    s = deepcopy(state)
    if 0 < y <= 2:
        temp = s[x][y]
        s[x][y] = s[x][y - 1]
        s[x][y - 1] = temp
        if s in open_list or s in visited:
            return [s, -1]
        h = heuristic(s)
        return [s, h]
    return [s, -1]


if __name__ == '__main__':
    open_list.append(ss)
    while len(open_list) != 0:
        first = open_list[0]
        visited.append(first)
        open_list.pop()
        if checkgoal(first, gs):
            print("found")
            break
        ind = index(first)
        h1 = left(first, ind[0], ind[1])
        h2 = right(first, ind[0], ind[1])
        h3 = up(first, ind[0], ind[1])
        h4 = down(first, ind[0], ind[1])
        hvalues = [{"h": "h1", "value": h1[1], "state": h1[0]}, {"h": "h2", "value": h2[1], "state": h2[0]}, {"h": "h3", "value": h3[1], "state": h3[0]}, {"h": "h4", "value": h4[1], "state": h4[0]}]
        hvalues_sorted = sorted(hvalues, key = lambda i: i["value"], reverse=True)
        for i in range(len(hvalues_sorted)):
            if hvalues_sorted[i]["value"] != -1:
                open_list.insert(0, hvalues_sorted[i]["state"])

    printpath()
    print(f"Total moves: {len(visited)}")