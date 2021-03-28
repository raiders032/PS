'''
https://www.acmicpc.net/problem/2309
2309번 일곱 난쟁이
브론즈2
브루트포스 알고리즘
풀이2.68ms
'''
import sys

input = sys.stdin.readline
heights = []
sum = 0
is_found = False

for _ in range(9):
    height = int(input())
    sum += height
    heights.append(height)

heights.sort()

for i in range(8):
    if is_found:
        break

    for j in range(i + 1, 9):
        if heights[i] + heights[j] == sum - 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(heights[k])
            is_found = True
            break
