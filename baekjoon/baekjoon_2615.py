#https://www.acmicpc.net/problem/2615
#2615번-오목

badook = [list(map(int,input().split())) for _ in range(19)]
dx = [1, 1, 0, -1] # 하(↓), 우하(⬊), 우(➞), 우상(⬈)
dy = [0, 1, 1, 1]
def check(i,j,now):
    x,y = i,j
    for i in range(4):
        cnt = 1
        nx,ny = dx[i]+x,dy[i]+y
        while 0<=nx<19 and 0<=ny<19 and badook[nx][ny]==now:
            cnt+=1
            if cnt==5:
                if 0<=x-dx[i]<19 and 0<=y-dy[i]<19 and badook[x-dx[i]][y-dy[i]]==now:break
                if 0<=nx+dx[i]<19 and 0<=ny+dy[i]<19 and badook[nx+dx[i]][ny+dy[i]]==now:break
                return True
            nx+=dx[i]
            ny+=dy[i]
    
for i in range(19):
    for j in range(19):
        if badook[i][j] and check(i,j,badook[i][j]):
            print(badook[i][j])
            print(i+1,j+1)
            exit()
print(0)