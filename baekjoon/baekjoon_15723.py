#https://www.acmicpc.net/problem/15723
#15723번-n단 논법
from collections import deque
n = int(input())
graph = [[] for _ in range(26)]
for _ in range(n):
    a = input().split(' ')
    graph[ord(a[0])-97].append(ord(a[2])-97)
m = int(input())
for _ in range(m):
    a = input().split(' ')
    q = deque([ord(a[0])-97])
    while q:
        now = q.popleft()
        if now == ord(a[2])-97: 
            print('T')
            break
        for i in graph[now]:
            q.append(i)
    else: print('F')