"""
https://www.acmicpc.net/problem/1449
1449.수리공 항승
실버3
풀이1.80ms
"""
N, L = map(int, input().split())
positions = list(map(int, input().split()))
positions.sort()
count = 0
end = 0

for position in positions:
    if position < end:
        continue

    end = position + L
    count += 1
print(count)

"""
2 1
1 2
2
---
2 2
1 2
1
"""