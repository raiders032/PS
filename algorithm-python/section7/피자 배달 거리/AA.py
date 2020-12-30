N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
pizza = []
selected = []
house = []
res = 10000


def dfs(cnt, idx):
    global res
    if cnt == M:
        sum_dist = 0
        for h_x, h_y in house:
            min_dist = 10000
            for p_x, p_y in selected:
                min_dist = min(min_dist, abs(p_x - h_x) + abs(p_y - h_y))
            sum_dist += min_dist
        res = min(res, sum_dist)
        return
    for i in range(idx, len(pizza)):
        selected.append((pizza[i][0], pizza[i][1]))
        dfs(cnt+1, i+1)
        selected.pop()


for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            house.append((i, j))
        elif board[i][j] == 2:
            pizza.append((i, j))

dfs(0, 0)
print(res)
