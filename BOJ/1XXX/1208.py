"""
https://www.acmicpc.net/problem/1208
1208.부분수열의 합 2
골드2
이분탐색,중간에서만나기,투포인터
풀이1.3276ms
"""
import sys


def dfs(level, num, sum):
    if level >= limits[num]:
        sums[num].append(sum)
        return
    dfs(level + 1, num, sum + arr[num][level])
    dfs(level + 1, num, sum)


input = sys.stdin.readline
N, M = map(int, input().split())
tmp = list(map(int, input().split()))
arr = [tmp[:N // 2], tmp[N // 2:]]
limits = [len(arr[0]), len(arr[1])]
sums = [list() for _ in range(2)]
for i in range(2):
    dfs(0, i, 0)
sums[0].sort()
sums[1].sort(reverse=True)
left = 0
right = 0
res = 0

while left < len(sums[0]) and right < len(sums[1]):
    if sums[0][left] + sums[1][right] == M:
        left_duplicate_count = 1
        while left + left_duplicate_count < len(sums[0]) and sums[0][left] == sums[0][left + left_duplicate_count]:
            left_duplicate_count += 1

        right_duplicate_count = 1
        while right + right_duplicate_count < len(sums[1]) and sums[1][right] == sums[1][right + right_duplicate_count]:
            right_duplicate_count += 1

        res += left_duplicate_count * right_duplicate_count
        left += left_duplicate_count
        right += right_duplicate_count

    elif sums[0][left] + sums[1][right] > M:
        right += 1

    elif sums[0][left] + sums[1][right] < M:
        left += 1

if M == 0:
    print(res - 1)
else:
    print(res)
