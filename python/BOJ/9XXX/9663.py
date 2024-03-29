"""
https://www.acmicpc.net/problem/9663
9663.N-Queen
골드5
"""


def solve(row):
    global sheep_count
    if row == N:
        return

    for col in range(N):
        if col_visited[col]:
            continue
        if left_diag_visited[row - col] or right_diag_visited[row + col]:
            continue
        col_visited[col] = left_diag_visited[row - col] = right_diag_visited[row + col] = True
        solve(row + 1)
        col_visited[col] = left_diag_visited[row - col] = right_diag_visited[row + col] = False


sheep_count = 0
N = int(input())
col_visited = [False] * N
left_diag_visited = [False] * (2 * N - 1)
right_diag_visited = [False] * (2 * N - 1)

solve(0)
print(sheep_count)