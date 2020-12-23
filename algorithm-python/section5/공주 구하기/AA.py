import collections
cnt = 0
N, K = map(int, input().split())
dq = collections.deque(range(1, N+1))

while len(dq) > 1:
    for i in range(K-1):
        dq.append(dq.popleft())
    dq.popleft()
print(dq[-1])
