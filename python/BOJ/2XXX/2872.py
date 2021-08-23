"""
https://www.acmicpc.net/problem/2872
2872.우리집엔 도서관이 있어
실버3
풀이2.220ms
"""
import sys

input = sys.stdin.readline
N = int(input())
books = [int(input()) for _ in range(N)]
ans = N

for index in range(N - 1, -1, -1):
    if books[index] == N:
        ans -= 1
        N -= 1

print(ans)
