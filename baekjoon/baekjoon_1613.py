#https://www.acmicpc.net/problem/1613
#1613번-역사
INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b =map(int,input().split())
    graph[a][b]=1
s=int(input())
check = list()
for _ in range(s):
    a,b = map(int,input().split())
    check.append((a,b))
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k]==1 and graph[k][j]==1: graph[i][j]=1

for a,b in check:
    if graph[a][b]==1:print(-1)
    elif graph[b][a]==1:print(1)
    else:print(0)