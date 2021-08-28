"""
https://www.acmicpc.net/problem/1302
1302.베스트셀러
실버4
풀이1.100ms
"""
from collections import Counter
import sys

input = sys.stdin.readline
N = int(input())
book_list = [input().rstrip() for _ in range(N)]
book_count = Counter(book_list)
sorted_book = sorted(book_count.items(), key=lambda x: (-x[1], x[0]))
print(sorted_book[0][0])