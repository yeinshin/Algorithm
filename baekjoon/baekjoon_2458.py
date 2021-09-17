#https://www.acmicpc.net/problem/2458
#2468번-키 순서
INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if graph[i][k]+graph[k][j]==2: graph[i][j]=1 #i와 j를 비교할 수 있다는 것, i는 j보다 작다는 것을 나타냄

cnt = [0]*(n+1)
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==1:
            cnt[i]+=1
            cnt[j]+=1
print(cnt.cnt(n-1))
