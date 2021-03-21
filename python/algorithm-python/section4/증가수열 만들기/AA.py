from collections import deque
N = int(input())
dq = deque(map(int, input().split()))
cur = 0
while dq:
    if cur < dq[0] and cur < dq[-1]:
        if dq[0] < dq[-1]:
            cur = dq.popleft()
            print('L', end='')
        else:
            cur = dq.pop()
            print('R', end='')
    elif cur < dq[-1]:
        cur = dq.pop()
        print('R', end='')
    elif cur < dq[0]:
        cur = dq.popleft()
        print('L', end='')
    else:
        break
