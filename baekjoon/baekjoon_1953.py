#https://www.acmicpc.net/problem/1953
#1953번-팀배분

from collections import deque
def bfs(x):
    color[x] = 1
    Q = deque([x])
    while Q:
        p = Q.popleft()
        for q in adj[p]:
            if color[q]: continue
            color[q] = 3-color[p]
            Q.append(q)

n = int(input())
adj = [[]] + [list(map(int,input().split()))[1:] for i in range(n)]
color = [0] * (n+1)

for i in range(1, n+1):
    if not color[i]: bfs(i)
one = [x for x in range(1, n+1) if color[x] == 1]
two = [x for x in range(1, n+1) if color[x] == 2]
if not two: two.append(one.pop())

print(len(one))
print(*one)
print(len(two))
print(*two)