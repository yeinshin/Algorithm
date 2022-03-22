#https://www.acmicpc.net/problem/1005
#1005번-ACM Craft
from collections import deque
for _ in range(int(input())):
    n,k = map(int,input().split())
    time = [0]+list(map(int,input().split()))
    indegree = [0]*(n+1)
    graph = [[] for _ in range(n+1)]

    for _ in range(k):
        a,b = map(int,input().split())
        graph[a].append(b)
        indegree[b]+=1

    w = int(input())

    def topology_sort():
        q = deque()
        check = [0]*(n+1)

        for i in range(1,n+1):
            if indegree[i]==0: q.append(i)
        
        while q:
            now = q.popleft()

            for i in graph[now]:
                indegree[i]-=1
                check[i] = max(check[i],time[now]+time[i])
                if indegree[i]==0:
                    q.append(i)
                    time[i] = check[i]
        print(time[w])

    topology_sort()