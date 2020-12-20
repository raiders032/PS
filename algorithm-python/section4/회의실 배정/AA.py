N = int(input())
arr = []
end = 0
cnt = 0
for i in range(N):
    S, E = map(int, input().split())
    arr.append((S, E))
arr.sort(key=lambda e: (e[1], e[0]))

for s, e in arr:
    if end <= s:
        end = e
        cnt += 1
print(cnt)
