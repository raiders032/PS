"""
https://www.acmicpc.net/problem/1022
1022.소용돌이 예쁘게 출력하기
풀이1.
"""
position = list(map(int, input().split()))
n = max(map(abs, position)) * 2 + 1

print(n)
