"""
네트워크
https://programmers.co.kr/learn/courses/30/lessons/43162
너비우선탐색
풀이2
"""
from collections import deque

def solution(n, computers):
    def visit(vertex):
        que = deque([vertex])
        visited[vertex] = True
        while que:
            vertex = que.popleft()
            print(vertex)
            for next_vertex in range(n):
                if visited[next_vertex] or not computers[vertex][next_vertex]:
                    continue
                visited[next_vertex]  = True
                que.append(next_vertex)
        
    visited = [False] * n
    num_network = 0    
    for vertex in range(n):
        if visited[vertex]:
            continue
        visit(vertex)
        num_network += 1
    
    return num_network
