#https://www.acmicpc.net/problem/11725
#11725번-트리의 부모 찾기

from collections import deque

#노드의 개수
n = int(input()) 
tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,input().split())
    tree[a].append(b)
    tree[b].append(a)

q=deque([1])
answer = {} #dictionary 선언
visited = [False for _ in range(n+1)]

while q:
    parent = q.popleft()
    for i in tree[parent]:
        if not visited[i]:
            answer[i] = parent
            q.append(i)
            visited[i]=True
        
for i in range(2,n+1):
    print(answer[i])

