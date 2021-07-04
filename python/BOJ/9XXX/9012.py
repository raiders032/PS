"""
https://www.acmicpc.net/problem/9012
9012.괄호
실버4
풀이1.88ms
"""
for _ in range(int(input())):
    count = 0
    for ch in list(input()):
        if ch == '(':
            count += 1
        else:
            count -= 1
            if count < 0:
                break

    if count:
        print("NO")
    else:
        print("YES")