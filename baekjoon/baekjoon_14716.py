#https://www.acmicpc.net/problem/14716
#14716번-현수막
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
def bfs(x,y):
    q = deque([(x,y)])
    while q:
        x,y = q.popleft()
        for a,b in ((1,0),(-1,0),(0,-1),(0,1),(-1,1),(-1,-1),(1,-1),(1,1)):
            nx,ny = x+a, y+b
            if 0<=nx<n and 0<=ny<m and graph[nx][ny]:
                q.append((nx,ny))
                graph[nx][ny]=0
answer = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]:
            bfs(i,j)
            answer +=1
print(answer)