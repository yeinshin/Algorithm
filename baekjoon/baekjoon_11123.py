#https://www.acmicpc.net/problem/11123
#11123번-양 한마리... 양 두마리...
from collections import deque
for _ in range(int(input())):
    n,m = map(int,input().split())
    graph = [list(input()) for _ in range(n)]
    
    def bfs(x,y):
        q = deque([(x,y)])
        graph[x][y]='.'
        while q:
            x,y = q.popleft()
            for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                if 0<=nx<n and 0<=ny<m and graph[nx][ny]=='#':
                    q.append((nx,ny))
                    graph[nx][ny]='.'
    answer = 0    
    for i in range(n):
        for j in range(m):
            if graph[i][j]=='#':
                bfs(i,j)
                answer+=1
    print(answer)