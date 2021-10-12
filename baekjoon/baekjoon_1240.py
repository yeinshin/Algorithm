#https://www.acmicpc.net/problem/1240
#1240번-노드사이의 거리
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dfs(start,end):
    if start == end:
        print(visited[end])
        return
    for x,y in graph[start]:
        if visited[x]==-1:
            visited[x]=visited[start]+y
            dfs(x,end)

for _ in range(m):
    i,j = map(int,input().split())
    visited = [-1]*(n+1)
    visited[i]=0
    dfs(i,j)
