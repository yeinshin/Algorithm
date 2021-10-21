#https://www.acmicpc.net/problem/2665
#2665번-미로만들기(풀이참고/1261번-알고스팟 참고)
from collections import deque
n = int(input())
graph = [list(map(int,input())) for _ in range(n)]
visited = [[-1]*n for _ in range(n)]
dx,dy = [0,0,-1,1],[-1,1,0,0]
q = deque([(0,0)])
visited[0][0]=0
while q:
    x,y = q.popleft()
    for i in range(4):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1:
            if graph[nx][ny]==0:
                visited[nx][ny]=visited[x][y]+1
                q.append((nx,ny))
            else: 
                visited[nx][ny]=visited[x][y]
                q.appendleft((nx,ny))
print(visited[n-1][n-1])