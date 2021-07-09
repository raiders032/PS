"""
https://www.acmicpc.net/problem/1002
1002.터렛
실버4
풀이1.84ms
"""
test_case = int(input())
for i in range(test_case):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dist = (x1 - x2) ** 2 + (y1 - y2) ** 2

    if dist == 0 and r1 == r2:
        print(-1)
    elif dist == 0:
        print(0)
    elif dist > (r1 + r2) ** 2:
        print(0)
    elif dist < (2 * max(r1, r2) - r1 - r2) ** 2:
        print(0)
    elif dist == (r1 + r2) ** 2:
        print(1)
    elif dist == (2 * max(r1, r2) - r1 - r2) ** 2:
        print(1)
    elif dist < (r1 + r2) ** 2:
        print(2)