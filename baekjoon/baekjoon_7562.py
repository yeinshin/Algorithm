#https://www.acmicpc.net/problem/7562
#7562번-나이트의 이동
from collections import deque
for _ in range(int(input())):
    n = int(input())
    x,y = map(int,input().split())
    d = list(map(int,input().split()))
    dx,dy = [-1,-1,-2,-2,1,1,2,2],[-2,2,1,-1,2,-2,1,-1]
    visited = [[-1]*n for _ in range(n)]

    q = deque([(x,y)])
    visited[x][y]=0
    while q:
        x,y = q.popleft()
        if x==d[0] and y==d[1]:
            print(visited[x][y])
            break
        for i in range(8):
            nx,ny = dx[i]+x,dy[i]+y
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1:
                q.append((nx,ny))
                visited[nx][ny]=visited[x][y]+1