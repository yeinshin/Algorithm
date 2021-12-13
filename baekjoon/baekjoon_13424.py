#https://www.acmicpc.net/problem/13424
#13424번-비밀 모임
INF = int(1e9)
for _ in range(int(input())):
    n,m = map(int,input().split())
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int,input().split())
        graph[a][b]=c
        graph[b][a]=c
    k = int(input())
    friend = list(map(int,input().split()))
    for i in range(1,n+1):
        graph[i][i]=0 
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                graph[i][j] = min(graph[i][j],graph[i][k]+graph[k][j])
        
    ans = []
    for i in range(1,n+1):
        cnt = 0
        for f in friend:
            cnt+=graph[f][i]
        ans.append((cnt,i))
        
    print(sorted(ans)[0][1])