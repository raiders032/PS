"""
https://www.acmicpc.net/problem/1712
1712.손익분기점
브론즈4
풀이1.72ms
"""
A, B, C = map(int, input().split())

if B >= C:
    print(-1)
else:
    print(A // (C - B) + 1)
