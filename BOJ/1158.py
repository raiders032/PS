from collections import deque
N, K = map(int, input().split())
q = [x for x in range(1, N+1)]
idx = 0
res = '<'

while q:
    idx += K-1
    if idx >= len(q):
        idx = idx % len(q)
    res += str(q.pop(idx))
    if q:
        res += ', '
res += '>'
print(res)
