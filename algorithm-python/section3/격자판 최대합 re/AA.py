N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0
for r in range(N):
    row_sum = 0
    col_cum = 0
    for c in range(N):
        row_sum += arr[r][c]
        col_cum += arr[c][r]
    ans = max(ans, row_sum, col_cum)

dia_sum1 = 0
dia_sum2 = 0
for i in range(N):
    dia_sum1 += arr[i][i]
    dia_sum2 += arr[i][N-1-i]
ans = max(ans, dia_sum1, dia_sum2)
print(ans)
