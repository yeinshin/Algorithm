#https://www.acmicpc.net/problem/20208
#20208번-진우의 민트초코우유(풀이참고)
def dfs(jwx, jwy, hp, milk):
    global ans
    for x, y in milks:
        if village[x][y] == 2:	# 현재까지 마시지 않은 우유인가
            dist = abs(jwx - x) + abs(jwy - y)
            if dist <= hp:		# 현재 체력으로 도달할 수 있는 위치인가
                village[x][y] = 0	# 보드 위에 이번 우유를 마셨다고 표시
                dfs(x, y, hp + h - dist, milk + 1)
                village[x][y] = 2	# 복구

    if abs(jwx - hx) + abs(jwy - hy) <= hp: # 다른 우유를 먹으러 갈 체력이 안될때 if 문 check
        ans = max(ans, milk)

n, m, h = map(int, input().split())
village = [list(map(int, input().split())) for _ in range(n)]

milks = []      # 우유의 위치를 저장할 리스트
hx, hy = 0, 0   # 집의 위치
for i in range(n):
    for j in range(n):
        if village[i][j] == 1:
            hx, hy = i, j
            
        if village[i][j] == 2:
            milks.append((i, j))
ans = 0
dfs(hx, hy, m, 0)
print(ans)