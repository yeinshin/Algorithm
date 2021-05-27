#https://www.acmicpc.net/problem/15654
#15654번-N과 M(5)

import sys
intput = sys.stdin.readline

n,m = map(int,input().split())
array = sorted(list(map(int,input().split())))
visited = list()

def dfs(cnt):
    if cnt == m:
        print(*visited)
        return
    
    for a in array:
        if a not in visited:
            visited.append(a)
            dfs(cnt+1)
            visited.pop()

dfs (0)
