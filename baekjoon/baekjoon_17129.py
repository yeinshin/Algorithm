#https://www.acmicpc.net/problem/17129
#17129번-윌리암슨수액빨이딱따구리가 정보섬에 올라온 이유
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
def bfs(x,y):
    q = deque([(x,y)])
    visited[x][y]=0
    while q:
        x,y = q.popleft()
        if graph[x][y] in (3,4,5):
            return print("TAK",visited[x][y],sep='\n')

        for nx,ny in ((x-1,y),(x+1,y),(x,y+1),(x,y-1)):
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1 and graph[nx][ny]!=1:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))
    return print('NIE')

for i in range(n):
    for j in range(m):
        if graph[i][j]==2:
            bfs(i,j)
            break