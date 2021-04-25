"""
https://leetcode.com/problems/number-of-islands/
200. Number of Islands
Medium
DFS
풀이1.144ms
"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        answer = 0
        m = len(grid)
        n = len(grid[0])
        visited = [[False] * n for _ in range(m)]
        dx = [-1, 0, 1, 0]
        dy = [0, 1, 0, -1]

        def visit(x, y):
            visited[x][y] = True
            for direction in range(4):
                nx = x + dx[direction]
                ny = y + dy[direction]
                if nx < 0 or nx >= m or ny < 0 or ny >= n:
                    continue
                if visited[nx][ny] or grid[nx][ny] == "0":
                    continue
                visit(nx, ny)

        for i in range(m):
            for j in range(n):
                if visited[i][j] or grid[i][j] == "0":
                    continue
                visit(i, j)
                answer += 1

        return answer