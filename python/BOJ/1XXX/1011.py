"""
https://www.acmicpc.net/problem/1011
1011.Fly me to the Alpha Centauri
실버1
풀이1.
"""
arr = [0, 1, 2, 3]
test_case = int(input())

for i in range(test_case):
    x, y = map(int, input().split())

    if y - x <= 3:
        print(arr[y - x])
        continue

    m = 1
    ans = 0
    while x < y:
        x += m
        y -= m
        m += 1
        ans += 2

    print(ans - 1 if (y - x) % 2 == 0 else ans)
