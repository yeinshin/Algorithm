#https://www.acmicpc.net/problem/15558
#15558번-점프 게임
from collections import deque
n,k = map(int,input().split())
graph = [list(map(int,input())) for _ in range(2)]
q = deque([(0,0,0)])
while q:
    x,y,cnt= q.popleft()
    for nx,ny in ((x,y+1),(x,y-1),(not x,y+k)):
        if cnt<ny<n and graph[nx][ny]:
            graph[nx][ny]=0
            q.append((nx,ny,cnt+1))
        elif ny>=n:
            print(1)
            exit()
print(0)