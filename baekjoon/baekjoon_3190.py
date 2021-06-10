#https://www.acmicpc.net/problem/3190
#3190번-뱀 / 풀이 확인함

from collections import deque

n= int(input())
k= int(input())
board = [[0]*n for _ in range(n)]
for _ in range(k):
    i,j = map(int,input().split())
    board[i-1][j-1]=1

l = int(input())
direc = list()
for _ in range(l):
    x,c = input().split()
    direc.append((int(x),c))

dx = [0,1,0,-1]
dy = [1,0,-1,0]

def simul():
    x,y = 0,0
    #뱀의 시작 위치는 (0,0) 이므로 (0,0)을 2로 표현
    board[0][0]=2
    time=0
    snake = deque([(0,0)])
    
    #뱀의 방향 정보 / 초반엔 동쪽에서 시작
    direction = 0

    #방향 변환 정보
    now = 0

    while True:
        nx = dx[direction] + x
        ny = dy[direction] + y
        #맵을 벗어 나지 않고 뱀의 몸통이 아닐때
        if 0<=nx<n and 0<=ny<n and board[nx][ny]!=2:
            ##가려는 칸에 사과가 없으면
            if board[nx][ny]==0:
                qx,qy = snake.popleft()
                board[qx][qy]=0
            
            board[nx][ny]=2
            snake.append((nx,ny))
            x,y=nx,ny
            time+=1

        #맵을 벗어나거나 뱀의 몸통일때
        else:
            time+=1
            break #즉시 종료

        if now<l and direc[now][0]==time:
            if direc[now][1]=='L':
                direction = (direction-1)%4
            else:
                direction = (direction+1)%4
            now+=1
    
    return time

print(simul())
        
        
                
                
    








