"""
https://www.acmicpc.net/problem/1493
1493.박스 채우기
골드4
풀이1.
"""
import sys
import heapq
sys.setrecursionlimit(10 ** 6)


def solve(x, y, z):
    if x == 0 or y == 0 or z == 0:
        return 0

    seen = []

    while cubes:
        exp, num = heapq.heappop(cubes)
        length = 2 ** -exp

        if length > x or length > y or length > z:
            seen.append((exp, num))
            continue

        for cube in seen:
            heapq.heappush(cubes, (cube[0], cube[1]))

        if num > 1:
            heapq.heappush(cubes, (exp, num - 1))

        if length == x and length == y and length == z:
            return 1

        return 1 + solve(x, y - length, z) + solve(x - length, length, z) + solve(length, length, z - length)

    print(-1)
    exit(0)


input = sys.stdin.readline
L, W, H = map(int, input().split())
N = int(input())

cubes = list()
for _ in range(N):
    exp, num = map(int, input().split())
    heapq.heappush(cubes, (-exp, num))

print(solve(L, W, H))

