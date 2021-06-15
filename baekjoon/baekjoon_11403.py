#https://www.acmicpc.net/problem/11403
#11403번-경로 찾기
#i번째 줄의 j번째 숫자가 1인 경우에는 i에서 j로 가는 간선이 존재한다는 뜻이고, 0인 경우는 없다는 뜻이다. i번째 줄의 i번째 숫자는 항상 0이다.

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
INF = int(1e9)

for i in range(n):
    for j in range(n):
        if graph[i][j]==0:
            graph[i][j]=INF

for k in range(n):
    for a in range(n):
        for b in range(n):
            graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

for x in range(n):
    for y in range(n):
        if graph[x][y]==INF:
            print(0,end=' ')
        else:
            print(1,end = ' ')
    print()
