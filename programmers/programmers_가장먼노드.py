#https://programmers.co.kr/learn/courses/30/lessons/49189
#프로그래머스-가장 먼 노드

from collections import deque
def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    visited = [0]*(n+1)
    
    for s,e in edge:
        graph[s].append(e)
        graph[e].append(s)
    
    def bfs():
        q = deque([1])
        visited[1]=1
        
        while q:
            start = q.popleft()
            
            for node in graph[start]:
                if visited[node]==0:
                    visited[node]= visited[start]+1
                    q.append(node)
                    
    bfs()

    return visited.count(max(visited))