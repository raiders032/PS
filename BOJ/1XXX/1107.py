"""
1107번 리모컨
골드5
브루트포스
풀이 2: 5236 ms
"""
import sys


def dfs(level, num):
    global res
    if level:
        res = min(res, abs(num - channel) + level)
        if level == limit:
            return
    for i in range(10):
        if is_broken[i]:
            continue
        dfs(level + 1, num * 10 + i)


input = sys.stdin.readline
channel = int(input())
limit = len(str(channel))+1
M = int(input())
res = abs(channel - 100)
is_broken = [False] * 10
for i in list(map(int, input().rstrip().split())):
    is_broken[i] = True
dfs(0, 0)
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

6
9
0 2 3 4 5 6 7 8 9
6

11 
8 
1 3 4 5 6 7 8 9
10

12 
9 
0 1 3 4 5 6 7 8 9
11

0
1
1
1
"""
