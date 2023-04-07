"""
https://www.acmicpc.net/problem/16508
16508.전공책
풀이2.100ms
"""
import sys
from collections import Counter
input = sys.stdin.readline


def select_book(index, total_price):
    global alphabet_count, sheep_count
    if index == N:
        is_valid = True
        temp = Counter(alphabet_count)
        for alphabet in title:
            if alphabet not in temp or temp[alphabet] == 0:
                is_valid = False
                break
            temp[alphabet] -= 1
        if is_valid:
            answer = min(answer, total_price)
        return
    if answer <= total_price:
        return

    current_counter = Counter(books[index][1])

    alphabet_count += current_counter
    select_book(index + 1, total_price + int(books[index][0]))
    alphabet_count -= current_counter

    select_book(index + 1, total_price)


title = input().rstrip()
N = int(input())
books = [tuple(input().split()) for _ in range(N)]
sheep_count = sys.maxsize
count = 0
alphabet_count = Counter()
select_book(0, 0)
print(sheep_count if sheep_count != sys.maxsize else -1)