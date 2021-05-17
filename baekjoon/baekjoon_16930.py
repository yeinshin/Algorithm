#16930번-달리기
#체육관의 각 칸은 빈 칸 또는 벽이고, 빈 칸은 '.', 벽은 '#'으로 주어진다.
#(x1, y1)에서 (x2, y2)로 이동하는 최소 시간을 출력한다. 이동할 수 없는 경우에는 -1을 출력한다.
#rstrip():공백 문자 제거

import sys
from collections import deque

input = sys.stdin.readline

#체육관의 크기 N과 M, 1초에 이동할 수 있는 칸의 최대 개수 K
n,m,k = map(int,input().split())
graph = [[s for s in input().rstrip()] for _ in range(n)]

#시작점 (x1, y1)과 도착점 (x2, y2)
x1,y1,x2,y2 = map(int,input().split())

#방문, 비용 체크 리스트
visited = [[-1]*m for _ in range(n)]

#상,하,좌,우
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs(i,j):
    q = deque()
    q.append((i,j))

    visited[i][j]=0

    while q:
        x,y = q.popleft()

        for i in range(4):
            for j in range(1,k+1):
                nx = x+dx[i]*j
                ny = y+dy[i]*j
                
                if nx<0 or ny<0 or nx>=n or ny>=m or graph[nx][ny]=='#':
                    break

                if visited[nx][ny]==-1:
                    visited[nx][ny]=visited[x][y] + 1
                    q.append((nx,ny))

                    if nx==(x2-1) and ny==(y2-1):
                        return visited[nx][ny]

                # elif visited[nx][ny]<visited[x][y]+1 : break 도 됨
                elif visited[nx][ny]==visited[x][y]+1: continue #일단 쭉 가본다
                else: break # 더 큰길은 탐색하지 않는다

                
    #이동할 수 없는 경우에는 -1을 출력한다.
    return -1


result = bfs(x1-1,y1-1)
print(result)

# print(*visited,sep='\n')