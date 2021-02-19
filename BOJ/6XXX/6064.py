"""
6064.카잉 달력
실버1
중국인의나머지정리, 수학, 정수론
풀이1 368ms
"""

tc = int(input())

for _ in range(tc):
    M, N, x, y = map(int, input().split())
    find = False
    if M > N:
        M, N = N, M
        x, y = y, x
    cur_y = x
    year = x
    while True:
        if cur_y == y:
            find = True
            break
        cur_y = cur_y + M if cur_y + M <= N else (cur_y + M) % N
        year += M
        if cur_y == x:
            find = False
            break
    if find:
        print(year)
    else:
        print(-1)
