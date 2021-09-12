#https://www.acmicpc.net/problem/16173
#16173번-점프왕 쩰리

from collections import deque

n = int(input())
graph = [list(map(int,input().split())) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
q = deque([(0,0)])
visited[0][0]=True
while q:
    x,y = q.popleft()
    if x==n-1 and y==n-1: break
    for nx,ny in ((x+graph[x][y],y),(x,y+graph[x][y])):
        if 0<=nx<n and 0<=ny<n and graph[nx][ny]!=0 and not visited[nx][ny]:
            visited[nx][ny]=True
            q.append((nx,ny))

print('HaruHaru' if visited[n-1][n-1] else 'Hing')




