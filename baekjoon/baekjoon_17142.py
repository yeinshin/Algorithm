#https://www.acmicpc.net/problem/17142
#17142번-연구소 3
from itertools import combinations
from collections import deque
n,m = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
virus = []
walls = 0
q = deque()
for i in range(n):
    for j in range(n):
        if graph[i][j]==2: virus.append((i,j))
        elif graph[i][j]==1: walls+=1

def bfs(n,walls):
    while q:
        x,y,d,b = q.popleft()
        for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0<=nx<n and 0<=ny<n and visited[nx][ny]==-1:
                if graph[nx][ny]==2:
                    visited[nx][ny]=0
                    check[nx][ny]=0
                    q.append((nx,ny,d,b+1))
                elif graph[nx][ny]==0:
                    if b!=0:
                        visited[nx][ny]=d+b
                    else:visited[nx][ny]=visited[x][y]+1
                    check[nx][ny]=0
                    q.append((nx,ny,visited[nx][ny],0))
    cnt = 0
    sec = -1
    for i in range(n):
        cnt+=sum(check[i])
        sec = max(sec,max(visited[i]))
    return sec if cnt==walls else INF


INF = int(1e9)
ans = INF
for comb in combinations(virus,m):
    visited = [[-1]*n for _ in range(n)]
    check = [[1]*n for _ in range(n)]
    for x,y in comb:
        q.append((x,y,0,0))
        visited[x][y]=0
        check[x][y]=0
    ans=min(ans,bfs(n,walls))

print(ans if ans!=INF else -1)


  