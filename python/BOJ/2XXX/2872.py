"""
https://www.acmicpc.net/problem/2872
2872.우리집엔 도서관이 있어
실버3
풀이3.240ms
"""
import sys

input = sys.stdin.readline
N = int(input())
books = [int(input()) for _ in range(N)]
sheep_count = 0
max_number = N

for i in range(N - 1, -1, -1):
    if books[i] < max_number:
        sheep_count += 1

    if books[i] == max_number:
        max_number -= 1

print(sheep_count)
