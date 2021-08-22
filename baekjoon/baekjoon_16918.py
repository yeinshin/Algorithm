#https://www.acmicpc.net/problem/16918
#16918번-봄버맨

from collections import deque
from copy import deepcopy 
import sys

input = sys.stdin.readline

#RxC인 직사각형 격자판, n초가 흐른 후의 격자판 상태
r,c,n = map(int,input().split())

#초기 상태, 1초 후 -> 2초 후 부터 폭탄 설치
board = [[m for m in input().rstrip()] for _ in range(r)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]
                
# 짝수 초때엔 폭탄 설치, 홀수 초때엔 폭탄 터트리기
sec = 2
while sec<=n:
    if sec%2==0:
        bombs = [['O']*c for _ in range(r)]
    else:
        for x in range(r):
            for y in range(c):
                if board[x][y]=='O':
                    bombs[x][y]='.'
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if 0<=nx<r and 0<=ny<c and bombs[nx][ny]=='O' and board[nx][ny]=='.':
                            bombs[nx][ny]='.'
                            
        board=deepcopy(bombs)

    sec+=1

if n==1 or n%2!=0:
    for i in range(r):
        print(''.join(board[i]))
else:
    for i in range(r):
        print(''.join(bombs[i]))