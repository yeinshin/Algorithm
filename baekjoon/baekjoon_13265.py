#https://www.acmicpc.net/problem/13265
#13265번-색칠하기

def dfs(now,graph,color,visited):
    for i in graph[now]:
        if visited[i] and color[i]==color[now]:
            return False
        if not visited[i]:
            color[i]=not color[now]
            visited[i]=True
            dfs(i,graph,color,visited)
    return True

for _ in range(int(input())):
    n,m = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    color = [0]*(n+1)
    visited = [False]*(n+1)
    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(n):
        if graph[i] and not visited[i]:
            visited[i]=True
            if not dfs(i,graph,color,visited):
                print('impossible')
                break
    else: print('possible')