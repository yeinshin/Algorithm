#https://www.acmicpc.net/problem/15650
#15650번-N과 M(2)
#itertools의 combinations를 이용한 풀이(2)

n,m = map(int,input().split())
visited = [False]*(n+1)
arr = list()

def dfs(cnt):
    if cnt==m:
        print(*arr)
        return
    
    for i in range(1,n+1):
        if not visited[i]: #방문을 하지 않았을 때!
            visited[i]=True
            arr.append(i)
            
            dfs(cnt+1)
            arr.pop()

            for j in range(i+1,n): #i보다 큰 경우만 visited를 False으로 바꿔줌
                visited[j]=False
            
dfs(0)