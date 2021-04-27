#2부<문제>2번-미래 도시
#플로이드 워셜 알고리즘으로 문제 해결

INF = int(1e9)
#n:전체 회사의 개수, m:경로의 개수
n,m=map(int,input().split())

graph=[[INF]*(n+1) for _ in range(n+1)]

for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

#x:물건을 판매 할 곳, k:소개팅 상대의 회사
x,k=map(int,input().split())

for c in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][c]+graph[c][b])

distance= graph[1][k]+graph[k][x]

#도달할 수 없는 경우, -1을 출력
if distance==INF:
    print('-1')
#도달할 수 있다면, 최단 거리를 출력
else:
    print(distance)
