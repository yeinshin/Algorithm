#https://www.acmicpc.net/problem/10451
#10451번-순열 사이클
#사이클 판별
#1.무방향 그래프 - 유니온 파인드
#2.방향 그래프 - DFS

def dfs(now,array,visited):
    i = array[now]
    if not visited[i]:
        visited[i]=True
        dfs(i,array,visited)

t = int(input())
for i in range(t):
    n = int(input())
    array = [0]+list(map(int,input().split()))
    visited = [False]*(n+1)
    cnt=0

    for a in range(1,n+1):
        if visited[a]==False:
            dfs(a,array,visited)
            cnt+=1
    print(cnt)


