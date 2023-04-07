'''
https://www.acmicpc.net/problem/2309
2309번 일곱 난쟁이
브론즈2
브루트포스 알고리즘
풀이3.76ms
'''
heights = [int(input()) for _ in range(9)]
heights.sort()
total = sum(heights)
for i in range(8):
    for j in range(i+1, 9):
        if total - heights[i] - heights[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(heights[k])
            exit()
