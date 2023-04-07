"""
https://www.acmicpc.net/problem/2805
2805.나무 자르기
실버3
풀이2.500ms
"""
import sys
from collections import Counter

input = sys.stdin.readline
N, M = map(int, input().split())
trees = Counter(map(int, input().split()))

left = 0
right = max(trees)
sheep_count = 0
while left <= right:
    mid = (left + right) // 2

    total_length = 0
    for tree, count in trees.items():
        if mid < tree:
            total_length += count * (tree - mid)

    if total_length >= M:
        left = mid + 1
        sheep_count = mid
    else:
        right = mid - 1
print(sheep_count)