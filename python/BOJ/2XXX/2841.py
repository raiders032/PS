"""
https://www.acmicpc.net/problem/2841
2841.외계인의 기타 연주
실버1
풀이2.1072ms
"""
import sys

input = sys.stdin.readline
N, P = map(int, input().split())
stacks = [list() for _ in range(N + 1)]
count = 0
for _ in range(N):
    n, p = map(int, input().split())

    while stacks[n] and stacks[n][-1] > p:
        stacks[n].pop()
        count += 1

    if stacks[n] and stacks[n][-1] == p:
        continue

    stacks[n].append(p)
    count += 1

print(count)