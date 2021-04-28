#3부<문제>40번-숨바꼭질

import sys
import heapq

INF=int(1e9)
input=sys.stdin.readline

n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
distance=[INF]*(n+1)

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        
        for i in graph[now]:
            cost=i[1]+dist

            if cost < distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(1)

#1번 헛간으로부터 최단 거리가 가장 먼 헛간의 거리
max_distance=max(distance[1:])


#숨어야 하는 헛간 중 가장 작은 헛간의 번호를 저장할 변수
min_barn=n
#숨어야 하는 헛간의 거리와 같은 거리를 가진 헛간의 수를 저장할 변수
count=0
for i in range(1,n+1):
    if distance[i]==max_distance:
        min_barn=min(min_barn,i)
        count+=1          

print(min_barn,max_distance,count,end='\n\n')

