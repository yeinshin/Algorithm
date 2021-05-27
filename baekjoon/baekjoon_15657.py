#https://www.acmicpc.net/problem/15657
#15657번-N과 M(8)

n,m = map(int,input().split())
array = sorted(list(map(int,input().split())))
visited = list()

def dfs(cnt,now):
    if cnt == m:
        print(*visited)
        return
    for a in array:
        if now<=a:
            visited.append(a)
            dfs(cnt+1,a)
            visited.pop()
dfs(0,0)