"""
https://www.acmicpc.net/problem/2812
2812.크게 만들기
풀이1.256ms
"""
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
number = list(input().rstrip())
stack = []
count = k

for i in range(n):
    while count and stack and stack[-1] < number[i]:
        stack.pop()
        count -= 1
    stack.append(number[i])

print(''.join(stack[:n - k]))
