#https://www.acmicpc.net/problem/6118
#6118번-숨바꼭질
from collections import deque
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
visited = [-1]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

q = deque([1])
visited[1]=0
while q:
    x = q.popleft()
    for i in graph[x]:
        if visited[i]==-1:
            visited[i]=visited[x]+1
            q.append(i)
ans = max(visited)
print(visited.index(ans),ans,visited.count(ans))