#2부<문제>3번-전보
#다익스트라 알고리즘으로 문제 풀이

import sys
import heapq

input=sys.stdin.readline
INF=int(1e9)

#n:도시의 개수, m:통로의 개수, c:메시지를 보내고자 하는 도시
n,m,c=map(int,input().split())
distance=[INF]*(n+1)
graph=[[] for _ in range(n+1)]

for _ in range(m):

    #특정 도시 x에서 다른 특정 도시 y로 이어지는 통로가 있으며 메세지가 전달되는 시간이 z
    x,y,z=map(int,input().split())
    graph[x].append((y,x))

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

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

#다익스트라 함수 실행
dijkstra(c)

#도시 c에서 보낸 메시지를 받게 되는 도시의 개수
city=0

#도시들이 모두 메시지를 받는 데까지 걸리는 시간
times=0
for i in range(1,n+1):
    if distance[i]!=INF:
        city+=1
        times=max(times,distance[i])

#city 정보에는 출발 노드 수도 포함되어 있음
print(city-1,times)