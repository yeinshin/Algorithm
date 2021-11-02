#https://www.acmicpc.net/problem/18290
#18290번-NM과 K(1)/(풀이참고)
n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx,dy = [0, 0, 1, -1],[1, -1, 0, 0]
answer = -1000000

def dfs(px, py, index, sum):
    if index == k:
        global answer
        answer = max(answer,sum)
        return

    for x in range(px, n):
        for y in range(py if x==px else 0, m):
            # 현재 위치 방문했었는지 확인
            if visited[x][y]:
                continue
            # 동서남북 방문 했었는지 확인
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < n and 0 <= ny < m and visited[nx][ny]:break        
            # 방문
            else:
                visited[x][y] = True
                dfs(x, y, index+1, sum+arr[x][y])
                visited[x][y] = False
dfs(0, 0, 0, 0)
print(answer)