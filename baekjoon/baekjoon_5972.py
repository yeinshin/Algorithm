#https://www.acmicpc.net/problem/5972
#5972번-택배 배송
#농부 현서는 헛간 1에 있고 농부 찬홍이는 헛간 N에 있습니다.
import heapq
INF = int(1e9)
n,m = map(int,input().split())
distance = [INF]*(n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

q = []
heapq.heappush(q,(0,1))
distance[1]=0
while q:
    dist, now = heapq.heappop(q)
    if distance[now]<dist:
        continue
    for i in graph[now]:
        cost = i[1]+dist
        if cost<distance[i[0]]:
            distance[i[0]]=cost
            heapq.heappush(q,(cost,i[0]))
print(distance[n])