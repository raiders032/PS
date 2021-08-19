"""
https://www.acmicpc.net/problem/9663
9663.N-Queen
골드5
풀이1.5844ms(PyPy3)
"""


def dfs(x):
    global ans

    if x == N - 1:
        ans += 1
        return

    row = x + 1

    for col in range(N):
        if col_visited[col] or right_dia_visited[row - col] or left_dia_visited[row + col]:
            continue
        col_visited[col] = True
        right_dia_visited[row - col] = True
        left_dia_visited[row + col] = True
        dfs(row)
        col_visited[col] = False
        right_dia_visited[row - col] = False
        left_dia_visited[row + col] = False


N = int(input())
col_visited = [False] * N
left_dia_visited = [False] * (2 * N - 1)
right_dia_visited = [False] * (2 * N - 1)
ans = 0

for col in range(N):
    col_visited[col] = True
    right_dia_visited[-col] = True
    left_dia_visited[col] = True

    dfs(0)

    col_visited[col] = False
    right_dia_visited[-col] = False
    left_dia_visited[col] = False

print(ans)
