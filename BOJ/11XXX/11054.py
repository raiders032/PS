"""
11054.가장 긴 바이토닉 부분 수열
골드3
다이나믹프로그래밍
"""
N = int(input())
arr = list(map(int, input().split()))
dp_up = [1] * N
dp_down = [1] * N
res = 1
for i in range(1, N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp_up[i] = max(dp_up[i], dp_up[j] + 1)

for i in range(N - 2, -1, -1):
    for j in range(i + 1, N):
        if arr[j] < arr[i]:
            dp_down[i] = max(dp_down[i], dp_down[j] + 1)
    res = max(res, dp_up[i] + dp_down[i] - 1)

print(res)
