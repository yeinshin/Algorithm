#https://www.acmicpc.net/problem/16236
#16236번-아기 상어

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n = int(input())
a = [ list(map(int, input().split())) for _ in range(n) ]
dx, dy = (-1, 1, 0, 0), (0, 0, -1, 1)

def bfs():
    q = []
    check = [[False]*n for _ in range(n)]
    #상어를 찾아서 heapq에 넣어주기 (거리,x좌표,y좌표)
    for i in range(n):
        for j in range(n):
            if a[i][j] == 9:
                heappush(q, (0, i, j))
                a[i][j] = 0
                break
    #현재 상어의 크기, 물고기를 먹은 횟수
    body, eat, ans  = 2, 0, 0
    check = [[False]*n for _ in range(n)]
    #bfs 시작!
    while q:
        d, x, y = heappop(q)

        #빈칸은 아니면서 body보다 작은 물고기를 골라보자
        if 0 < a[x][y] < body:
            eat += 1
            #이미 먹었으니 0으로 처리
            a[x][y] = 0
            #상어의 크기만큼 물고기를 먹었으면 크기가 1 증가
            if eat == body:
                body += 1
                eat = 0
            #현재까지 이동한 거리를 ans 변수에 계속해서 갱신 시켜준다
            ans = d
            #가장 가까운 물고기 먹었으니 그 위치에서의 가까운 물고기를 수집해야하므로 우선순위 큐를 초기화 시켜준다.
            q = []
            #현재 물고기를 먹은 위치에서 다시 가까운 물고기를 찾아야하니 visited 리스트를 초기화 시켜준다
            check = [[False]*n for _ in range(n)]
        
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0<=nx<n and 0<=ny<n and not check[nx][ny] and body>=a[nx][ny]:
                check[nx][ny] = True
                heappush(q, (d+1, nx, ny))

    return ans

print(bfs())