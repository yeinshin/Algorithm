#14226번-이모티콘 / 다시 풀어보기

import sys
from collections import deque

#s개의 이모티콘
s=int(sys.stdin.readline())
visited = [[-1]*1001 for _ in range(1001)]
visited[1][0]=0

def bfs(x,y):
    q=deque()
    q.append((x,y))

    while q:
        x,y = q.popleft()

        if x == s:
            return visited[x][y]

        #복사, 붙여넣기, 이모티콘 하나 삭제
        for nx in ((x,x),(x+y,y),(x-1,y)):

            if 0<=nx[0]<1001 and visited[nx[0]][nx[1]]==-1:
                visited[nx[0]][nx[1]] = visited[x][y]+1
                q.append((nx[0],nx[1]))

print(bfs(1,0))