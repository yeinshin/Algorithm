# https://www.acmicpc.net/problem/14499
# 14499번-주사위 굴리기

# 지도의 세로크기: n, 가로크기:m, 주사위를 놓은 곳의 좌표:x,y, 명령의 개수:k
n, m, x, y, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
# 동: 1, 서:2, 북:3, 남:4
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
move = list(map(int, input().split()))
dice = [0]*6

for i in range(k):
    if 0 <= x+dx[move[i]-1] < n and 0 <= y+dy[move[i]-1] < m:
        x += dx[move[i]-1]
        y += dy[move[i]-1]
        if move[i] == 1:
            temp = dice[2]
            dice[2] = dice[0]
            dice[0] = dice[3]
            dice[3] = dice[5]
            dice[5] = temp
        elif move[i] == 2:
            temp = dice[3]
            dice[3] = dice[0]
            dice[0] = dice[2]
            dice[2] = dice[5]
            dice[5] = temp
        elif move[i] == 3:
            temp = dice[1]
            dice[1] = dice[0]
            dice[0] = dice[4]
            dice[4] = dice[5]
            dice[5] = temp
        else:
            temp = dice[5]
            dice[5] = dice[4]
            dice[4] = dice[0]
            dice[0] = dice[1]
            dice[1] = temp

        if arr[x][y] == 0:
            arr[x][y] = dice[5]
        else:
            dice[5] = arr[x][y]
            arr[x][y] = 0
        print(dice[0])
