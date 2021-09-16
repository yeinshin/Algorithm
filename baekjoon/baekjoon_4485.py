#https://www.acmicpc.net/problem/4485
#4485번-녹색 옷 입은 애가 젤다지?
import heapq
cnt=0
while True:
    n = int(input())
    if n==0: break
    cnt+=1
    graph = [list(map(int,input().split())) for _ in range(n)]
    distance = [[int(1e9)]*n for _ in range(n)]

    q = []
    heapq.heappush(q,(graph[0][0],0,0))
    distance[0][0]=graph[0][0]
    while q:
        dist,x,y= heapq.heappop(q)
        if distance[x][y]<dist:
            continue
        for nx,ny in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
            if 0<=nx<n and 0<=ny<n:
                cost = graph[nx][ny]+dist
                if cost<distance[nx][ny]:
                    distance[nx][ny]=cost
                    heapq.heappush(q,(cost,nx,ny))
    print('Problem %d:'%cnt+' %d'%distance[n-1][n-1])
