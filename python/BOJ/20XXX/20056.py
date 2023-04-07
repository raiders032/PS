"""
https://www.acmicpc.net/problem/20056
20056.마법사 상어와 파이어볼
풀이1.384ms
"""
import sys
from collections import deque
from collections import defaultdict
input = sys.stdin.readline


def operation1():
    visited = defaultdict(list)

    for _ in range(len(fire_balls)):
        r, c, m, s, d = fire_balls.popleft()
        next_r = (r + dx[d] * s) % N if dx[d] else (r + (N + dx[d] * s)) % N
        next_c = (c + dy[d] * s) % N if dy[d] else (c + (N + dy[d] * s)) % N
        visited[(next_r, next_c)].append((next_r, next_c, m, s, d))

    for key, fire_ball_list, in visited.items():
        if len(fire_ball_list) == 1:
            fire_balls.append(fire_ball_list[0])
            continue
        operation2(fire_ball_list)


def operation2(fire_ball_list):
    r = fire_ball_list[0][0]
    c = fire_ball_list[0][1]
    m = 0
    s = 0

    is_all_even = True
    is_all_odd = True
    for fire_ball in fire_ball_list:
        m += fire_ball[2]
        s += fire_ball[3]
        if fire_ball[4] % 2 == 0:
            is_all_odd = False
        else:
            is_all_even = False

    m = m // 5
    s = s // len(fire_ball_list)

    if m == 0:
        return

    if is_all_odd or is_all_even:
        for d in [0, 2, 4, 6]:
            fire_balls.append((r, c, m, s, d))
    else:
        for d in [1, 3, 5, 7]:
            fire_balls.append((r, c, m, s, d))


dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]
N, M, K = map(int, input().split())
fire_balls = deque()
for _ in range(M):
    fire_balls.append(list(map(int, input().split())))

for _ in range(K):
    operation1()

sheep_count = 0
while fire_balls:
    r, c, m, s, d, = fire_balls.pop()
    sheep_count += m
print(sheep_count)