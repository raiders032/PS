N, M = map(int, input().split())
adj_mat = [[0] * N for _ in range(N)]
for _ in range(M):
    v1, v2, w = map(int, input().split())
    adj_mat[v1-1][v2-1] = w
for row in adj_mat:
    for x in row:
        print(x, end=' ')
    print()
