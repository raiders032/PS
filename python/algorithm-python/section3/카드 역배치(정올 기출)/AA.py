arr = list(range(21))

for _ in range(10):
    l, r = map(int, input().split())
    for i in range((r-l+1)//2):
        arr[l+i], arr[r-i] = arr[r-i], arr[l+i]
arr.pop(0)
for x in arr:
    print(x, end=' ')
