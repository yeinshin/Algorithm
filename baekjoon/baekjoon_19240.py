#https://www.acmicpc.net/problem/19240
#19240번-장난감 동맹군

from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n,m = map(int,input().split())
    graph = [set() for _ in range(n+1)]
    team = [0]*(n+1)

    for _ in range(m):
        a,b = map(int,input().split())
        graph[a].add(b)
        graph[b].add(a)

    def bfs(x):
        q = deque([x])
        team[x]=1
        while q:
            x = q.popleft()
            for i in graph[x]:
                if team[i]==team[x]:
                    return False
                elif not team[i]:
                    team[i]=3-team[x]
                    q.append(i)
        return True

    for i in range(1,n+1):
        if not team[i]:
            if not bfs(i):
                print('NO')
                break
    else: print('YES')