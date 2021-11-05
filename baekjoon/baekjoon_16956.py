#https://www.acmicpc.net/problem/16956
#16956번-늑대와 양
n,m = map(int,input().split())
graph = [list(input()) for _ in range(n)]
check = False
dx,dy = [0,0,-1,1],[1,-1,0,0]
for x in range(n):
    for y in range(m):
        if graph[x][y]=='W':
            for z in range(4):
                nx,ny = dx[z]+x,dy[z]+y
                if 0<=nx<n and 0<=ny<m and graph[nx][ny]=='S':
                    check = True
                    break
        
        elif graph[x][y]=='.': graph[x][y]='D'
if not check:
    print(1)
    for i in range(n):
        print(*graph[i],sep='')
else: print(0)