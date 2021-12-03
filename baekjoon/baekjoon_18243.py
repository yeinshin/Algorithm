#https://www.acmicpc.net/problem/18243
#18243번-Small World Network
INF = int(1e9)
n,k = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(k):
    a,b = map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j: continue
        if graph[i][j]>6:
            print('Big World!')
            exit()
print('Small World!')
