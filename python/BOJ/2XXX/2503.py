"""
https://www.acmicpc.net/problem/2503
2503.숫자 야구
실버5
풀이1.
"""
import sys

input = sys.stdin.readline
ans = set([str(i) for i in range(111, 1000)])

for _ in range(int(input())):
    predicate, s, b = map(int, input().split())
    predicate = str(predicate)
    for num in list(ans):
        s_count = 0
        b_count = 0
        for i in range(3):
            if predicate[i] == num[i]:
                s_count += 1
                continue
            if (predicate[i] == num[(i + 1) % 3] and num[(i + 1) % 3] != predicate[(i + 1) % 3]) or (predicate[i] == num[(i + 2) % 3] and predicate[(i + 2) % 3] != num[(i + 2) % 3]):
                b_count += 1
                continue
        if s != s_count or b != b_count:
            ans.remove(num)
print(len(ans))
