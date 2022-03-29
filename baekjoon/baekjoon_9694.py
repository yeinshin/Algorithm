#https://www.acmicpc.net/problem/9694
#9694번-무엇을 아느냐가 아니라 누구를 아느냐가 문제다
import heapq
for t in range(int(input())):
    n,m = map(int,input().split())
    graph = [[] for _ in range(m)]
    INF = int(1e9)
    dist = [INF]*m
    node = [-1]*m

    for _ in range(n):
        a,b,c = map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    def dijkstra():
        q = []
        heapq.heappush(q,(0,0))
        dist[0]=0
        while q:
            d,now = heapq.heappop(q)
            if dist[now]<d: continue

            for i in graph[now]:
                cost = i[1] + d
                if cost<dist[i[0]]:
                    dist[i[0]]=cost
                    node[i[0]]=now
                    heapq.heappush(q,(cost,i[0]))
    dijkstra()

    print("Case #%d: "%(t+1),end='')
    ans=[]
    if dist[m-1]!=INF:
        k = m-1
        while node[k]!=-1:
            ans.append(k)
            k = node[k]
        ans +=[0]
        print(*ans[::-1],sep=' ')
    else:print(-1)