"""
1107번 리모컨 골드5
브루트포스
"""

import sys

is_broken = [False] * 10
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
res = abs(N - 100)

for x in map(int, sys.stdin.readline().rstrip().split()):
    is_broken[x] = True

for num in range(1000000):
    for digit in set(map(int, str(num))):
        if is_broken[digit]:
            break
    else:
        res = min(res, abs(N - num) + len(str(num)))
print(res)

"""
368453
8
0 5 4 6 9 8 3 7
146237

431392
9
0 1 2 4 5 9 7 6 8
98065

0
3
0 1 2
4

888
3
7 8 9
116
"""
