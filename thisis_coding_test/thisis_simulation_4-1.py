#2부<문제>예제4-1번-상하좌우

n = int(input())
move = list(input().split())
x,y = 0,0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
mv = ['U','D','L','R']

for m in move:
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0<=nx<n and 0<=ny<n and m==mv[i]:
            x,y=nx,ny
            print('x:',x,'y:',y)
print(x+1,y+1)

