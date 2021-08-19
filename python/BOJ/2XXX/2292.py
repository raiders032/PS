"""
https://www.acmicpc.net/problem/2292
2292.벌집
브론즈2
풀이1.68ms
"""
N = int(input()) - 1
ans = 1

while N > 0:
    N -= 6 * ans
    ans += 1

print(ans)