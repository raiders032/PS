"""
https://www.acmicpc.net/problem/6064
6064.카잉 달력
실버1
중국인의나머지정리, 수학, 정수론
풀이3.
10 12 3 9
10 12 7 2
13 11 5 6
"""
test_case = int(input())

for i in range(test_case):
    M, N, X, Y = map(int, input().split())

    ans = X - 1

    for i in range(N+1):
        if ans % N == Y - 1:
            print(ans + 1)
            break
        ans += M
    else:
        print(-1)