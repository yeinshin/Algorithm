#https://www.acmicpc.net/problem/2644
#2644번-촌수계산

from collections import deque

#전체 사람의 수
n = int(input())
#촌수를 계산해야 하는 서로 다른 두 사람의 번호
p1,p2 = map(int,input().split())
#부모 자식들 간의 관계의 개수
m = int(input())
#x:부모 y:자식
family = [[] for _ in range(n+1)]
for _ in range(m):
    x,y = map(int,input().split())
    family[x].append(y)
    family[y].append(x)

visited = [False for _ in range(n+1)]
count = [0]*(n+1)

def bfs(start,end):
    q = deque([start])
    visited[start]=True

    while q:
        parent=q.popleft()
        for son in family[parent]:
            if not visited[son]:
                visited[son]=True
                q.append(son)
                count[son] = count[parent] + 1
            if son == end:
                break
bfs(p1,p2)

if count[p2]: print(count[p2])
else: print(-1)

