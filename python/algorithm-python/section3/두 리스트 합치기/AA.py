N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
C = []
idx_a = 0
idx_b = 0
for i in range(N+M):
    if A[idx_a] < B[idx_b]:
        C.append(A[idx_a])
        idx_a += 1
    else:
        C.append(B[idx_b])
        idx_b += 1

    if idx_a == N:
        C += B[idx_b:]
        break
    elif idx_b == M:
        C += A[idx_a:]
        break
for x in C:
    print(x, end=" ")
