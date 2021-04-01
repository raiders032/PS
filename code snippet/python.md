sys.setrecursionlimit(100000)



## 정렬

```python
array = list() 
array.sort()
```



## 2차원 배열 4방향

```python
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for dir in range(4):
  nx = x + dx[dir]
  ny = y + dy[dir]
  if nx < 0 or nx >= N or ny < 0 or ny >= N:
    continue
```

# 스택

```python
# stack 선언
stack = []
# stack push
stack.append(0)
# stack pop
stack.pop()
# stack Top
stack[-1]
```

# 큐

```python
from collections import deque
que = deque()
que.popleft()
que.append(next_vertex)
```



### 큐 최소 거리 구하기

```python
from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(start_x, start_y):
    visited = [[0] * length for _ in range(length)]
    queue = deque([(start_x, start_y)])
    visited[start_x][start_y] = 1
    while queue:
        x, y = queue.popleft()

        if x == end_x and y == end_y:
            return visited[x][y] - 1

        for dir in range(4):
            nx = x + dx[dir]
            ny = y + dy[dir]
            if nx < 0 or nx >= length or ny < 0 or ny >= length:
                continue

            if visited[nx][ny]:
                continue

            visited[nx][ny] = visited[x][y] + 1
            queue.append((nx, ny))
```



## 최대 최소

```python
min = sys.maxsize
max = -sys.maxsize
```

