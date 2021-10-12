#https://www.acmicpc.net/problem/16973
#16973번-직사각형 탈출(풀이참고)
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
h,w,sx,sy,fx,fy = map(int,input().split())
dx,dy = [0,0,-1,1],[-1,1,0,0]
visited = [[-1]*m for _ in range(n)]
walls = []
for i in range(n):
    for j in range(m):
        if graph[i][j]==1: walls.append((i,j))

q = deque([(sx-1,sy-1)])
visited[sx-1][sy-1]=0
while q:
    x,y = q.popleft()
    if x==fx-1 and y==fy-1:
        print(visited[x][y])
        exit()
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        check = True
        if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
            for wx,wy in walls:
                if ny+w-1>=m or nx+h-1>=n or(nx<=wx<nx+h and ny<=wy<ny+w):check = False
            if check:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))
print(-1)
    