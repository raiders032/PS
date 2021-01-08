"""
14501번 퇴사 실버4
브루트포스, 다이나믹프로그래밍
브루트포스 풀이
"""
import sys

N = int(sys.stdin.readline())
T = [0]
P = [0]
ans = 0


def dfs(day, pay):
    global ans
    if day > N:
        ans = max(ans, pay)
        return
    if day + T[day] <= N + 1:
        dfs(day + T[day], pay + P[day])
    dfs(day + 1, pay)


for i in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)
dfs(1, 0)
print(ans)
