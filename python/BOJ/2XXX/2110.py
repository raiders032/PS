"""
https://www.acmicpc.net/problem/2110
2110.공유기 설치
풀이3.988ms
"""
import sys
input = sys.stdin.readline


def check(distance):
    route_count = 1
    current_route = routes[0]
    for i in range(1, N):
        if routes[i] - current_route >= distance:
            route_count += 1
            current_route = routes[i]
    return route_count >= C


N, C = map(int, input().split())
routes = sorted([int(input()) for _ in range(N)])

low = 0
high = 1000000001
while low + 1 < high:
    mid = (low + high) // 2

    route_count = 1
    current_route = routes[0]
    for i in range(1, N):
        if routes[i] - current_route >= mid:
            route_count += 1
            current_route = routes[i]

    if check(mid):
        low = mid
    else:
        high = mid

print(low)