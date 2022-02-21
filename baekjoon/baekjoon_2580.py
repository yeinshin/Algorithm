#https://www.acmicpc.net/problem/2580
#2580번-스도쿠
import sys
input = sys.stdin.readline
sdoku = []
zero = []
for i in range(9):
    s = list(map(int,input().split()))
    for j in range(9):
        if s[j]==0:zero.append((i,j))
    sdoku.append(s)

def check(x,y,value):
    for i in range(9):
        if i!=x and sdoku[i][y]==value: return False
    for j in range(9):
        if j!=y and sdoku[x][j]==value: return False
    
    if 0<=x<3: a = 0
    elif 3<=x<6: a = 3
    else: a = 6

    if 0<=y<3: b = 0
    elif 3<=y<6: b= 3
    else: b = 6

    for i in range(a,a+3):
        for j in range(b,b+3):
            if i!=x and j!=y and sdoku[i][j]==value: return False

    return True

def backtracking(cnt,idx):
    if cnt==len(zero):
        for i in range(9):
            print(*sdoku[i],sep=' ')
        exit(0)

    for j in range(1,10):
        x,y = zero[idx][0],zero[idx][1] 
        if sdoku[x][y]==0 and check(x,y,j):
            sdoku[x][y]=j
            backtracking(cnt+1,idx+1)
            sdoku[x][y]=0

backtracking(0,0)