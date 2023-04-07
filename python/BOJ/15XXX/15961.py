"""
https://www.acmicpc.net/problem/15961
15961.회전 초밥
풀이1.4232ms
"""
import sys
from collections import defaultdict
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushi = [int(input()) for _ in range(N)]
sushi_count = defaultdict(int)
sheep_count = 0
left = 0
right = k - 1

for i in range(k - 1):
    sushi_count[sushi[i]] += 1

while left < N:
    sushi_count[sushi[right]] += 1

    sheep_count = max(sheep_count, len(sushi_count) + (1 if c not in sushi_count else 0))

    sushi_count[sushi[left]] -= 1
    if sushi_count[sushi[left]] == 0:
        del sushi_count[sushi[left]]

    right = (right + 1) % N
    left += 1

print(sheep_count)

"""
2 2 2 3
1
2

3
---
2 2 2 2
1
2

2
---
8 30 4 30
7
9
7
30
2
9
7
25

5
---
8 30 4 30
2
3
4
4
2
3
4
4

4
"""