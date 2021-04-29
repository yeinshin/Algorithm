#3부<문제>39번-화성 탐사/ 다시 풀어보기

import sys
import heapq

INF= int(1e9)
input=sys.stdin.readline

dx=[-1,0,1,0]
dy=[0,-1,0,1]

for _ in range(int(input())):
    n=int(input())

    graph=[[int(m) for m in input().split()] for _ in range(n)]

    distance=[[INF]*n for _ in range(n)]

    x,y=0,0

    q=[]
    heapq.heappush(q,(graph[x][y],x,y))

    while q:
        dist,x,y=heapq.heappop(q)

        if distance[x][y] < dist:
            continue
        
        #상,하,좌,우로 이동 가능하기 때문에 range(4)로 둔다
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx>=n or nx < 0 or ny>=n or ny < 0:
                continue

            cost = dist + graph[nx][ny]

            if cost < distance[nx][ny]:
                distance[nx][ny]=cost
                heapq.heappush(q,(cost,nx,ny))

    print(distance[n-1][n-1]) 