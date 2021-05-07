#3부<문제>17번-경쟁적 전염/다시 풀어보기

# import sys
# from collections import deque

# global s
# n,k = map(int,sys.stdin.readline().split())


# graph = [[int(m) for m in sys.stdin.readline().split()] for _ in range(n)]
# data = [[0]*(n) for _ in range(n)]

# #s초 후에 (x,y)에 존재하는 바이러스의 종류
# s,x,y = map(int,sys.stdin.readline().split())

# da = [-1,1,0,0]
# db = [0,0,-1,1]

# def bfs(x,y):

#     global s
    
#     q=deque()
#     q.append((x,y))
#     data[x][y]=graph[x][y]
#     # print("graph[x][y]:",graph[x][y])
#     for _ in range(s):
#         if q:
#             a,b = q.popleft()
#             # print('a:',a,'b:',b)
#             for i in range(4):
#                 na = a + da[i]
#                 nb = b + db[i]

#                 if na>=0 and nb>=0 and na<n and nb<n:
#                     if data[na][nb]==0:
#                         q.append((na,nb))
#                         data[na][nb]=graph[x][y]

        
    

# for i in range(1,k+1):               
#     for a in range(n):
#         for b in range(n):
#             if graph[a][b]==i:
#                 bfs(a,b)

# if data[x-1][y-1]!=0:
#     print(data[x-1][y-1])
# else:
#     print(0)

# print(*data,sep='\n')

from collections import deque

n, k = map(int, input().split())
test = [] # 전체 맵 정보 담는 리스트
data =[] # 바이러스 정보를 담는 리스트
for i in range(n):
    test.append(list(map(int, input().split())))
    for j in range(n):
        if test[i][j] != 0:
            # 바이러스 숫자, x위치, y위치, 시간 을 입력받는다.
            data.append((test[i][j], i, j, 0))

rs, rx, ry = map(int, input().split())
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

data.sort()
q = deque(data)

while q:
    virus, x, y, time = q.popleft()
    
    if time == rs:
        break
    for i in range(4):
        mx = x + dx[i]
        my = y + dy[i]
        if 0 <= mx < n and 0 <= my < n:
            if test[mx][my] == 0:
                test[mx][my] = virus
                q.append((virus, mx, my, time+1))

print(test[rx-1][ry-1])