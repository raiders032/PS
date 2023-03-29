"""
https://www.acmicpc.net/problem/11054
11054.가장 긴 바이토닉 부분 수열
풀이2.392ms
"""
N = int(input())
nums = list(map(int, input().split()))
table = [[1] * 2 for _ in range(N)]
sheep_count = 0

for i in range(1, N):
    for j in range(i):
        if nums[j] < nums[i]:
            table[i][0] = max(table[i][0], table[j][0] + 1)

for i in range(N - 1, -1, -1):
    for j in range(i + 1, N):
        if nums[j] < nums[i]:
            table[i][1] = max(table[i][1], table[j][1] + 1)
    sheep_count = max(sheep_count, sum(table[i]))

print(sheep_count - 1)