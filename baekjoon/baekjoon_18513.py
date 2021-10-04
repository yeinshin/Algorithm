#https://www.acmicpc.net/problem/18513
#18513번-샘터
from collections import deque
n,k = map(int,input().split())
saemteo = list(map(int,input().split()))
visited = set()
cnt = 0
distance = 0
q = deque()
for s in saemteo:
    q.append((s,0))
    visited.add(s)
while q:
    now,d = q.popleft()
    for i in (1,-1):
        if i+now not in visited:
            distance+=d+1
            cnt+=1
            visited.add(i+now)
            q.append((i+now,d+1))
            if cnt==k:
                print(distance)
                exit()

