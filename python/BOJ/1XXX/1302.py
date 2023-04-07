"""
https://www.acmicpc.net/problem/1302
1302.베스트셀러
실버4
풀이2.92ms
"""
import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
books = Counter([input().rstrip() for _ in range(N)])
books = sorted(books.items(), key=lambda x: (-x[1], x[0]))
print(books[0][0])
