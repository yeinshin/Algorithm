#17086번-아기 상어 2

from collections import deque
import sys

input = sys.stdin.readline

#NxM
n,m = map(int,input().split())

graph = [[int(m) for m in input().split()] for _ in range(n)]

def bfs(i,j):

    visited = [[-1]*m for _ in range(n)]
    q = deque()
    q.append((i,j))
    visited[i][j]=0

    while q:
        x,y = q.popleft()

        # 상, 하, 좌, 우, ↖, ↙, ↘, ↗
        #nx[0]:x좌표
        #nx[1]:y좌표
        for nx in ((x-1,y),(x+1,y),(x,y-1),(x,y+1),(x-1,y-1),(x+1,y-1),(x+1,y+1),(x-1,y+1)):
            if nx[0]>=0 and nx[1]>=0 and nx[0]<n and nx[1]<m and visited[nx[0]][nx[1]]==-1:
                visited[nx[0]][nx[1]] = visited[x][y]+1
                q.append((nx[0],nx[1]))

                if graph[nx[0]][nx[1]]==1:
                    return visited[nx[0]][nx[1]]

max_value = 0

for i in range(n):
    for j in range(m):
        if graph[i][j]==0:
            max_value=max(max_value,bfs(i,j))

print(max_value)