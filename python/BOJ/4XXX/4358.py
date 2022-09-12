"""
https://www.acmicpc.net/problem/4358
4358.생태학
풀이1.528ms
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

tree_count = defaultdict(int)
total_count = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    tree_count[tree] += 1
    total_count += 1

result = []
for tree, count in tree_count.items():
    result.append((tree, count / total_count * 100))
result.sort()

for tree, ratio in result:
    print(f'{tree} {ratio:.4f}')