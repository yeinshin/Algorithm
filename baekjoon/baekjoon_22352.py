#https://www.acmicpc.net/problem/22352
#22352번-항체 인식
from collections import deque

n,m = map(int,input().split())
ago = [list(map(int,input().split())) for _ in range(n)]
after = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx,dy = [-1,1,0,0],[0,0,-1,1]
def bfs(x,y,now,change):
    q=deque([(x,y)])
    visited[x][y]=True
    ago[x][y]=change
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = dx[i]+x
            ny = dy[i]+y
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and ago[nx][ny]==now:
                ago[nx][ny]=change
                visited[nx][ny]=True
                q.append((nx,ny))

check = False
for i in range(n):
    for j in range(m):
        if ago[i][j]!=after[i][j] and not visited[i][j]:
            bfs(i,j,ago[i][j],after[i][j])
            check=True
            break
    if check: break
    
print( 'YES' if ago == after else 'NO')