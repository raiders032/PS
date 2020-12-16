'''
9095번 1, 2, 3 더하기 실버3
브루트포스, 다이나믹 프로그래밍
브루트포스 풀이
'''
N = 0
tc = int(input())
cnt = 0


def dfs(sum):
    global cnt
    if sum >= N:
        if sum == N:
            cnt += 1
    else:
        for i in range(1, 4):
            dfs(sum + i)


for _ in range(tc):
    cnt = 0
    N = int(input())
    dfs(0)
    print(cnt)
