"""
https://www.acmicpc.net/problem/17451
17451.평행 우주
실버3
풀이1.356ms
"""
N = int(input())
velocity = list(map(int, input().split()))
min_velocity = velocity[-1]

for i in range(N - 1, 0, -1):
    if velocity[i - 1] >= min_velocity:
        min_velocity = velocity[i - 1]
    else:
        min_velocity = min_velocity // velocity[i - 1] + (1 if min_velocity % velocity[i - 1] else 0)
        min_velocity *= velocity[i - 1]
print(min_velocity)
