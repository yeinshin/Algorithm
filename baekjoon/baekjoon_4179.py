#https://www.acmicpc.net/problem/4179
#4179번-불!(풀이참고)
from collections import deque
n,m = map(int,input().split())
miro = [input() for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx,dy=[-1,1,0,0],[0,0,-1,1]

q = deque()
for i in range(n):
    for j in range(m):
        if miro[i][j]=='J':
            q.append((i,j,'J'))
            visited[i][j]=1
        elif miro[i][j]=='F':
            q.appendleft((i,j,'F'))
            visited[i][j]=1

while q:
    x,y,state = q.popleft()
    if state=='J' and (x==n-1 or x==0 or y==m-1 or y==0):
        print(visited[x][y])
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and miro[nx][ny]!='#':
            visited[nx][ny]=visited[x][y]+1
            q.append((nx,ny,state))
else: print("IMPOSSIBLE")