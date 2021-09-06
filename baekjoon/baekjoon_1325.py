#https://www.acmicpc.net/problem/1325
#1325번-효율적인 해킹

from collections import deque

n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
result = list()
for _ in range(m):
    a,b = map(int,input().split())
    graph[b].append(a)

def bfs(i,visited):
    q = deque([i])
    visited[i] = 1
    while q:
        n = q.popleft()
        for a in graph[n]:
            if not visited[a]: 
                visited[a]=1
                q.append(a)
    return sum(visited[1:])

for i in range(1,n+1):
    visited = [0]*(n+1)
    result.append(bfs(i,visited))

max_value = max(result)
for i in range(n):
    if max_value==result[i]:
        print(i+1,end=' ')
