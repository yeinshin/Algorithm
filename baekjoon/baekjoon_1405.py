#https://www.acmicpc.net/problem/1405
#1405번-미친 로봇

n,east,west,south,north = map(int,input().split())

#east,west,south,north
dx=[0,0,1,-1]
dy=[1,-1,0,0]

per=[east/100,west/100,south/100,north/100]

visited = [(0,0)]
result = 0

def dfs(x,y,cnt,percent):
    global result

    #n만큼 이동을 다 하면,
    if cnt == n:
        result += percent
        return
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx,ny) not in visited:
            visited.append((nx,ny))
            dfs(nx,ny,cnt+1,percent*per[i])
            visited.pop()

dfs(0,0,0,1)
print("%0.9f"%result)
