# 기본

## sys

```python
import sys

# 재귀 제한 설정
sys.setrecursionlimit(10 ** 6)

# 최대 최소 값
min = sys.maxsize
max = -sys.maxsize

# 빠른 입출력 및 사용
input = sys.stdin.readline
input()
```

# 자료구조

## 집합

```python
plugs = set()
# 원소 1 제거 존재하지 않으면 KeyError 발생
plugs.remove(1)

# 원소 1이 존재하면 제거
plugs.discard(1)

# 원소 2 추가
plugs.add(2)

# 임의 원소 제거 및 반환 set에 원소가 없으면 KeyError 발생
plugs.pop()
```



## 스택

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



## 큐

```python
from collections import deque
que = deque()
que.popleft()
que.append(next_vertex)
```



## 최소 힙

```python
import heapq

min_heap = []
heapq.heappush(min_heap, item)
heapq.heappop(min_heap)
```



# 알고리즘



## 최대 최소

```python

```



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



## 큐 최소 거리 구하기

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



## 자리수 구하기

```python
import math

def digit_length(n):
    return int(math.log10(n)) + 1 if n else 0
```

```python
def digit_length(n):
    ans = 0

    while n:
        n //= 10
        ans += 1

    return ans
```



## 아이템 개수 계산하기

```python
from collections import defaultdict

count = defaultdict(int)
count['a'] += 1
count['b'] += 1
count['b'] += 1

print(count)
defaultdict(<class 'int'>, {'a': 1, 'b': 2})
```

```python
from collections import Counter

a = [1, 2, 3, 4, 5, 5, 5, 6, 6]
b = Counter(a)

print(b)
Counter({5: 3, 6: 2, 1: 1, 2: 1, 3: 1, 4: 1})
```
