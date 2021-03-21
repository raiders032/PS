n = int(input())
arr = list(map(int, input().split()))
cnt = 0
score = 0
for x in arr:
    if x == 0:
        cnt = 0
    else:
        cnt += 1
        score += cnt
print(score)

