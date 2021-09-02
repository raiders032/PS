"""
https://www.acmicpc.net/problem/10025
10025.게으른 백곰
실버4
풀이1.332ms
"""
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
left = right = 0
ice = [tuple(map(int, input().split())) for _ in range(N)]
ice.sort(key=lambda x: x[1])
answer = total = ice[0][0]

while True:
    if ice[right][1] - ice[left][1] <= 2 * K:
        answer = max(answer, total)
        right += 1
        if right >= N:
            break
        total += ice[right][0]
    else:
        total -= ice[left][0]
        left += 1

print(answer)
