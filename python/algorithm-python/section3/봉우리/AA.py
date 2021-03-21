N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
direction = [[-1, 0], [0, 1], [1, 0], [0, -1]]
cnt = 0
for i in range(N):
    for j in range(N):
        isMax = True
        for d in range(4):
            nx = i + direction[d][0]
            ny = j + direction[d][1]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if board[i][j] <= board[nx][ny]:
                isMax = False
        if isMax:
            cnt += 1
print(cnt)
