"""
https://www.acmicpc.net/problem/10773
10773.제로
실버4
풀이1.120ms
"""
import sys

input = sys.stdin.readline
K = int(input())
stack = []

for num in [int(input()) for _ in range(K)]:
    if num == 0:
        stack.pop()
        continue
    stack.append(num)

print(sum(stack))