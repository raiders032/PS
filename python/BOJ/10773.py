N = int(input())
arr = []

for _ in range(N):
    num = int(input())
    if num ==0:
        arr.pop()
    else:
        arr.append(num)

print(sum(arr))