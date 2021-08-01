"""
https://www.acmicpc.net/problem/13904
13904.과제
골드3
풀이1.84ms
"""
import sys

input = sys.stdin.readline
N = int(input())
tasks = [tuple(map(int, input().split())) for _ in range(N)]
tasks.sort(key=lambda x: (-x[1], -x[0]))
visited = [False] * 1001
ans = 0

for task in tasks:
    index = task[0]
    while index:
        if not visited[index]:
            visited[index] = True
            ans += task[1]
            break
        index -= 1

print(ans)