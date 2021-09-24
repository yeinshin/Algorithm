#https://www.acmicpc.net/problem/1913
#1913번-달팽이
n = int(input())
m = int(input())
start = n**2
d = [[1,0],[0,1],[-1,0],[0,-1]]
graph = [[0]*n for _ in range(n)]
now = 0
x,y = -1,0
result = []
while start!=0:
    nx = d[now][0]+x
    ny = d[now][1]+y
    if start == m: result.append((nx+1,ny+1))
    if 0<=nx<n and 0<=ny<n:
        graph[nx][ny]=start
        x,y = nx,ny
        if x+d[now][0]>=n or y+d[now][1]>=n or x+d[now][0]<0 or y+d[now][1]<0 or graph[x+d[now][0]][y+d[now][1]]!=0:
            now+=1
            if now==4: now=0
    start-=1
for i in range(n):
    print(*graph[i],sep=' ')
print(result[0][0],result[0][1])