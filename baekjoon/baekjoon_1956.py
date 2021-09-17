#https://www.acmicpc.net/problem/1956
#1956번-운동
INF = int(1e9)
n,m = map(int,input().split())
dist = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int,input().split())
    dist[a][b]=c
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
result = int(1e9)
for i in range(1,n+1):
    result = min(result,dist[i][i])
print(-1 if result==INF else result)