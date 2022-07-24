"""
https://www.acmicpc.net/problem/16508
16508.전공책
풀이1.1800ms(PyPy3)
"""
import itertools
import sys
from collections import Counter

input = sys.stdin.readline

title = input().rstrip()
N = int(input())
books = [tuple(input().split()) for _ in range(N)]
answer = sys.maxsize
for i in range(1, N + 1):
    for selected_books in itertools.combinations(books, i):
        total_price = 0
        char_count = Counter()
        for selected_book in selected_books:
            total_price += int(selected_book[0])
            char_count += Counter(selected_book[1])
        is_valid = True
        for char in title:
            if char not in char_count or char_count[char] == 0:
                is_valid = False
                break
            char_count[char] -= 1

        if is_valid:
            answer = min(answer, total_price)
print(answer if answer != sys.maxsize else -1)