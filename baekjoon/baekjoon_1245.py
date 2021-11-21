#https://www.acmicpc.net/problem/1245
#1245번-농장 관리
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[0]*m for _ in range(n)]

def bfs(x,y,n,m,now):
    q = deque([(x,y)])
    visit = [[0]*m for _ in range(n)]
    visited[x][y],visit[x][y]=1,1

    while q:
        x,y = q.popleft()
        for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1),(x+1,y+1),(x-1,y+1),(x-1,y-1),(x+1,y-1)):
            if 0<=nx<n and 0<=ny<m:
                if visit[nx][ny]==0 and graph[nx][ny]==now:
                    visited[nx][ny]=1
                    visit[nx][ny]=1
                    q.append((nx,ny))
                elif graph[nx][ny]>now: return False
    return True
    
ans = 0
for i in range(n):
    for j in range(m):
        if graph[i][j]>0 and visited[i][j]==0:
            if bfs(i,j,n,m,graph[i][j]):ans+=1
print(ans)
