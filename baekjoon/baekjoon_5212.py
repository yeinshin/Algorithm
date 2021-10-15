#https://www.acmicpc.net/problem/5212
#5212번-지구 온난화
from copy import deepcopy
n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]
test = deepcopy(graph)
dx,dy=[0,0,-1,1],[1,-1,0,0]

for i in range(n):
    for j in range(m):
        if graph[i][j]=='X': 
            cnt = 0
            for z in range(4):
                nx,ny = dx[z]+i,dy[z]+j
                if 0<=nx<n and 0<=ny<m:
                    if graph[nx][ny]=='.':cnt+=1
                else: cnt+=1
            if cnt>=3: test[i][j]='.'

start_y, end_y = 0, 0
for i in range(n):
    if 'X' in test[i]:
        start_y = i
        break
for i in range(n-1, -1,-1):
    if 'X' in test[i]:       
        end_y = i
        break

tmp = []
for j in range(m):
    for i in range(start_y, end_y + 1):
        if 'X' == test[i][j]:
            tmp.append(j)
            break

for y in range(start_y, end_y+1):
    print("".join(test[y][tmp[0]:tmp[-1]+1]))