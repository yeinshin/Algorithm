#https://www.acmicpc.net/problem/10282
#10282번-해킹
import heapq
for _ in range(int(input())):
    #n:컴퓨터의 개수, d:의존성의 개수, c:해킹당한 컴퓨터의 번호
    n,d,c = map(int,input().split())
    graph = [[] for _ in range(n+1)]
    INF = int(1e9)
    dist = [INF]*(n+1)
    for _ in range(d):
        x,y,z = map(int,input().split())
        graph[y].append((x,z))

    q = []
    heapq.heappush(q,(0,c))
    dist[c]=0
    while q:
        time,node = heapq.heappop(q)
        if dist[node]<time: continue
        for i in graph[node]:
            #i[0]:node 번호 , i[1]:걸리는 시간
            cost = i[1]+time
            if cost<dist[i[0]]:
                dist[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))
    ans = [1,0]
    for i in range(1,n+1):
        if i!=c and dist[i]!=INF:
            ans[0]+=1
            ans[1]=max(ans[1],dist[i])
    print(*ans,sep=' ')

    