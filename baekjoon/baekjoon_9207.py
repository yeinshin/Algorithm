#https://www.acmicpc.net/problem/9207
#9207번-페그 솔리테어
import sys
sys.setrecursionlimit(100000)
t = int(input())
dx,dy = [1,-1,0,0],[0,0,-1,1]

def dfs(board,cnt):
        global check
        for x in range(5):
            for y in range(9):
                if board[x][y]=='o':
                    for i in range(4):
                        nx = dx[i]+x
                        ny = dy[i]+y
                        if 0<=nx<5 and 0<=ny<9 and board[nx][ny]=='o':
                            nnx = dx[i]+nx
                            nny = dy[i]+ny
                            if 0<=nnx<5 and 0<=nny<9 and board[nnx][nny]=='.':
                                board[x][y]='.'
                                board[nx][ny]='.'
                                board[nnx][nny]='o'
                                dfs(board,cnt+1)
                                board[x][y]='o'
                                board[nx][ny]='o'
                                board[nnx][nny]='.'                       
        check = max(check,cnt)
        return

for i in range(t):
    board = [list(input()) for _ in range(5)]
    if i!=t-1: s=input()
    pin = 0
    ans = []
    for i in range(5):
        for j in range(9):
            if board[i][j]=='o':pin+=1

    check = 0
    dfs(board,0)
    print(pin-check,check)