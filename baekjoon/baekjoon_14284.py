#https://www.acmicpc.net/problem/14284
#14284번-간선 이어가기 2
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]
dist = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

s,t = map(int,input().split())

def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    dist[start]=0
    while q:
        c,n = heapq.heappop(q)
        if c>dist[n]:continue
        for i in graph[n]:
            cost = i[1]+c
            if dist[i[0]]>cost:
                heapq.heappush(q,(cost,i[0]))
                dist[i[0]]=cost

dijkstra(s)
print(dist[t])
