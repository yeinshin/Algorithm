#https://www.acmicpc.net/problem/17836
#17836번-공주님을 구해라!
from collections import deque
import sys
input = sys.stdin.readline

n,m,t = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[-1]*m for _ in range(n)]
item = 10001
def bfs():
    global item
    q = deque([(0,0)])
    visited[0][0] = 0
    while q:
        x,y = q.popleft()
        if graph[x][y]==2:
            item = (n-1-x)+(m-1-y) + visited[x][y]
        if x==n-1 and y==m-1:
            return min(item,visited[x][y])
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
             
            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1:
                if graph[nx][ny]!=1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx,ny))
    return item

result = bfs()
print('Fail' if result>t else result)

