#https://www.acmicpc.net/problem/1389
#1389번-케빈 베이컨의 6단계 법칙

INF = int(1e9)
#n:유저의 수, m:친구 관계의 수
n,m = map(int,input().split())

graph = [[INF]*n for _ in range(n)]

for a in range(n):
    graph[a-1][a-1]=0

for _ in range(m):
    a,b = map(int,input().split())
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

for i in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b],graph[a][i]+graph[i][b])
result = list()
for i in range(n):
    result.append(sum(graph[i]))

print(result.index(min(result))+1)