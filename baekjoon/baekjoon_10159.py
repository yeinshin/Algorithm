#https://www.acmicpc.net/problem/10159
#10159번-저울
n = int(input())
m = int(input())
INF = int(1e9)
graph = [[INF]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b]=1
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][k]+graph[k][b]==2: graph[a][b]=1
result = [n-1]*n
for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==1:
            result[i-1]-=1 # i가 j보다 작은 횟수
            result[j-1]-=1 # j가 i보다 큰 횟수
print(*result,sep='\n')