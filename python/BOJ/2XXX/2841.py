"""
https://www.acmicpc.net/problem/2841
2841.외계인의 기타 연주
실버1
풀이1.1044ms
"""
import sys

input = sys.stdin.readline
N, P = map(int, input().split())
stacks = [list([0]) for _ in range(N + 1)]
count = 0
for _ in range(N):
    n, p = map(int, input().split())

    if stacks[n][-1] < p:
        count += 1
        stacks[n].append(p)

    elif stacks[n][-1] > p:
        while p < stacks[n][-1]:
            stacks[n].pop()
            count += 1
        if p == stacks[n][-1]:
            continue
        stacks[n].append(p)
        count += 1

print(count)
