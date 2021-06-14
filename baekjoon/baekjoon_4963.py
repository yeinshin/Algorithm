#https://www.acmicpc.net/problem/4963
#4963번-섬의 개수
#입력은 여러 개의 테스트 케이스로 이루어져 있다. 
#각 테스트 케이스의 첫째 줄에는 지도의 너비 w와 높이 h가 주어진다. 
#w와 h는 50보다 작거나 같은 양의 정수이다.
#둘째 줄부터 h개 줄에는 지도가 주어진다. 1은 땅, 0은 바다이다.

#BFS 풀이
from collections import deque

while True:
    #(h,w)
    w,h = map(int,input().split())
    if w==0 and h==0:
        break

    graph = [list(map(int,input().split())) for _ in range(h)]
    dx = [-1,1,0,0,-1,1,1,-1]
    dy = [0,0,-1,1,1,1,-1,-1]

    def bfs(x,y):
        q = deque()
        q.append((x,y))

        while q:
            x,y = q.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
                    q.append((nx,ny))
                    graph[nx][ny]=0

    result = 0 
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                bfs(i,j)
                result +=1
    print(result)

#------------------------------------------------------------------------------#
#DFS 풀이
while True:
    #(h,w)
    w,h = map(int,input().split())
    if w==0 and h==0:
        break

    graph = [list(map(int,input().split())) for _ in range(h)]
    dx = [-1,1,0,0,-1,1,1,-1]
    dy = [0,0,-1,1,1,1,-1,-1]

    def dfs(x,y):
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<h and 0<=ny<w and graph[nx][ny]==1:
                graph[nx][ny]=0
                dfs(nx,ny)

    result = 0 
    for i in range(h):
        for j in range(w):
            if graph[i][j]==1:
                dfs(i,j)
                result +=1
    print(result)