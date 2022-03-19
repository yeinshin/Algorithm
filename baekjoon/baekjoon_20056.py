#https://www.acmicpc.net/problem/20056
#20056번-마법사 상어와 파이어볼
from collections import deque

#nxn, m개의 파이어볼, k번의 명령
N,M,K = map(int,input().split())
ball = deque([list(map(int,input().split())) for _ in range(M)])
dr = [-1,-1,0,1,1,1,0,-1]
dc = [0,1,1,1,0,-1,-1,-1]

graph = [[deque() for _ in range(N)] for _ in range(N)]
for _ in range(K):
    #모든 파이어볼이 자신의 방향 d로 속력 s칸 만큼 이동한다.
    while ball:
        r,c,m,s,d=ball.popleft()
        r = (r + s%N * dr[d]) % N
        c = (c + s%N * dc[d]) % N
        graph[r][c].append([m,s,d])

    #모든 파이어볼의 이동이 모두 끝난 뒤 2개 이상의 파이어볼이 있는 칸을 찾아준다.
    for r in range(N):
        for c in range(N):
            if len(graph[r][c])>=2:
                check,weight,fast,cnt = 0,0,0,len(graph[r][c])
                while graph[r][c]:
                    nm,ns,nd = graph[r][c].popleft()
                    weight+=nm
                    fast+=ns
                    if nd%2: check+=1
                    else: check-=1
                weight//=5
                fast//=cnt
                if weight:
                    dir = (0,2,4,6) if abs(check)==cnt else (1,3,5,7)
                    for d in dir: ball.append([r,c,weight,fast,d])
            elif len(graph[r][c])==1: ball.append([r,c]+graph[r][c].popleft())

print(sum([b[2] for b in ball]))




# from collections import deque
# N, M, K = map(int, input().split())
# ball = deque([list(map(int,input().split())) for _ in range(M)])

# MAP = [[deque() for _ in range(N+1)] for _ in range(N+1)]

# dx = [-1, -1, 0, 1, 1, 1, 0, -1]
# dy = [0, 1, 1, 1, 0, -1, -1, -1]

# for _ in range(K):
#     # 파이어볼 이동
#     while ball:
#         cr, cc, cm, cs, cd = ball.popleft()
#         nr = (cr + cs%N * dx[cd]) % N  # 1번-N번 행 연결되어있기 때문
#         nc = (cc + cs%N * dy[cd]) % N
#         MAP[nr][nc].append([cm, cs, cd])

#     # 2개 이상인지 체크
#     for r in range(1,N+1):
#         for c in range(1,N+1):
#             # 2개 이상인 경우 -> 4개의 파이어볼로 쪼개기
#             if len(MAP[r][c]) > 1:
#                 sum_m, sum_s, check, cnt = 0, 0, 0, len(MAP[r][c])
#                 while MAP[r][c]:
#                     _m, _s, _d = MAP[r][c].popleft()
#                     sum_m += _m
#                     sum_s += _s
#                     if _d % 2:check += 1
#                     else:check -= 1
#                 nd = (0,2,4,6) if abs(check)== cnt else (1,3,5,7)
#                 if sum_m//5:  # 질량 0이면 소멸
#                     for d in nd: ball.append((r, c, sum_m//5, sum_s//cnt, d))
#             # 1개인 경우
#             if len(MAP[r][c]) == 1:
#                 ball.append([r, c] + MAP[r][c].popleft())

# print(sum([f[2] for f in ball]))