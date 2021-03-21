N = int(input())
arr = []
for i in range(N):
    h, w = map(int, input().split())
    arr.append((h, w))
arr.sort(reverse=True)
cnt = 0
maxW = 0
for h, w in arr:
    if w > maxW:
        maxW = w
        cnt += 1
print(cnt)
