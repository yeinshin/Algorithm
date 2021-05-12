#1260번-DFS와 BFS

from collections import deque

n,m,v = map(int,input().split())
node = [[] for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)

# print(node,end='\n')

def dfs(start,visited,node,n):
    visited[start]=True
    print(start,end=' ')
    node[start].sort()
    for i in node[start]:
        if visited[i]==False:
            dfs(i,visited,node,n)

def bfs(start,node,n):
    visited = [False]*(n+1)
    q=deque([start])
    visited[start]=True
    while q:
        now = q.popleft()
        print(now, end = ' ')
        node[now].sort()
        for n in node[now]:
            if visited[n]==False:
                visited[n]=True
                q.append(n)

dfs(v,visited,node,n)
print()
bfs(v,node,n)