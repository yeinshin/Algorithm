#https://www.acmicpc.net/problem/5427
#5427번-불

from collections import deque
import sys
input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
def bfs():
    global q, f
    while q:
        temp = deque()
        while q:
            x, y = q.popleft()
            if (x == h - 1 or y == w - 1 or x == 0 or y == 0) and s[x][y] != "*": return s[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and s[nx][ny] == "." and s[x][y] != "*":
                    s[nx][ny] = s[x][y] + 1
                    temp.append([nx, ny])
        q = temp
        temp = deque()
        while f:
            x, y = f.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w and visit[nx][ny] == 0 and s[nx][ny] != "#":
                    s[nx][ny] = "*"
                    visit[nx][ny] = 1
                    temp.append([nx, ny])
        f = temp
        
t = int(input())
for i in range(t):
    w, h = map(int, input().split())
    s, f, q = [], deque(), deque()
    visit = [[0] * w for i in range(h)]
    for j in range(h):
        a = list(input().strip())
        s.append(a)
        for k in range(w):
            if a[k] == "@":
                s[j][k] = 0
                q.append([j, k])
            elif a[k] == "*":
                f.append([j, k])
                visit[j][k] = 1
    result = bfs()
    print(result + 1 if result != None else "IMPOSSIBLE")



# from collections import deque
# for _ in range(int(input())):
#     m,n = map(int,input().split())
#     graph = [input() for _ in range(n)]
#     visited = [[-1]*m for _ in range(n)]
#     check = [[0]*m for _ in range(n)]

#     q = deque()
#     for i in range(n):
#         for j in range(m):
#             if graph[i][j]=='@': 
#                 q.append((i,j,'@'))
#                 visited[i][j]=0
#             elif graph[i][j]=='*': 
#                 q.appendleft((i,j,'*'))
#                 check[i][j]=1
#                 visited[i][j]=0
#     while q:
#         x,y,s = q.popleft()
#         if (x in (0,n-1) or y in (0,m-1)) and graph[x][y]=='.' and s=='@':
#             print(visited[x][y]+1)
#             break
#         for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
#             if 0<=nx<n and 0<=ny<m and check[nx][ny]==0:
#                 if s=='@' and graph[nx][ny]=='.' and visited[nx][ny]==-1:
#                     visited[nx][ny]=visited[x][y]+1
#                     check[x][y]=1
#                     q.append((nx,ny,s))
#                 elif s=='*' and graph[nx][ny]!='#':
#                     check[nx][ny]=1
#                     visited[nx][ny]=visited[x][y]+1
#                     q.append((nx,ny,s))
#     else: print('IMPOSSIBLE')