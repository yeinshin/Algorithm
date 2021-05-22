#2589번-보물섬
#각 칸은 육지(L)나 바다(W)로 표시
#이동은 상하좌우로 이웃한 육지로만 가능하며, 한 칸 이동하는데 한 시간이 걸린다. -> 비용이 같다? 즉 BFS를 써라
#보물은 서로 간에 최단 거리로 이동하는데 있어 가장 긴 시간이 걸리는 육지 두 곳에 나뉘어 묻혀있다. -> 이말도 최소 비용을 구해야하는 BFS를 쓰라는 힌트
#육지를 나타내는 두 곳 사이를 최단 거리로 이동하려면 같은 곳을 두 번 이상 지나가거나, 멀리 돌아가서는 안 된다. -> 방문 체크를 해줘야함

from collections import deque

#m:세로, n:가로
n,m = map(int,input().split())
island = [list(input()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    
    visited = [[-1]*m for _ in range(n)]
    max_distance = 0

    q = deque()
    q.append((x,y))
    
    visited[x][y]=0


    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==-1 and island[nx][ny]=='L':
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx,ny))
    
    for i in range(n):
        max_distance = max(max_distance,max(visited[i]))
    
    return max_distance
                    
max_distance = 0
for i in range(n):
    for j in range(m):
        if island[i][j]=='L':
            max_distance = max(max_distance,bfs(i,j))

print(max_distance)