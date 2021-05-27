#https://www.acmicpc.net/problem/15656
#15656번-N과 M(7)

n,m = map(int,input().split())
array = sorted(list(map(int,input().split())))
visited = list()

def dfs(cnt):
    if cnt == m:
        print(*visited)
        return
    
    for a in array:
        visited.append(a)
        dfs(cnt+1)
        visited.pop()

dfs(0)