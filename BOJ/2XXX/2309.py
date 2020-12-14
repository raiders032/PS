'''
2309번 일곱 난쟁이 브론즈2
브루트포스 알고리즘
'''
sum = 0
arr = []
find = False
for _ in range(9):
    num = int(input())
    arr.append(num)
    sum += num

arr.sort()

for i in range(8):
    if find:
        break
    for j in range(i+1, 9):
        if sum - arr[i] - arr[j] == 100:
            for k in range(9):
                if k == i or k == j:
                    continue
                print(arr[k])
            find = True
            break
