#https://www.acmicpc.net/problem/17070
#17070번-파이프 옮기기 1 (풀이참고)
#shape에서 가로는 0, 세로는 1, 대각선은 2로 표시한다 -> 방문 체크할 필요 없음 왜냐면 back을 할 수 없기 때문

import sys
input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def dfs(x, y, shape):
    global ans
    if x == n-1 and y == n-1:
        ans += 1
        return
    #가로
    if shape == 0 or shape == 2:
        if y + 1 < n and a[x][y+1] == 0:
            dfs(x, y+1, 0)
    #세로
    if shape == 1 or shape == 2:
        if x + 1 < n and a[x+1][y] == 0:
            dfs(x+1, y, 1)
    #대각선
    if shape == 0 or shape == 1 or shape == 2:
        if x + 1 < n and y + 1 < n and a[x+1][y] == 0 and a[x][y+1] == 0 and a[x+1][y+1] == 0:
            dfs(x+1, y+1, 2)
dfs(0, 1, 0)
print(ans)

