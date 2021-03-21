"""
6603번 로또 실버2
백트래킹, 조합론, 재귀 
"""
arr = []
selected = []


def dfs(cnt, idx):
    if cnt == 6:
        for x in selected:
            print(x, end=' ')
        print()
        return
    for i in range(idx, arr[0]+1):
        selected.append(arr[i])
        dfs(cnt+1, i+1)
        selected.pop()


while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    dfs(0, 1)
    print()
