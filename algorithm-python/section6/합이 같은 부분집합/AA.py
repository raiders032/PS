n = int(input())
arr = list(map(int, input().split()))
visited = [False] * n


def dfs(idx):
    if idx >= n:
        sum1 = 0
        sum2 = 0
        for i in range(n):
            if visited[i]:
                sum1 += arr[i]
            else:
                sum2 += arr[i]
        if sum1 == sum2:
            return True
        else:
            return False
    visited[idx] = True
    if dfs(idx+1):
        return True
    visited[idx] = False
    if dfs(idx+1):
        return True
    return False


print("YES" if dfs(0) else "NO")
