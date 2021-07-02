"""
https://www.acmicpc.net/problem/5397
5397.키로거
실버3
자료구조, 덱, 스택
풀이2.1280ms
"""
import sys

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    left = []
    right = []
    for char in list(input().rstrip()):
        if char == '<':
            if not left:
                continue
            right.append(left.pop())
        elif char == '>':
            if not right:
                continue
            left.append(right.pop())
        elif char == '-':
            if not left:
                continue
            left.pop()
        else:
            left.append(char)

    print(''.join(left + right[::-1]))
