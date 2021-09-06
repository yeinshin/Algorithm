#https://www.acmicpc.net/problem/1926
#1926번-그림
from collections import deque

n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
cnt = 0
result = 0

def bfs(x,y):
    area = 1
    q=deque([(x,y)])
    visited[x][y]=True
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and graph[nx][ny]==1:
                visited[nx][ny]=True
                q.append((nx,ny))
                area+=1
    return area

for i in range(n):
    for j in range(m):
        if not visited[i][j] and graph[i][j]==1:
            result = max(result,bfs(i,j))
            cnt+=1
print(cnt,result,sep='\n')