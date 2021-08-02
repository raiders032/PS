"""
https://www.acmicpc.net/problem/1783
1783.병든 나이트
실버4
풀이1.84ms
"""


def solve():
    if N >= 3:
        if M >= 7:
            print(M - 2)
        elif M <= 4:
            print(M)
        elif M <= 6:
            print(4)
    elif N == 2:
        result = M // 2 if M % 2 == 0 else M // 2 + 1
        print(min(result, 4))
    else:
        print(1)


N, M = map(int, input().split())
solve()
