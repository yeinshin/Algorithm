#https://www.acmicpc.net/problem/4396
#4396번-지뢰 찾기
n = int(input())
a = [input() for _ in range(n)]
b = [list(map(str,input())) for _ in range(n)]
dx,dy=[0,0,-1,1,-1,-1,1,1],[1,-1,0,0,-1,1,-1,1]

def check (x,y):
    cnt = 0 
    for i in range(8):
        nx = dx[i]+x
        ny = dy[i]+y
        if 0<=nx<n and 0<=ny<n and a[nx][ny]=='*': cnt+=1
    return cnt
for i in range(n):
    for j in range(n):
        if b[i][j]=='x' and a[i][j]=='.':b[i][j]=check(i,j)
        elif b[i][j]=='x' and a[i][j]=='*':
            for x in range(n):
                for y in range(n):
                    if a[x][y]=='*': b[x][y]='*'
                    
for i in range(n):
    print(*b[i],sep='')