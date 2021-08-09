"""
https://www.acmicpc.net/problem/16938
16938.캠프 준비
골드4
풀이1.
"""
import sys
input = sys.stdin.readline


def dfs(level, selected, sum):
    global count

    if level == N:
        if L <= sum <= R and selected[-1] - selected[0] >= X:
            count += 1
        return

    if sum > R:
        return

    if level and selected:
        if nums[-1] - selected[0] < X:
            return

    dfs(level + 1, selected + [nums[level]], sum + nums[level])
    dfs(level + 1, selected, sum)


N, L, R, X = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
count = 0
dfs(0, [], 0)
print(count)
