#https://www.acmicpc.net/problem/2617
#2617번-구슬 찾기(풀이참고)
INF = int(1e9)
n,m = map(int,input().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF: print('x',end=' ')
        else: print(graph[i][j],end=' ')
    print()
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][k]==1 and graph[k][b]==1 : graph[a][b]=1

cnt = [0]*(n+1)
result = 0
for i in range(1,n+1):
    h,w = 0,0
    for j in range(1,n+1):
        if i!=j:
            if graph[i][j]==1: h+=1
            elif graph[j][i]==1: w+=1
    if h>n//2 or w>n//2: result+=1
print(result)